<template>
    <div class="min-h-screen bg-gray-50 p-4 md:p-6">
      <div class="">
        <!-- Header Section -->
        <header class="mb-8">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <h1 class="text-3xl md:text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-500">
                ⚽ Forebet Pro+
              </h1>
              <p class="text-gray-500 mt-1">AI-powered football predictions & analytics</p>
            </div>
            <div class="flex gap-3">
              <button
                @click="fetchData"
                class="flex items-center gap-2 px-4 py-2 bg-white rounded-lg shadow-xs hover:shadow-sm transition-all border border-gray-200 hover:border-blue-300"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
                Refresh
              </button>
              <button
                @click="showFilters = !showFilters"
                class="flex items-center gap-2 px-4 py-2 bg-white rounded-lg shadow-xs hover:shadow-sm transition-all border border-gray-200 hover:border-blue-300"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
                </svg>
                {{ showFilters ? 'Hide' : 'Show' }} Filters
              </button>
            </div>
          </div>
        </header>

        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
          <!-- Left Sidebar - Stats & Filters -->
          <div class="lg:col-span-1 space-y-6">
            <!-- Filters Card -->
            <div v-if="showFilters" class="bg-white p-5 rounded-xl shadow-xs border border-gray-200">
              <h3 class="font-medium text-gray-800 mb-4 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                </svg>
                Filter Matches
              </h3>
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Date</label>
                  <input
                    type="date"
                    v-model="dateFilter"
                    class="w-full rounded-lg border-gray-200 shadow-sm focus:border-blue-500 focus:ring-blue-500 text-sm"
                  >
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Time of Day</label>
                  <select v-model="timeFilter" class="w-full rounded-lg border-gray-200 shadow-sm focus:border-blue-500 focus:ring-blue-500 text-sm">
                    <option value="">All Day</option>
                    <option value="morning">Morning (00:00-11:59)</option>
                    <option value="afternoon">Afternoon (12:00-17:59)</option>
                    <option value="evening">Evening (18:00-23:59)</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Min Confidence</label>
                  <select v-model="minProbability" class="w-full rounded-lg border-gray-200 shadow-sm focus:border-blue-500 focus:ring-blue-500 text-sm">
                    <option value="0">Any %</option>
                    <option value="50">50%+</option>
                    <option value="60">60%+</option>
                    <option value="70">70%+</option>
                    <option value="80">80%+</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">League</label>
                  <select v-model="leagueFilter" class="w-full rounded-lg border-gray-200 shadow-sm focus:border-blue-500 focus:ring-blue-500 text-sm">
                    <option value="">All Leagues</option>
                    <option v-for="league in availableLeagues" :value="league">{{ league }}</option>
                  </select>
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">Team Quality</label>
                  <select v-model="topTeamsFilter" class="w-full rounded-lg border-gray-200 shadow-sm focus:border-blue-500 focus:ring-blue-500 text-sm">
                    <option value="false">All Teams</option>
                    <option value="true">Top 3 Ranked Only</option>
                  </select>
                </div>
              </div>
              <div class="mt-6 flex justify-end gap-3">
                <button
                  @click="resetFilters"
                  class="px-4 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50"
                >
                  Reset
                </button>
                <button
                  @click="applyFilters"
                  class="px-4 py-2 bg-blue-600 rounded-lg text-sm font-medium text-white hover:bg-blue-700"
                >
                  Apply
                </button>
              </div>
            </div>

            <!-- Stats Card -->
            <div class="bg-white p-5 rounded-xl shadow-xs border border-gray-200">
              <h3 class="font-medium text-gray-800 mb-4 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                Today's Stats
              </h3>
              <div class="space-y-4">
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">Total Matches</span>
                  <span class="font-medium">{{ filteredMatches.length }}</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">High Confidence</span>
                  <span class="font-medium">{{ highConfidenceMatchesCount }} ({{ highConfidencePercentage }}%)</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">Top Team Matches</span>
                  <span class="font-medium">{{ topTeamMatchesCount }}</span>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-sm text-gray-600">Avg. Confidence</span>
                  <span class="font-medium">{{ averageConfidence }}%</span>
                </div>
              </div>
            </div>

            <!-- Leagues Card -->
            <div class="bg-white p-5 rounded-xl shadow-xs border border-gray-200">
              <h3 class="font-medium text-gray-800 mb-4 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                Top Leagues
              </h3>
              <div class="space-y-3">
                <div
                  v-for="league in topLeagues"
                  :key="league.name"
                  class="flex items-center justify-between cursor-pointer hover:bg-gray-50 p-2 rounded-lg"
                  @click="leagueFilter = league.name; applyFilters()"
                >
                  <span class="text-sm font-medium">{{ league.name }}</span>
                  <span class="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded-full">{{ league.count }} matches</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Main Content Area -->
          <div class="lg:col-span-3 space-y-6">
            <!-- Best Bets Section -->
            <div v-if="bestBets.length > 0" class="bg-gradient-to-r from-blue-50 to-indigo-50 p-5 rounded-xl border border-blue-100">
              <div class="flex items-center justify-between mb-4">
                <h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                  </svg>
                  Best Bets of the Day
                </h2>
                <span class="text-sm bg-white px-3 py-1 rounded-full text-blue-600 font-medium">
                  {{ bestBets.length }} high confidence picks
                </span>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div
                  v-for="match in bestBets"
                  :key="'best-'+match.id"
                  class="bg-white rounded-xl shadow-sm hover:shadow-md transition-all duration-300 overflow-hidden border-2 border-green-200"
                >
                  <div class="p-4">
                    <div class="flex justify-between items-start mb-2">
                      <div>
                        <h3 class="font-bold text-gray-800 line-clamp-1">{{ match.game }}</h3>
                        <p class="text-xs text-gray-400 mt-1">{{ match.league }}</p>
                      </div>
                      <span class="bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full font-medium">
                        {{ getHighestProbability(match) }}% Confidence
                      </span>
                    </div>

                    <div class="flex items-center justify-between my-3">
                      <div class="text-center">
                        <div class="font-bold text-gray-800">{{ match.home_team }}</div>
                        <div v-if="match.home_rank" class="text-xs mt-1" :class="{
                          'text-yellow-600 font-bold': isTopRanked(match.home_rank),
                          'text-gray-400': !isTopRanked(match.home_rank)
                        }">
                          Rank {{ match.home_rank }}
                        </div>
                      </div>

                      <div class="flex flex-col items-center mx-1">
                        <div class="text-xs text-gray-500 mb-1">VS</div>
                        <div class="bg-green-100 text-green-800 px-2 py-0.5 rounded-full text-xs font-bold">
                          {{ getPredictionType(match) }}
                        </div>
                      </div>

                      <div class="text-center">
                        <div class="font-bold text-gray-800">{{ match.away_team }}</div>
                        <div v-if="match.away_rank" class="text-xs mt-1" :class="{
                          'text-yellow-600 font-bold': isTopRanked(match.away_rank),
                          'text-gray-400': !isTopRanked(match.away_rank)
                        }">
                          Rank {{ match.away_rank }}
                        </div>
                      </div>
                    </div>

                    <div class="mt-3">
                      <div class="flex justify-between items-center text-xs">
                        <div class="text-center flex-1">
                          <div class="font-bold">1</div>
                          <div class="h-2 w-full bg-gray-200 rounded-full mt-1 overflow-hidden">
                            <div
                              class="h-full"
                              :class="{'bg-green-500': match.prob_1 > 60, 'bg-green-300': match.prob_1 <= 60}"
                              :style="{ width: `${match.prob_1}%` }"
                            ></div>
                          </div>
                          <div class="mt-1 text-xs" :class="{'text-green-600 font-bold': match.prob_1 > 60}">
                            {{ match.prob_1 }}%
                          </div>
                        </div>
                        <div class="text-center flex-1 px-1">
                          <div class="font-bold">X</div>
                          <div class="h-2 w-full bg-gray-200 rounded-full mt-1 overflow-hidden">
                            <div
                              class="h-full"
                              :class="{'bg-green-500': match.prob_x > 60, 'bg-yellow-300': match.prob_x <= 60}"
                              :style="{ width: `${match.prob_x}%` }"
                            ></div>
                          </div>
                          <div class="mt-1 text-xs" :class="{'text-green-600 font-bold': match.prob_x > 60}">
                            {{ match.prob_x }}%
                          </div>
                        </div>
                        <div class="text-center flex-1">
                          <div class="font-bold">2</div>
                          <div class="h-2 w-full bg-gray-200 rounded-full mt-1 overflow-hidden">
                            <div
                              class="h-full"
                              :class="{'bg-green-500': match.prob_2 > 60, 'bg-red-300': match.prob_2 <= 60}"
                              :style="{ width: `${match.prob_2}%` }"
                            ></div>
                          </div>
                          <div class="mt-1 text-xs" :class="{'text-green-600 font-bold': match.prob_2 > 60}">
                            {{ match.prob_2 }}%
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <a
                    :href="match.match_url"
                    target="_blank"
                    class="block text-center bg-green-50 hover:bg-green-100 py-2 text-xs font-medium text-green-700 transition-colors"
                  >
                    View detailed analysis →
                  </a>
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

            <!-- Regular Matches Grid -->
            <div v-else>
              <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4">
                <h2 class="text-xl font-bold text-gray-800">
                  {{ dateFilter ? `Matches on ${formatDate(dateFilter)}` : 'All Upcoming Matches' }}
                  <span class="text-sm font-normal text-gray-500 ml-2">({{ filteredMatches.length }} matches)</span>
                </h2>
                <div class="flex items-center gap-2">
                  <span class="text-sm text-gray-500">Sort:</span>
                  <select
                    v-model="sortOption"
                    @change="applySorting"
                    class="rounded-lg border-gray-200 shadow-sm focus:border-blue-500 focus:ring-blue-500 text-sm"
                  >
                    <option value="highest-prob">Highest Probability</option>
                    <option value="time">Match Time</option>
                    <option value="league">League</option>
                  </select>
                </div>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <div
                  v-for="match in filteredMatches"
                  :key="match.id"
                  class="bg-white rounded-xl shadow-xs hover:shadow-sm transition-all duration-300 overflow-hidden border border-gray-200"
                  :class="{
                    'border-yellow-300 border-2': isTopRanked(match.home_rank) || isTopRanked(match.away_rank)
                  }"
                >
                  <div class="p-4">
                    <div class="flex justify-between items-start mb-2">
                      <div>
                        <h3 class="font-bold text-gray-800 line-clamp-1">{{ match.game }}</h3>
                        <p class="text-xs text-gray-400 mt-1">{{ match.league }}</p>
                      </div>
                      <span class="bg-blue-50 text-blue-600 text-xs px-2 py-1 rounded-full">{{ match.time_str }}</span>
                    </div>

                    <div class="flex items-center justify-between my-3">
                      <div class="text-center">
                        <div class="font-bold text-gray-800">{{ match.home_team }}</div>
                        <div v-if="match.home_rank" class="text-xs mt-1" :class="{
                          'text-yellow-600 font-bold': isTopRanked(match.home_rank),
                          'text-gray-400': !isTopRanked(match.home_rank)
                        }">
                          Rank {{ match.home_rank }}
                        </div>
                      </div>

                      <div class="flex flex-col items-center mx-1">
                        <div class="text-xs text-gray-500 mb-1">VS</div>
                        <div class="bg-indigo-100 text-indigo-700 px-2 py-0.5 rounded text-xs font-bold">
                          {{ match.prediction }}
                        </div>
                      </div>

                      <div class="text-center">
                        <div class="font-bold text-gray-800">{{ match.away_team }}</div>
                        <div v-if="match.away_rank" class="text-xs mt-1" :class="{
                          'text-yellow-600 font-bold': isTopRanked(match.away_rank),
                          'text-gray-400': !isTopRanked(match.away_rank)
                        }">
                          Rank {{ match.away_rank }}
                        </div>
                      </div>
                    </div>

                    <div class="bg-gray-50 rounded-lg p-3 mt-3">
                      <div class="flex justify-between items-center text-xs">
                        <div class="text-center">
                          <div class="font-bold">1</div>
                          <div class="h-2 w-12 bg-gray-200 rounded-full mt-1 overflow-hidden">
                            <div
                              class="h-full"
                              :class="{'bg-green-500': match.prob_1 > 60, 'bg-green-300': match.prob_1 <= 60}"
                              :style="{ width: `${match.prob_1}%` }"
                            ></div>
                          </div>
                          <div class="mt-1 text-xs" :class="{'text-green-600 font-bold': match.prob_1 > 60}">
                            {{ match.prob_1 }}%
                          </div>
                        </div>
                        <div class="text-center">
                          <div class="font-bold">X</div>
                          <div class="h-2 w-12 bg-gray-200 rounded-full mt-1 overflow-hidden">
                            <div
                              class="h-full"
                              :class="{'bg-green-500': match.prob_x > 60, 'bg-yellow-300': match.prob_x <= 60}"
                              :style="{ width: `${match.prob_x}%` }"
                            ></div>
                          </div>
                          <div class="mt-1 text-xs" :class="{'text-green-600 font-bold': match.prob_x > 60}">
                            {{ match.prob_x }}%
                          </div>
                        </div>
                        <div class="text-center">
                          <div class="font-bold">2</div>
                          <div class="h-2 w-12 bg-gray-200 rounded-full mt-1 overflow-hidden">
                            <div
                              class="h-full"
                              :class="{'bg-green-500': match.prob_2 > 60, 'bg-red-300': match.prob_2 <= 60}"
                              :style="{ width: `${match.prob_2}%` }"
                            ></div>
                          </div>
                          <div class="mt-1 text-xs" :class="{'text-green-600 font-bold': match.prob_2 > 60}">
                            {{ match.prob_2 }}%
                          </div>
                        </div>
                      </div>
                    </div>

                    <div v-if="match.score || match.half_time_score" class="mt-3 flex justify-center gap-3">
                      <div v-if="match.score" class="text-xs bg-blue-50 text-blue-700 px-2 py-1 rounded-full">
                        FT: {{ match.score }}
                      </div>
                      <div v-if="match.half_time_score" class="text-xs bg-purple-50 text-purple-700 px-2 py-1 rounded-full">
                        HT: {{ match.half_time_score }}
                      </div>
                    </div>
                  </div>

                  <a
                    :href="match.match_url"
                    target="_blank"
                    class="block text-center bg-gray-50 hover:bg-gray-100 py-2 text-xs font-medium text-blue-600 transition-colors"
                  >
                    View match details →
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

  // State
  const matches = ref([])
  const loading = ref(true)
  const error = ref(null)
  const showFilters = ref(false)

  // Filters
  const dateFilter = ref('')
  const minProbability = ref('0')
  const leagueFilter = ref('')
  const topTeamsFilter = ref('false')
  const sortOption = ref('highest-prob')
  const timeFilter = ref('')

  // Sample data to ensure matches show up
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
      iso_time: new Date().toISOString(),
      match_url: '#',
      score: '2-0',
      half_time_score: '1-0'
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
      iso_time: new Date().toISOString(),
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
      iso_time: new Date().toISOString(),
      match_url: '#'
    },
    {
      id: '4',
      game: 'Bundesliga - Bayern vs Dortmund',
      league: 'Bundesliga',
      home_team: 'Bayern Munich',
      away_team: 'Dortmund',
      prob_1: 60,
      prob_x: 25,
      prob_2: 15,
      prediction: '1',
      home_rank: 1,
      away_rank: 2,
      time_str: '18:30',
      iso_time: new Date().toISOString(),
      match_url: '#'
    },
    {
      id: '5',
      game: 'Serie A - Juventus vs Milan',
      league: 'Serie A',
      home_team: 'Juventus',
      away_team: 'AC Milan',
      prob_1: 45,
      prob_x: 30,
      prob_2: 25,
      prediction: '1',
      home_rank: 3,
      away_rank: 2,
      time_str: '20:45',
      iso_time: new Date().toISOString(),
      match_url: '#'
    }
  ]

  // Computed: Leagues
  const availableLeagues = computed(() => {
    const leagues = new Set()
    matches.value.forEach(match => {
      if (match.league) leagues.add(match.league)
    })
    return Array.from(leagues).sort()
  })

  // Computed: Top Leagues (for sidebar)
  const topLeagues = computed(() => {
    const leagueCounts = {}

    matches.value.forEach(match => {
      if (!leagueCounts[match.league]) {
        leagueCounts[match.league] = 0
      }
      leagueCounts[match.league]++
    })

    return Object.entries(leagueCounts)
      .map(([name, count]) => ({ name, count }))
      .sort((a, b) => b.count - a.count)
      .slice(0, 5)
  })

  // Computed: Stats
  const highConfidenceMatchesCount = computed(() => {
    return filteredMatches.value.filter(match =>
      match.prob_1 >= 70 || match.prob_x >= 70 || match.prob_2 >= 70
    ).length
  })

  const highConfidencePercentage = computed(() => {
    if (filteredMatches.value.length === 0) return 0
    return Math.round((highConfidenceMatchesCount.value / filteredMatches.value.length) * 100)
  })

  const topTeamMatchesCount = computed(() => {
    return filteredMatches.value.filter(match =>
      isTopRanked(match.home_rank) || isTopRanked(match.away_rank)
    ).length
  })

  const averageConfidence = computed(() => {
    if (filteredMatches.value.length === 0) return 0

    const total = filteredMatches.value.reduce((sum, match) => {
      return sum + Math.max(match.prob_1, match.prob_x, match.prob_2)
    }, 0)

    return Math.round(total / filteredMatches.value.length)
  })

  // Computed: Filtered Matches
  const filteredMatches = computed(() => {
    let result = [...matches.value]

    // Date filter (local, not UTC)
    if (dateFilter.value) {
      const selectedDate = new Date(dateFilter.value)
      result = result.filter(match => {
        const matchDate = new Date(match.iso_time)
        return (
          matchDate.getFullYear() === selectedDate.getFullYear() &&
          matchDate.getMonth() === selectedDate.getMonth() &&
          matchDate.getDate() === selectedDate.getDate()
        )
      })
    }

    // Time of Day filter
    if (timeFilter.value) {
      result = result.filter(match => {
        if (!match.time_str) return false
        const [hours] = match.time_str.split(':').map(Number)
        if (timeFilter.value === 'morning') return hours >= 0 && hours < 12
        if (timeFilter.value === 'afternoon') return hours >= 12 && hours < 18
        if (timeFilter.value === 'evening') return hours >= 18 && hours <= 23
        return true
      })
    }

    // Min probability filter
    if (minProbability.value > 0) {
      const minProb = Number(minProbability.value)
      result = result.filter(match =>
        match.prob_1 >= minProb ||
        match.prob_x >= minProb ||
        match.prob_2 >= minProb
      )
    }

    // League filter
    if (leagueFilter.value) {
      result = result.filter(match => match.league === leagueFilter.value)
    }

    // Top teams filter
    if (topTeamsFilter.value === 'true') {
      result = result.filter(match =>
        isTopRanked(match.home_rank) || isTopRanked(match.away_rank)
      )
    }

    // Apply sorting
    if (sortOption.value === 'highest-prob') {
      result.sort((a, b) => {
        const aMax = Math.max(a.prob_1, a.prob_x, a.prob_2)
        const bMax = Math.max(b.prob_1, b.prob_x, b.prob_2)
        return bMax - aMax
      })
    } else if (sortOption.value === 'time') {
      result.sort((a, b) => new Date(a.iso_time) - new Date(b.iso_time))
    } else if (sortOption.value === 'league') {
      result.sort((a, b) => a.league.localeCompare(b.league))
    }

    return result
  })

  // Computed: Best Bets
  const bestBets = computed(() => {
    if (filteredMatches.value.length === 0) return []

    const highProbMatches = filteredMatches.value.filter(match =>
      match.prob_1 > 70 || match.prob_x > 70 || match.prob_2 > 70
    )

    return highProbMatches.sort((a, b) => {
      const aMax = Math.max(a.prob_1, a.prob_x, a.prob_2)
      const bMax = Math.max(b.prob_1, b.prob_x, b.prob_2)
      return bMax - aMax
    }).slice(0, 3)
  })

  // Utils
  const isTopRanked = (rank) => {
    return rank && [1, 2, 3].includes(Number(rank))
  }

  const getHighestProbability = (match) => {
    return Math.max(match.prob_1, match.prob_x, match.prob_2)
  }

  const getPredictionType = (match) => {
    const maxProb = getHighestProbability(match)
    if (maxProb === match.prob_1) return 'Home Win'
    if (maxProb === match.prob_x) return 'Draw'
    return 'Away Win'
  }

  const formatDate = (dateString) => {
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
    return new Date(dateString).toLocaleDateString('en-US', options)
  }

  // Sorting
  const applySorting = () => {
    // Sorting is now handled in the filteredMatches computed property
  }

  // Filters actions
  const applyFilters = () => {
    showFilters.value = false
  }

  const resetFilters = () => {
    dateFilter.value = ''
    minProbability.value = '0'
    leagueFilter.value = ''
    topTeamsFilter.value = 'false'
    sortOption.value = 'highest-prob'
    timeFilter.value = ''
  }

  // Fetch Matches
  const fetchData = async () => {
    loading.value = true
    error.value = null
    try {
      // Try to fetch from API first
      const res = await axios.get('/forebet-data')
      matches.value = res.data.map(match => ({
        ...match,
        league: match.game.split(' - ')[0] || match.league
      }))
    } catch (e) {
      console.error('Error loading predictions', e)
      // If API fails, use sample data
      matches.value = sampleMatches.map(match => ({
        ...match,
        league: match.game.split(' - ')[0] || match.league
      }))
      error.value = 'Using sample data - API unavailable'
    } finally {
      loading.value = false
    }
  }

  // Load on mount
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
  </style>
