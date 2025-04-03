
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import cloudscraper
import pandas as pd
import time
import datetime
import schedule
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import os
import mysql.connector
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://www.forebet.com"
START_URL = f"{BASE_URL}/en/football-tips-and-predictions-for-today"
OUTPUT_DIR = "forebet_data"
MAX_RETRIES = 3
REQUEST_DELAY = 3  # delay between requests to avoid detection


def setup_driver() -> webdriver.Chrome:
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0 Safari/537.36")
    options.add_argument("--headless=new")
    prefs = {
        "profile.managed_default_content_settings.images": 2,
        "profile.managed_default_content_settings.stylesheet": 2
    }
    options.add_experimental_option("prefs", prefs)
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def load_full_page(driver: webdriver.Chrome) -> str:
    print("\n🌐 Loading page and clicking 'More' buttons...")
    driver.get(START_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rcnt")))
    last_height = driver.execute_script("return document.body.scrollHeight")
    attempts = 0
    while attempts < MAX_RETRIES:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        try:
            more_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@id="mrows"]/span[text()="More"]'))
            )
            more_button.click()
            print("🔘 Clicked 'More' button")
            time.sleep(2)
            attempts = 0
        except Exception:
            attempts += 1
            print(f"⏳ No 'More' button found (attempt {attempts}/{MAX_RETRIES})")
            time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print("✅ Finished loading page content")
    return driver.page_source


def extract_standing(soup: BeautifulSoup, team_name: str) -> str:
    full_standings = soup.select_one("#stand_hidden table.standings")
    short_standings = soup.select_one("#short_standings table.standings")
    for table in [full_standings, short_standings]:
        if not table:
            continue
        for row in table.find_all("tr"):
            cols = row.find_all("td")
            if len(cols) >= 2 and team_name.lower() in cols[1].text.strip().lower():
                return cols[0].text.strip()

    teams_container = soup.find("div", class_="teamtablesp_container")
    if teams_container:
        left = teams_container.find("span", class_="teamtableleft")
        right = teams_container.find("span", class_="teamtableright")
        if left and team_name.lower() in soup.text.lower():
            return left.text.strip().split()[0]
        if right and team_name.lower() in soup.text.lower():
            return right.text.strip().split()[0]
    return ""


def correct_game_url(raw_href: str) -> Optional[str]:
    if raw_href.startswith('http'):
        if 'forebet.com' in raw_href:
            parts = raw_href.split('forebet.com')
            corrected_path = parts[-1] if len(parts) > 1 else parts[0]
            return BASE_URL + corrected_path
        else:
            print(f"⚠️ Invalid external URL detected: {raw_href}")
            return None
    elif raw_href.startswith('/'):
        return BASE_URL + raw_href
    else:
        return f"{BASE_URL}/{raw_href}"


def fix_forebet_url(url):
    if url.count("https://www.forebet.com") > 1:
        url = "https://www.forebet.com" + url.split("https://www.forebet.com", 1)[1]
    return url


