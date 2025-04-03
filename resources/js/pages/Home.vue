<template>
    <div class="min-h-screen bg-gray-50 p-4 md:p-6">
      <div class="">
       <!-- Header Section -->
<header class="mb-8">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
    <div class="flex items-center gap-3">
      <img src="https://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Tunisia.svg" alt="Tunisian Flag"
           class="h-10 w-10 rounded-full border border-gray-300" />
      <div>
        <h1 class="text-3xl md:text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-red-600 to-rose-500">
          🇹🇳 DimaRaba7
        </h1>
        <p class="text-gray-600 italic mt-1">توقعات كروية... عالطريقة التونسية ✨</p>
      </div>
    </div>

    <div class="flex gap-3">
      <button
        @click="fetchData"
        class="flex items-center gap-2 px-4 py-2 bg-white rounded-lg shadow-xs hover:shadow-sm transition-all border border-gray-200 hover:border-red-300"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
        Refresh
      </button>

      <button
        @click="showFilters = !showFilters"
        class="flex items-center gap-2 px-4 py-2 bg-white rounded-lg shadow-xs hover:shadow-sm transition-all border border-gray-200 hover:border-red-300"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
        </svg>
        {{ showFilters ? 'Hide' : 'Show' }} Filters
      </button>
    </div>
  </div>
</header>


        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
          <!-- Left Sidebar - Stats & Filters -->
          <div class="space-y-6 w-full lg:w-auto lg:col-span-1">
            <!-- Filters Card -->
            <div class="bg-white p-6 rounded-2xl shadow-md border border-gray-100 transition-all">
                <h3 class="text-lg font-semibold text-gray-800 mb-5 flex items-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.5a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.207A1 1 0 013 6.5V4z" />
        </svg>
        Match Filters
    </h3>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Date -->
        <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Date</label>
        <input
            type="date"
            v-model="dateFilter"
            class="w-full rounded-lg border-gray-200 shadow-sm focus:border-red-500 focus:ring-red-500 text-sm"
        />
        </div>

        <!-- Min Confidence -->
        <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Min Confidence</label>
        <select
            v-model="minProbability"
            class="w-full rounded-lg border-gray-200 shadow-sm focus:border-red-500 focus:ring-red-500 text-sm"
        >
            <option value="0">Any %</option>
            <option value="50">50%+</option>
            <option value="60">60%+</option>
            <option value="70">70%+</option>
            <option value="80">80%+</option>
        </select>
        </div>

        <!-- Top Teams Only -->
        <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Team Quality</label>
        <select
            v-model="topTeamsFilter"
            class="w-full rounded-lg border-gray-200 shadow-sm focus:border-red-500 focus:ring-red-500 text-sm"
        >
            <option value="false">All Teams</option>
            <option value="true">Top 3 Ranked Only</option>
        </select>
        </div>
    </div>

    <!-- Actions -->
    <div class="mt-6 flex justify-end gap-3">
        <button
        @click="resetFilters"
        class="px-4 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-100 transition"
        >
        Reset
        </button>
        <button
        @click="applyFilters"
        class="px-4 py-2 bg-red-600 rounded-lg text-sm font-medium text-white hover:bg-red-700 transition"
        >
        Apply
        </button>
    </div>