def fetch_match_details(game_url, home_team, away_team, scraper) -> Dict[str, str]:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            time.sleep(REQUEST_DELAY)
            response = scraper.get(game_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                home_rank = extract_standing(soup, home_team)
                away_rank = extract_standing(soup, away_team)
                return {"Home Rank": home_rank, "Away Rank": away_rank}
        except Exception as e:
            if attempt == MAX_RETRIES:
                print(f"❌ Failed to fetch standings for {home_team} vs {away_team}: {str(e)}")
    return {"Home Rank": "", "Away Rank": ""}


def parse_page(html: str, scraper: cloudscraper.CloudScraper) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    matches = soup.find_all("div", class_="rcnt")
    print(f"\n🔍 Found {len(matches)} matches to parse...")
    temp_matches = []
    predictions = []

    for i, match in enumerate(matches, start=1):
        try:
            meta = match.find("meta", {"itemprop": "name"})
            prediction_span = match.find("span", class_="forepr")
            probs = match.find("div", class_="fprc")
            link_tag = match.find("a", class_="tnmscn")
            time_tag = match.find("span", class_="date_bah")
            time_element = match.find("time", {"itemprop": "startDate"})
            score_full = match.find("b", class_="l_scr")
            score_half = match.find("span", class_="ht_scr")
            et_min = match.find("div", class_="ladtm")
            et_minute = match.find("span", class_="l_min")

            if not all([meta, prediction_span, probs, link_tag]):
                continue

            game_name = meta.get("content", "").strip()
            prediction = prediction_span.get_text(strip=True)
            match_time = time_tag.text.strip() if time_tag else ""
            match_datetime = time_element.get("datetime", "") if time_element else ""
            match_score = score_full.text.strip() if score_full else ""
            half_time_score = score_half.text.strip() if score_half else ""
            extra_time = et_min.text.strip() if et_min else ""
            extra_minute = et_minute.text.strip() if et_minute else ""

            prob_spans = probs.find_all("span")
            if len(prob_spans) != 3:
                continue
            prob_1 = prob_spans[0].text.strip()
            prob_x = prob_spans[1].text.strip()
            prob_2 = prob_spans[2].text.strip()

            raw_href = link_tag['href']
            game_url = fix_forebet_url(correct_game_url(raw_href))
            if not game_url:
                continue
            home_team = link_tag.find("span", class_="homeTeam").text.strip()
            away_team = link_tag.find("span", class_="awayTeam").text.strip()

            temp_matches.append({
                "base": {
                    "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Game": game_name,
                    "Time": match_time,
                    "ISO Time": match_datetime,
                    "Score": match_score,
                    "Half-Time Score": half_time_score,
                    "ET": extra_time,
                    "ET Minute": extra_minute,
                    "Prediction": prediction,
                    "1%": prob_1,
                    "X%": prob_x,
                    "2%": prob_2,
                    "Home Team": home_team,
                    "Away Team": away_team,
                    "Match URL": game_url
                },
                "url": game_url,
                "home": home_team,
                "away": away_team
            })

        except Exception as e:
            print(f"⚠️ Error processing match #{i}: {str(e)}")
            continue

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            executor.submit(fetch_match_details, m["url"], m["home"], m["away"], scraper): m
            for m in temp_matches
        }
        for future in as_completed(futures):
            match = futures[future]
            result = future.result()
            match["base"].update(result)
            predictions.append(match["base"])

    return predictions


def save_to_excel(data: List[Dict[str, str]]) -> str:
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/forebet_predictions_{timestamp}.xlsx"
    df = pd.DataFrame(data)
    df["Home Rank"] = pd.to_numeric(df["Home Rank"], errors="coerce")
    df = df.sort_values(by="Home Rank", ascending=True)
    with pd.ExcelWriter(filename, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Predictions")
        writer.sheets["Predictions"].set_column("A:P", 20)
    print(f"\n💾 Saved {len(df)} predictions to {filename}")
    return filename


def save_to_mysql(data: List[Dict[str, str]]):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="forebet_db",
            charset="utf8mb4"
        )
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO forebet_matches (
                timestamp, game, time_str, iso_time, score, half_time_score,
                et, et_minute, prediction, prob_1, prob_x, prob_2,
                home_team, away_team, home_rank, away_rank, match_url
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        for row in data:
            cursor.execute(insert_query, (
                row["Timestamp"], row["Game"], row["Time"], row["ISO Time"], row["Score"],
                row["Half-Time Score"], row["ET"], row["ET Minute"], row["Prediction"],
                row["1%"], row["X%"], row["2%"], row["Home Team"], row["Away Team"],
                row["Home Rank"], row["Away Rank"], row["Match URL"]
            ))
        conn.commit()
        print(f"🗃️ Inserted {len(data)} rows into MySQL database.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"❌ MySQL Error: {err}")


def run_scraper():
    start_time = time.time()
    print(f"\n🔄 Starting scraping at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        driver = setup_driver()
        html = load_full_page(driver)
        driver.quit()
        scraper = cloudscraper.create_scraper()
        data = parse_page(html, scraper)
        if data:
            filename = save_to_excel(data)
            save_to_mysql(data)
            print(f"\n✅ Scraped {len(data)} matches in {time.time() - start_time:.2f} seconds")
        else:
            print("⚠️ No data scraped")
    except Exception as e:
        print(f"\n❌ Error during scraping: {str(e)}")
    print(f"\n⏱️ Total execution time: {time.time() - start_time:.2f} seconds")


def schedule_scraper(interval_minutes: int = 60):
    print(f"\n[INFO] Scheduling scraper to run every {interval_minutes} minutes...")
    schedule.every(interval_minutes).minutes.do(run_scraper)
    run_scraper()
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule_scraper(interval_minutes=60)