</div>



          <!-- Stats Card -->
          <div class="bg-white p-6 rounded-2xl shadow-md border border-gray-100 transition">
            <h3 class="text-lg font-semibold text-gray-800 mb-5 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                Today’s Stats
            </h3>

            <div class="space-y-3">
                <!-- Stat Row -->
                <div class="flex items-center justify-between bg-gray-50 rounded-lg px-4 py-2 hover:bg-gray-100 transition">
                <div class="flex items-center gap-2 text-sm text-gray-600">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    Total Matches
                </div>
                <span class="font-bold text-gray-800">{{ filteredMatches.length }}</span>
                </div>

                <div class="flex items-center justify-between bg-gray-50 rounded-lg px-4 py-2 hover:bg-gray-100 transition">
                <div class="flex items-center gap-2 text-sm text-gray-600">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m0-4h.01M12 20h.01" />
                    </svg>
                    High Confidence
                </div>
                <span class="font-bold text-gray-800">
                    {{ highConfidenceMatchesCount }} ({{ highConfidencePercentage }}%)
                </span>
                </div>

                <div class="flex items-center justify-between bg-gray-50 rounded-lg px-4 py-2 hover:bg-gray-100 transition">
                <div class="flex items-center gap-2 text-sm text-gray-600">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M11 11V9a4 4 0 118 0v2m-3 4h.01M6 13h.01M6 17h.01M6 9h.01" />
                    </svg>
                    Top Team Matches
                </div>
                <span class="font-bold text-gray-800">{{ topTeamMatchesCount }}</span>
                </div>

                <div class="flex items-center justify-between bg-gray-50 rounded-lg px-4 py-2 hover:bg-gray-100 transition">
                <div class="flex items-center gap-2 text-sm text-gray-600">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M11 11V9a4 4 0 118 0v2m-3 4h.01M6 13h.01M6 17h.01M6 9h.01" />
                    </svg>
                    Avg. Confidence
                </div>
                <span class="font-bold text-gray-800">{{ averageConfidence }}%</span>
                </div>
            </div>
            </div>


           <!-- Must-Watch Matches -->
            <!-- Top 5 Must-Watch Match Schedule -->
            <div v-if="mustWatchMatches.length" class="bg-white border border-gray-100 rounded-2xl shadow-sm mt-6 overflow-hidden">
            <div class="bg-yellow-50 border-b border-yellow-100 px-6 py-4">
                <h2 class="text-lg font-bold text-yellow-800 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M13 16h-1v-4h-1m0-4h.01M12 20h.01M9 12h.01M15 12h.01M12 8v.01" />
                </svg>
                Must-Watch Matches Today
                </h2>
            </div>

            <div class="divide-y divide-gray-100">
                <div
                v-for="match in mustWatchMatches"
                :key="match.id"
                class="grid grid-cols-1 sm:grid-cols-12 gap-4 items-center px-6 py-3 hover:bg-gray-50 transition"
                >
                <!-- Time -->
                <div class="col-span-2 text-sm text-gray-500 font-medium">
                    {{ match.time_str }}
                </div>

                <!-- Teams + Ranks -->
                <div class="col-span-6 flex flex-col sm:flex-row sm:items-center sm:gap-2 text-sm text-gray-800 font-semibold">
                    <span>{{ match.home_team }} <span class="text-gray-400 font-normal text-xs">(#{{ match.home_rank }})</span></span>
                    <span class="text-gray-500 font-normal hidden sm:inline">vs</span>
                    <span>{{ match.away_team }} <span class="text-gray-400 font-normal text-xs">(#{{ match.away_rank }})</span></span>
                </div>

                <!-- Prediction -->
                <div class="col-span-2 text-sm text-gray-700 font-medium">
            {{ match.prediction }} →
            {{
                match.prediction === '1' ? 'Home Win' :
                match.prediction === 'X' ? 'Draw' :
                match.prediction === '2' ? 'Away Win' :
                'Unknown'
            }}
            </div>


                <!-- Hot Pick + Action -->
                <div class="col-span-2 flex items-center justify-between sm:justify-end gap-2">
                    <span
                    v-if="getHighestProbability(match) > 60"
                    class="text-xs bg-yellow-100 text-yellow-800 font-semibold px-2 py-0.5 rounded-full"
                    >
                    🔥 Hot Pick
                    </span>
                    <a
                    :href="match.match_url"
                    target="_blank"
                    class="text-sm text-blue-600 hover:underline"
                    >
                    View →
                    </a>
                </div>
                </div>
            </div>
            </div>


          </div>

          <!-- Main Content Area -->
          <div class="lg:col-span-3 space-y-6">


            <!-- Modern Best Bets Hero Section -->
<div v-if="bestBets.length > 0" class="relative bg-gradient-to-tr from-[#f9fafb] to-[#eef4ff] p-8 rounded-3xl border border-blue-200 shadow-md">
  <!-- Header -->
  <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-6 gap-4">
    <div class="flex items-center gap-3">
      <img src="https://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Tunisia.svg" alt="Tunisia Flag" class="w-6 h-6 rounded-full border border-gray-300">
      <h2 class="text-2xl font-extrabold text-blue-900 flex items-center gap-2">
        🔒 Verified Best Bets
      </h2>
      <span class="text-xs bg-green-100 text-green-700 font-medium px-2 py-0.5 rounded-full">
        Certified 🇹🇳 by DimaRaba7 AI
      </span>
    </div>

    <div class="flex items-center gap-2 text-sm text-gray-600">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M9 12l2 2l4 -4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      Trusted by thousands of punters daily
    </div>
  </div>

  <!-- Bets Horizontal Scroll -->
  <div class="overflow-x-auto scrollbar-hide -mx-2">
    <div class="flex gap-4 px-2">
      <div
        v-for="match in bestBets"
        :key="match.id"
        class="min-w-[320px] bg-white rounded-xl border border-gray-200 p-4 shadow-sm hover:shadow-md transition-all"
      >
        <!-- Match Info -->
        <div class="flex justify-between items-start mb-2">
          <div>
            <h3 class="font-semibold text-gray-800 text-sm">{{ match.game }}</h3>
            <p class="text-xs text-gray-400">{{ match.league }}</p>
          </div>
          <span class="text-xs bg-green-100 text-green-800 px-2 py-0.5 rounded-full font-medium">
            {{ getHighestProbability(match) }}%
          </span>
        </div>

        <!-- Teams + Prediction -->
        <div class="flex justify-between items-center mb-3">
          <div class="text-center">
            <div class="font-bold text-gray-800">{{ match.home_team }}</div>
            <div class="text-xs text-gray-400">#{{ match.home_rank }}</div>
          </div>
          <div class="bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full text-xs font-bold">
            {{ match.prediction === '1' ? 'Home Win' : match.prediction === 'X' ? 'Draw' : 'Away Win' }}
          </div>
          <div class="text-center">
            <div class="font-bold text-gray-800">{{ match.away_team }}</div>
            <div class="text-xs text-gray-400">#{{ match.away_rank }}</div>
          </div>
        </div>

        <!-- Confidence Bars -->
        <div class="space-y-2 text-xs">
          <div class="flex items-center gap-2">
            <span class="w-4">1</span>
            <div class="flex-1 bg-gray-200 h-2 rounded-full overflow-hidden">
              <div class="h-full bg-green-500" :style="{ width: match.prob_1 + '%' }"></div>
            </div>
            <span>{{ match.prob_1 }}%</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-4">X</span>
            <div class="flex-1 bg-gray-200 h-2 rounded-full overflow-hidden">
              <div class="h-full bg-yellow-400" :style="{ width: match.prob_x + '%' }"></div>
            </div>
            <span>{{ match.prob_x }}%</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-4">2</span>
            <div class="flex-1 bg-gray-200 h-2 rounded-full overflow-hidden">
              <div class="h-full bg-red-400" :style="{ width: match.prob_2 + '%' }"></div>
            </div>
            <span>{{ match.prob_2 }}%</span>
          </div>
        </div>

        <!-- CTA -->
        <div class="mt-4 text-center">
          <a
            :href="match.match_url"
            target="_blank"
            class="text-sm text-blue-600 font-medium hover:underline"
          >
            View Analysis →
          </a>
        </div>
      </div>
    </div>
  </div>
</div>





            <!-- Loading State -->
            <div v-if="loading" class="flex justify-center items-center py-20">
              <div class="animate-pulse flex flex-col items-center gap-4">
                <div class="h-12 w-12 bg-blue-200 rounded-full"></div>
                <p class="text-gray-500">Loading predictions...</p>
              </div>
            </div>

            <!-- Error State -->
            <div v-else-if="error" class="bg-red-50 border-l-4 border-red-500 p-4 rounded-lg">
              <div class="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <p class="text-red-700 font-medium">{{ error }}</p>
              </div>
            </div>

            <!-- Empty State -->
            <div v-else-if="filteredMatches.length === 0" class="text-center py-20">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <p class="text-gray-500 mt-4 text-lg">No matches found with current filters</p>
              <button
                @click="resetFilters"
                class="mt-4 px-4 py-2 bg-blue-600 rounded-lg text-sm font-medium text-white hover:bg-blue-700"
              >
                Reset Filters
              </button>
            </div>

<!-- Regular Matches Grid (Modern, No Scores) -->
<div v-else>
  <!-- Header -->
  <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
    <h2 class="text-xl font-bold text-red-700 flex items-center gap-2">
      🇹🇳 {{ dateFilter ? `Matches on ${formatDate(dateFilter)}` : 'All Upcoming Matches' }}
      <span class="text-sm font-normal text-gray-500 ml-2">({{ filteredMatches.length }} matches)</span>
    </h2>

    <!-- Sort -->
    <div class="flex items-center gap-2">
      <span class="text-sm text-gray-500">Sort:</span>
      <select
        v-model="sortOption"
        @change="applySorting"
        class="rounded-md border border-gray-300 text-sm py-1 px-2 focus:outline-none focus:ring-1 focus:ring-red-500 focus:border-red-500"
      >
        <option value="highest-prob">Highest Probability</option>
        <option value="time">Match Time</option>
        <option value="league">League</option>
      </select>
    </div>
  </div>

  <!-- Match Cards -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
    <div
      v-for="match in filteredMatches"
      :key="match.id"
      class="bg-white border border-gray-200 rounded-2xl shadow-sm hover:shadow-md transition-all duration-300 overflow-hidden"
      :class="{ 'border-red-400': isTopRanked(match.home_rank) || isTopRanked(match.away_rank) }"
    >
      <div class="p-5 space-y-4">

        <!-- Match Info -->
        <div class="flex justify-between items-center">
          <div class="text-left">
            <h3 class="font-semibold text-gray-800 text-sm truncate">{{ match.game }}</h3>
            <p class="text-xs text-gray-400">{{ match.league }}</p>
          </div>
          <span class="text-xs bg-red-100 text-red-700 px-2 py-0.5 rounded-full font-medium">
            {{ match.time_str }}
          </span>
        </div>

        <!-- Teams & Prediction -->
        <div class="flex items-center justify-between text-sm">
          <div class="text-left">
            <div class="font-bold text-gray-900">{{ match.home_team }}</div>
            <div v-if="match.home_rank" class="text-xs text-gray-400">#{{ match.home_rank }}</div>
          </div>

          <div class="bg-red-100 text-red-700 px-3 py-1 rounded-full text-xs font-semibold whitespace-nowrap">
            {{ match.prediction === '1' ? 'Home Win' : match.prediction === 'X' ? 'Draw' : 'Away Win' }}
          </div>

          <div class="text-right">
            <div class="font-bold text-gray-900">{{ match.away_team }}</div>
            <div v-if="match.away_rank" class="text-xs text-gray-400">#{{ match.away_rank }}</div>
          </div>
        </div>

        <!-- Confidence Bars -->
        <div class="space-y-2 text-xs">
          <div class="flex items-center gap-2">
            <span class="w-5 font-medium text-gray-600">1</span>
            <div class="flex-1 h-2 rounded-full bg-gray-200 overflow-hidden">
              <div class="h-full bg-green-500" :style="{ width: `${match.prob_1}%` }"></div>
            </div>
            <span :class="{ 'text-green-700 font-bold': match.prob_1 > 60 }">{{ match.prob_1 }}%</span>
          </div>

          <div class="flex items-center gap-2">
            <span class="w-5 font-medium text-gray-600">X</span>
            <div class="flex-1 h-2 rounded-full bg-gray-200 overflow-hidden">
              <div class="h-full bg-yellow-400" :style="{ width: `${match.prob_x}%` }"></div>
            </div>
            <span :class="{ 'text-yellow-700 font-bold': match.prob_x > 60 }">{{ match.prob_x }}%</span>
          </div>

          <div class="flex items-center gap-2">
            <span class="w-5 font-medium text-gray-600">2</span>
            <div class="flex-1 h-2 rounded-full bg-gray-200 overflow-hidden">
              <div class="h-full bg-red-400" :style="{ width: `${match.prob_2}%` }"></div>
            </div>
            <span :class="{ 'text-red-700 font-bold': match.prob_2 > 60 }">{{ match.prob_2 }}%</span>
          </div>
        </div>
      </div>

      <!-- View Button -->
      <a
        :href="match.match_url"
        target="_blank"
        class="block bg-red-50 hover:bg-red-100 py-2 text-center text-xs font-medium text-red-700 transition"
      >
        View Match Details →
      </a>
    </div>
  </div>
</div>


          </div>
        </div>
      </div>
    </div>
  </template>
<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

// 🔄 State
const matches = ref([])
const loading = ref(true)
const error = ref(null)
const showFilters = ref(false)

// 🔍 Filters
const dateFilter = ref('')
const minProbability = ref('0')
const leagueFilter = ref('')
const topTeamsFilter = ref('false')
const sortOption = ref('highest-prob')

// 🎯 Sample Matches (Today-based ISO dates)
const todayISO = new Date().toISOString().split('T')[0]

const sampleMatches = [
  {
    id: '1',
    game: 'Premier League - Arsenal vs Chelsea',
    league: 'Premier League',
    home_team: 'Arsenal',
    away_team: 'Chelsea',
    prob_1: 65,
    prob_x: 20,
    prob_2: 15,
    prediction: '1',
    home_rank: 1,
    away_rank: 4,
    time_str: '20:00',
    iso_time: `${todayISO}T20:00:00Z`,
    match_url: '#'
  },
  {
    id: '2',
    game: 'La Liga - Barcelona vs Real Madrid',
    league: 'La Liga',
    home_team: 'Barcelona',
    away_team: 'Real Madrid',
    prob_1: 40,
    prob_x: 30,
    prob_2: 30,
    prediction: 'X',
    home_rank: 2,
    away_rank: 1,
    time_str: '21:00',
    iso_time: `${todayISO}T21:00:00Z`,
    match_url: '#'
  },
  {
    id: '3',
    game: 'Ligue 1 - PSG vs Marseille',
    league: 'Ligue 1',
    home_team: 'PSG',
    away_team: 'Marseille',
    prob_1: 75,
    prob_x: 15,
    prob_2: 10,
    prediction: '1',
    home_rank: 1,
    away_rank: 5,
    time_str: '19:45',
    iso_time: `${todayISO}T19:45:00Z`,
    match_url: '#'
  }
]

// 🧠 Utils
const isTopRanked = (rank) => rank && [1, 2, 3].includes(Number(rank))

const getHighestProbability = (match) =>
  Math.max(match.prob_1, match.prob_x, match.prob_2)

const formatDate = (dateString) => {
  return new Intl.DateTimeFormat('fr-TN', {
    weekday: 'long',
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  }).format(new Date(dateString))
}

const isSameDay = (a, b) =>
  a.getFullYear() === b.getFullYear() &&
  a.getMonth() === b.getMonth() &&
  a.getDate() === b.getDate()

// 📊 Stats
const highConfidenceMatchesCount = computed(() =>
  filteredMatches.value.filter(
    m => m.prob_1 >= 70 || m.prob_x >= 70 || m.prob_2 >= 70
  ).length
)

const highConfidencePercentage = computed(() => {
  if (filteredMatches.value.length === 0) return 0
  return Math.round((highConfidenceMatchesCount.value / filteredMatches.value.length) * 100)
})

const topTeamMatchesCount = computed(() =>
  filteredMatches.value.filter(
    m => isTopRanked(m.home_rank) || isTopRanked(m.away_rank)
  ).length
)

const averageConfidence = computed(() => {
  if (filteredMatches.value.length === 0) return 0
  const total = filteredMatches.value.reduce((sum, m) =>
    sum + getHighestProbability(m), 0)
  return Math.round(total / filteredMatches.value.length)
})

// 🔍 Filtered Matches
const filteredMatches = computed(() => {
  let result = [...matches.value]

  if (dateFilter.value) {
    const selected = new Date(dateFilter.value)
    result = result.filter(m => isSameDay(new Date(m.iso_time), selected))
  }

  if (minProbability.value > 0) {
    const minProb = Number(minProbability.value)
    result = result.filter(m =>
      m.prob_1 >= minProb || m.prob_x >= minProb || m.prob_2 >= minProb
    )
  }

  if (leagueFilter.value) {
    result = result.filter(m => m.league === leagueFilter.value)
  }

  if (topTeamsFilter.value === 'true') {
    result = result.filter(m =>
      isTopRanked(m.home_rank) || isTopRanked(m.away_rank)
    )
  }

  // Sorting
  if (sortOption.value === 'highest-prob') {
    result.sort((a, b) => getHighestProbability(b) - getHighestProbability(a))
  } else if (sortOption.value === 'time') {
    result.sort((a, b) => new Date(a.iso_time) - new Date(b.iso_time))
  } else if (sortOption.value === 'league') {
    result.sort((a, b) => a.league.localeCompare(b.league))
  }

  return result
})

// 🌟 Best Bets
const bestBets = computed(() =>
  filteredMatches.value
    .filter(m => getHighestProbability(m) > 70)
    .sort((a, b) => getHighestProbability(b) - getHighestProbability(a))
    .slice(0, 3)
)

// 🔥 Must-Watch Matches (Top 4 vs Low rank 10+)
const mustWatchMatches = computed(() =>
  filteredMatches.value
    .filter(m => {
      const home = Number(m.home_rank)
      const away = Number(m.away_rank)
      const top4 = [1, 2, 3, 4]
      return (top4.includes(home) && away >= 10) || (top4.includes(away) && home >= 10)
    })
    .sort((a, b) => getHighestProbability(b) - getHighestProbability(a))
    .slice(0, 5)
)

// 🧹 Filters actions
const applyFilters = () => (showFilters.value = false)

const resetFilters = () => {
  dateFilter.value = ''
  minProbability.value = '0'
  leagueFilter.value = ''
  topTeamsFilter.value = 'false'
  sortOption.value = 'highest-prob'
}

// 🌐 Load Matches
const fetchData = async () => {
  loading.value = true
  error.value = null
  try {
    const res = await axios.get('/forebet-data')
    matches.value = res.data.map(match => ({
      ...match,
      league: match.game.split(' - ')[0] || match.league
    }))
  } catch (err) {
    console.warn('API failed, using sample data')
    matches.value = sampleMatches.map(match => ({
      ...match,
      league: match.game.split(' - ')[0] || match.league
    }))
    error.value = '⚠️ Using sample data - API unavailable'
  } finally {
    loading.value = false
  }
}

// 🚀 On Mount
onMounted(() => {
  fetchData()
})
</script>


  <style>
  /* Custom scrollbar */
  ::-webkit-scrollbar {
    width: 8px;
    height: 8px;
  }
  ::-webkit-scrollbar-track {
    background: #f1f1f1;
  }
  ::-webkit-scrollbar-thumb {
    background: #c1c1c1;
    border-radius: 4px;
  }
  ::-webkit-scrollbar-thumb:hover {
    background: #a1a1a1;
  }

  /* Smooth transitions */
  * {
    transition: background-color 0.2s ease, border-color 0.2s ease;
  }

  /* Better focus states */
  button:focus, select:focus, input:focus {
    outline: none;
    ring: 2px;
    ring-opacity: 50%;
    ring-color: #3b82f6;
  }

  /* Match card hover effect */
  .bg-white:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  }

  /* Responsive adjustments */
  @media (max-width: 768px) {
    .grid-cols-1 {
      grid-template-columns: 1fr;
    }
    .lg\:col-span-1, .lg\:col-span-3 {
      grid-column: span 1;
    }
  }
  @media (max-width: 768px) {
  .filters-sticky {
    position: sticky;
    top: 0;
    z-index: 10;
    background-color: white;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    padding-top: 1rem;
  }
}

  </style>
