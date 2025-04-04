<template>
    <div class="min-h-screen bg-gray-50 p-4 md:p-6">
        <div class="">
            <!-- Header Section -->
            <!-- Animated Header Section -->
            <header class="mb-8 animate-fade-in-up">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                    <!-- Logo + Title -->
                    <div class="flex items-center gap-4">
                        <!-- Tunisia Flag Logo -->
                        <div class="relative group transition-all duration-300">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Tunisia.svg"
                                alt="Tunisia Logo"
                                class="w-12 h-12 rounded-lg shadow-lg border-2 border-white transform group-hover:rotate-6 transition-transform duration-300" />
                            <div
                                class="absolute -inset-2 rounded-lg bg-gradient-to-tr from-red-500/20 to-red-900/10 -z-10">
                            </div>
                        </div>

                        <div class="transition-transform duration-300 group-hover:scale-105">
                            <h1
                                class="text-3xl md:text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-red-700 via-red-500 to-red-400 tracking-tight">
                                ⚽ DimaRaba7
                            </h1>
                            <p class="text-sm text-gray-600 font-medium">
                                <span
                                    class="bg-gradient-to-r from-red-500 to-red-400 bg-clip-text text-transparent">Tunisian
                                    Football Intelligence</span>
                                • Predictions • Analytics
                            </p>

                            <!-- Online User Count Section -->
                            <p class="text-xs text-gray-500 mt-1 flex items-center gap-1">
                                <!-- User Icon -->
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 text-green-500"
                                    viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4S8 5.79 8 8s1.79 4 4 4zM12 14c-4.42
                 0-8 1.79-8 4v2h16v-2c0-2.21-3.58-4-8-4z" />
                                </svg>
                                {{ onlineUsers }} visitors online
                            </p>


                        </div>

                    </div>

                    <!-- Buttons -->
                    <div class="flex gap-3">
                        <button @click="fetchData"
                            class="flex items-center gap-2 px-4 py-2.5 bg-gradient-to-br from-white to-gray-50 rounded-xl shadow-sm hover:shadow-md transition-all border border-gray-100 hover:border-red-200 group">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5 text-red-500 group-hover:rotate-180 transition-transform duration-300"
                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                            </svg>
                            <span class="font-medium text-gray-700">Refresh</span>
                        </button>

                        <button @click="showFilters = !showFilters"
                            class="flex items-center gap-2 px-4 py-2.5 bg-gradient-to-br from-white to-gray-50 rounded-xl shadow-sm hover:shadow-md transition-all border border-gray-100 hover:border-red-200 group">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5 text-red-500 group-hover:scale-110 transition-transform duration-300"
                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
                            </svg>
                            <span class="font-medium text-gray-700">{{ showFilters ? 'Hide' : 'Show' }} Filters</span>
                        </button>
                    </div>
                </div>
            </header>




            <!-- Main Content Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
                <!-- Left Sidebar - Stats & Filters -->
                <div class="lg:col-span-1 space-y-6">
                    <!-- Filters Card -->
                    <!-- Filters Card -->
                    <div v-if="showFilters" class="bg-white p-5 rounded-2xl shadow-sm border border-gray-200">
                        <h3 class="font-semibold text-gray-800 mb-4 flex items-center gap-2 text-lg">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                            </svg>
                            Filter Matches
                        </h3>
                        <div class="space-y-4">
                            <!-- Date -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Date</label>
                                <input type="date" v-model="dateFilter"
                                    class="w-full rounded-lg border-gray-200 shadow-sm focus:border-red-500 focus:ring-red-500 text-sm">
                            </div>

                            <!-- Min Confidence -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Min Confidence</label>
                                <select v-model="minProbability"
                                    class="w-full rounded-lg border-gray-200 shadow-sm focus:border-red-500 focus:ring-red-500 text-sm">
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
                                <select v-model="topTeamsFilter"
                                    class="w-full rounded-lg border-gray-200 shadow-sm focus:border-red-500 focus:ring-red-500 text-sm">
                                    <option value="false">All Teams</option>
                                    <option value="true">Top 3 Ranked Only</option>
                                </select>
                            </div>

                            <!-- <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Insights</label>
                                <select v-model="tagFilter"
                                    class="w-full rounded-lg border-gray-200 shadow-sm focus:border-red-500 focus:ring-red-500 text-sm">
                                    <option value="">All</option>
                                    <option value="over">?? Over 2.5 Goals</option>
                                    <option value="safe">? Safe Pick</option>
                                </select>
                            </div> -->


                            <!--  <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Min Confidence</label>
                                <input type="range" min="0" max="100" step="10" v-model="minProbability"
                                    class="w-full accent-red-500">
                                <p class="text-xs text-gray-500 mt-1">Showing picks with {{ minProbability }}%+
                                    probability</p>
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Predicted Result</label>
                                <select v-model="pickFilter"
                                    class="w-full rounded-lg border-gray-200 shadow-sm focus:border-red-500 focus:ring-red-500 text-sm">
                                    <option value="">All Picks</option>
                                    <option value="1">Home Win</option>
                                    <option value="X">Draw</option>
                                    <option value="2">Away Win</option>
                                </select>
                            </div> -->

                            <div class="mt-3 flex items-center gap-2">
                                <input type="checkbox" v-model="smartDefaults" id="smartDefaults"
                                    class="text-red-600 border-gray-300 rounded focus:ring-red-500">
                                <label for="smartDefaults" class="text-sm text-gray-700">Auto-detect ?? Strong
                                    Picks</label>
                            </div>

                        </div>

                        <!-- Actions -->
                        <div class="mt-6 flex justify-end gap-3">
                            <button @click="resetFilters"
                                class="px-4 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 hover:bg-gray-50">
                                Reset
                            </button>
                            <button @click="applyFilters"
                                class="px-4 py-2 bg-red-600 rounded-lg text-sm font-medium text-white hover:bg-red-700">
                                Apply
                            </button>
                        </div>
                    </div>

                    <!-- Modern Stats Card -->
                    <div
                        class="bg-white p-6 rounded-2xl shadow-md border border-gray-100 hover:shadow-lg transition-all duration-300 animate-fade-in-up">
                        <h3 class="text-lg font-semibold text-gray-800 mb-6 flex items-center gap-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                            </svg>
                            Today’s Stats
                        </h3>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm">
                            <!-- Total Matches -->
                            <div
                                class="flex items-center justify-between px-3 py-2 rounded-lg bg-gray-50 hover:bg-gray-100 transition">
                                <div class="flex items-center gap-2 text-gray-700 font-medium">
                                    <svg class="h-4 w-4 text-red-400" fill="none" viewBox="0 0 24 24"
                                        stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M9 12h6m2 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                    Total Matches
                                </div>
                                <span class="text-gray-800 font-semibold">{{ filteredMatches.length }}</span>
                            </div>

                            <!-- High Confidence -->
                            <div
                                class="flex items-center justify-between px-3 py-2 rounded-lg bg-green-50 hover:bg-green-100 transition">
                                <div class="flex items-center gap-2 text-green-700 font-medium">
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M5 13l4 4L19 7" />
                                    </svg>
                                    High Confidence
                                </div>
                                <span class="text-green-800 font-semibold">{{ highConfidenceMatchesCount }} ({{
                                    highConfidencePercentage }}%)</span>
                            </div>

                            <!-- Top Team Matches -->
                            <div
                                class="flex items-center justify-between px-3 py-2 rounded-lg bg-yellow-50 hover:bg-yellow-100 transition">
                                <div class="flex items-center gap-2 text-yellow-700 font-medium">
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M8 17l4-4 4 4m0-8l-4 4-4-4" />
                                    </svg>
                                    Top Team Matches
                                </div>
                                <span class="text-yellow-800 font-semibold">{{ topTeamMatchesCount }}</span>
                            </div>

                            <!-- Avg Confidence -->
                            <div
                                class="flex items-center justify-between px-3 py-2 rounded-lg bg-indigo-50 hover:bg-indigo-100 transition">
                                <div class="flex items-center gap-2 text-indigo-700 font-medium">
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M11 11V7a4 4 0 118 0v4m-4 4h-1a4 4 0 100 8h1a4 4 0 100-8z" />
                                    </svg>
                                    Avg. Confidence
                                </div>
                                <span class="text-indigo-800 font-semibold">{{ averageConfidence }}%</span>
                            </div>
                        </div>
                    </div>



                    <!-- Must-Watch Matches -->
                    <div v-if="mustWatchMatches.length"
                        class="bg-white border border-gray-100 rounded-2xl shadow-sm mt-6 overflow-hidden">
                        <!-- Header -->
                        <div class="bg-yellow-50 border-b border-yellow-100 px-6 py-4">
                            <h2 class="text-lg font-bold text-yellow-800 flex items-center gap-2">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-yellow-500" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M13 16h-1v-4h-1m0-4h.01M12 20h.01M9 12h.01M15 12h.01M12 8v.01" />
                                </svg>
                                Must-Watch Matches Today
                            </h2>
                        </div>

                        <!-- Match List -->
                        <div class="divide-y divide-gray-100">
                            <div v-for="match in (showAllMustWatch ? mustWatchMatches : mustWatchMatches.slice(0, 4))"
                                :key="match.id"
                                class="grid grid-cols-1 sm:grid-cols-12 gap-4 items-center px-6 py-3 hover:bg-gray-50 transition">
                                <!-- Time -->
                                <div class="col-span-2 text-sm text-gray-500 font-medium">
                                    {{ match.time_str }}
                                </div>

                                <!-- Teams -->
                                <div
                                    class="col-span-6 flex flex-col sm:flex-row sm:items-center sm:gap-2 text-sm text-gray-800 font-semibold">
                                    <span>{{ match.home_team }} <span v-if="match.home_rank"
                                            class="text-gray-400 text-xs font-normal">(#{{ match.home_rank
                                            }})</span></span>
                                    <span class="text-gray-500 font-normal hidden sm:inline">vs</span>
                                    <span>{{ match.away_team }} <span v-if="match.away_rank"
                                            class="text-gray-400 text-xs font-normal">(#{{ match.away_rank
                                            }})</span></span>
                                </div>

                                <!-- Prediction -->
                                <div class="col-span-2 text-sm text-gray-700 font-medium">
                                    🧠
                                    {{
                                        match.prediction === '1' ? 'Home Win' :
                                            match.prediction === 'X' ? 'Draw' :
                                                match.prediction === '2' ? 'Away Win' :
                                    'Unknown'
                                    }}
                                </div>

                                <!-- Hot Pick + View -->
                                <div class="col-span-2 flex items-center justify-between sm:justify-end gap-2">
                                    <span v-if="getHighestProbability(match) > 60"
                                        class="text-xs bg-yellow-100 text-yellow-800 font-semibold px-2 py-0.5 rounded-full">
                                        🔥 Hot Pick
                                    </span>
                                    <a :href="match.match_url" target="_blank"
                                        class="text-sm text-blue-600 hover:underline">
                                        👀 View
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- See More Button -->
                        <div class="text-center py-4 border-t border-gray-100">
                            <button @click="showAllMustWatch = !showAllMustWatch"
                                class="text-sm font-medium text-yellow-700 hover:underline">
                                {{ showAllMustWatch ? '🔽 Show Less' : '🔼 See More' }}
                            </button>
                        </div>
                    </div>

  <div ref="adContainer"></div>



                </div>

                <!-- Main Content Area -->
                <div class="lg:col-span-3 space-y-6">
                    <!-- Best Bets Section -->
                    <div v-if="bestBets.length > 0"
                        class="bg-white/90 backdrop-blur border border-indigo-100 p-6 rounded-2xl shadow-md">

                        <!-- Header -->
                        <div class="flex flex-col md:flex-row md:items-center justify-between mb-6 gap-4">
                            <div class="flex items-center gap-2 text-indigo-800">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-yellow-400" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                                </svg>
                                <h2 class="text-xl font-bold">Best Bets of the Day</h2>
                            </div>

                            <div class="flex items-center gap-3 flex-wrap text-sm text-blue-800">
                                <span class="bg-blue-100 px-3 py-1 rounded-full font-medium">
                                    {{ bestBets.length }} top confidence picks
                                </span>
                                <span class="hidden sm:inline text-gray-400">|</span>
                                <span class="text-gray-600 font-medium">
                                    {{ new Date().toLocaleDateString() }}
                                </span>
                                <span class="hidden sm:inline text-gray-400">|</span>
                                <div class="flex items-center gap-2 text-xs text-gray-500">
                                    <span class="inline-flex items-center gap-1">
                                        <span class="h-3 w-3 rounded-full bg-green-400 inline-block"></span> 70%+
                                    </span>
                                    <span class="inline-flex items-center gap-1">
                                        <span class="h-3 w-3 rounded-full bg-yellow-300 inline-block"></span> Below 70%
                                    </span>
                                </div>
                            </div>
                        </div>

                        <!-- Match Grid -->
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
                            <div v-for="match in bestBets" :key="match.id"
                                class="bg-gradient-to-tr from-white via-gray-50 to-blue-50 border border-gray-200 rounded-xl shadow-sm hover:shadow-lg hover:scale-[1.01] transition-all duration-300">
                                <div class="p-4 space-y-2">

                                    <!-- Match Info -->
                                    <div class="flex items-center justify-between">
                                        <div>
                                            <h3 class="text-sm font-semibold text-gray-800 truncate">{{ match.game }}
                                            </h3>
                                            <p class="text-xs text-gray-500">{{ match.league }}</p>
                                        </div>
                                        <span class="text-xs font-bold px-2 py-1 rounded-full" :class="{
                                            'bg-green-100 text-green-800': getHighestProbability(match) >= 70,
                                            'bg-yellow-100 text-yellow-800': getHighestProbability(match) < 70
                                        }">
                                            {{ getHighestProbability(match) }}%
                                        </span>
                                    </div>

                                    <!-- Teams -->
                                    <div class="flex justify-between items-center pt-2">
                                        <div class="text-center">
                                            <div class="font-bold text-gray-800">{{ match.home_team }}</div>
                                            <div v-if="match.home_rank" class="text-xs text-gray-400 mt-0.5">#{{
                                                match.home_rank }}</div>
                                        </div>
                                        <div class="text-xs text-gray-500 font-medium px-2">VS</div>
                                        <div class="text-center">
                                            <div class="font-bold text-gray-800">{{ match.away_team }}</div>
                                            <div v-if="match.away_rank" class="text-xs text-gray-400 mt-0.5">#{{
                                                match.away_rank }}</div>
                                        </div>
                                    </div>

                                    <!-- Prediction Label with Live Odds -->
                                    <div class="text-xs mt-2 text-indigo-600 font-semibold flex items-center gap-2">
                                        <span class="underline">
                                            🔮 {{
                                                match.prediction === '1' ? 'Home Win' :
                                                    match.prediction === 'X' ? 'Draw' :
                                                        match.prediction === '2' ? 'Away Win' :
                                            'Unknown'
                                            }}
                                        </span>

                                        <!-- Live Odds badge -->
                                        <span v-if="match.live_odds"
                                            class="bg-indigo-100 text-indigo-800 px-2 py-0.5 rounded-full text-[10px] font-medium shadow-sm">
                                            💸 {{ match.live_odds }}
                                        </span>
                                    </div>

                                    <!-- Confidence Bars -->
                                    <div class="flex justify-between items-end gap-1 mt-4 text-xs text-center">
                                        <div class="flex-1">
                                            <div class="font-bold">1</div>
                                            <div class="h-2 w-full bg-gray-200 rounded-full mt-1 overflow-hidden">
                                                <div class="h-full rounded-full transition-all"
                                                    :class="{ 'bg-green-500': match.prob_1 > 60, 'bg-gray-300': match.prob_1 <= 60 }"
                                                    :style="{ width: match.prob_1 + '%' }"></div>
                                            </div>
                                            <div class="mt-1">{{ match.prob_1 }}%</div>
                                        </div>
                                        <div class="flex-1">
                                            <div class="font-bold">X</div>
                                            <div class="h-2 w-full bg-gray-200 rounded-full mt-1 overflow-hidden">
                                                <div class="h-full rounded-full transition-all"
                                                    :class="{ 'bg-yellow-400': match.prob_x > 60, 'bg-gray-300': match.prob_x <= 60 }"
                                                    :style="{ width: match.prob_x + '%' }"></div>
                                            </div>
                                            <div class="mt-1">{{ match.prob_x }}%</div>
                                        </div>
                                        <div class="flex-1">
                                            <div class="font-bold">2</div>
                                            <div class="h-2 w-full bg-gray-200 rounded-full mt-1 overflow-hidden">
                                                <div class="h-full rounded-full transition-all"
                                                    :class="{ 'bg-red-500': match.prob_2 > 60, 'bg-gray-300': match.prob_2 <= 60 }"
                                                    :style="{ width: match.prob_2 + '%' }"></div>
                                            </div>
                                            <div class="mt-1">{{ match.prob_2 }}%</div>
                                        </div>
                                    </div>

                                    <!-- Modern Stats Section -->
                                    <div class="grid grid-cols-2 gap-4 text-xs mt-4">
                                        <!-- Home Stats -->
                                        <div class="bg-blue-50 border border-blue-100 rounded-2xl p-3 shadow-md">
                                            <div class="flex justify-between items-center mb-2">
                                                <div class="font-semibold text-blue-800">
                                                    {{ match.home_team }}
                                                </div>
                                                <span v-if="match.home_rank"
                                                    class="text-[10px] bg-gradient-to-r from-blue-100 to-blue-200 text-blue-700 px-2 py-0.5 rounded-full shadow-sm">
                                                    #{{ match.home_rank }}
                                                </span>
                                            </div>
                                            <div class="space-y-2 text-[11px] text-gray-700">
                                                <div class="flex justify-between">
                                                    <span class="text-gray-500">PTS</span>
                                                    <span class="font-medium">{{ match.home_pts || '/' }}</span>
                                                </div>
                                                <div class="flex justify-between">
                                                    <span class="text-gray-500">W / D / L</span>
                                                    <span class="font-medium">{{ match.home_w }}/{{ match.home_d }}/{{
                                                        match.home_l }}</span>
                                                </div>
                                                <div class="flex justify-between">
                                                    <span class="text-gray-500">GF / GA</span>
                                                    <span class="font-medium">{{ match.home_gf }}/{{ match.home_ga
                                                        }}</span>
                                                </div>
                                                <div class="flex justify-between">
                                                    <span class="text-gray-500">GD</span>
                                                    <span class="font-medium">{{ match.home_gd || '/' }}</span>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Away Stats -->
                                        <div class="bg-indigo-50 border border-indigo-100 rounded-2xl p-3 shadow-md">
                                            <div class="flex justify-between items-center mb-2">
                                                <div class="font-semibold text-indigo-800">
                                                    {{ match.away_team }}
                                                </div>
                                                <span v-if="match.away_rank"
                                                    class="text-[10px] bg-gradient-to-r from-indigo-100 to-indigo-200 text-indigo-700 px-2 py-0.5 rounded-full shadow-sm">
                                                    #{{ match.away_rank }}
                                                </span>
                                            </div>
                                            <div class="space-y-2 text-[11px] text-gray-700">
                                                <div class="flex justify-between">
                                                    <span class="text-gray-500">PTS</span>
                                                    <span class="font-medium">{{ match.away_pts || '/' }}</span>
                                                </div>
                                                <div class="flex justify-between">
                                                    <span class="text-gray-500">W / D / L</span>
                                                    <span class="font-medium">{{ match.away_w }}/{{ match.away_d }}/{{
                                                        match.away_l }}</span>
                                                </div>
                                                <div class="flex justify-between">
                                                    <span class="text-gray-500">GF / GA</span>
                                                    <span class="font-medium">{{ match.away_gf }}/{{ match.away_ga
                                                        }}</span>
                                                </div>
                                                <div class="flex justify-between">
                                                    <span class="text-gray-500">GD</span>
                                                    <span class="font-medium">{{ match.away_gd || '/' }}</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Action -->
                                <a :href="match.match_url" target="_blank"
                                    class="block text-center bg-blue-50 hover:bg-blue-100 py-2 text-xs font-medium text-blue-700 transition">
                                    📊 View Analysis
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
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-500 mr-2" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <p class="text-red-700 font-medium">{{ error }}</p>
                        </div>
                    </div>

                    <!-- Empty State -->
                    <div v-else-if="filteredMatches.length === 0" class="text-center py-20">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto text-gray-300" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <p class="text-gray-500 mt-4 text-lg">No matches found with current filters</p>
                        <button @click="resetFilters"
                            class="mt-4 px-4 py-2 bg-blue-600 rounded-lg text-sm font-medium text-white hover:bg-blue-700">
                            Reset Filters
                        </button>
                    </div>

                    <!-- Regular Matches Grid -->
                    <!-- Regular Matches Section -->
                    <div class="mt-10">
                        <!-- Toggle View Button -->
                        <div class="flex justify-end mb-4">
                            <button @click="tableView = !tableView"
                                class="text-sm px-4 py-2 rounded-full border border-gray-200 bg-white hover:bg-blue-50 transition flex items-center gap-2 shadow-sm">
                                <svg v-if="tableView" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-blue-600"
                                    fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M4 6h16M4 10h16M4 14h16M4 18h16" />
                                </svg>
                                <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-blue-600" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M4 6h7v7H4zM13 6h7v7h-7zM4 17h7v1H4zM13 17h7v1h-7z" />
                                </svg>
                                <span class="text-blue-600 font-medium">{{ tableView ? 'Grid View' : 'Table View'
                                    }}</span>
                            </button>
                        </div>

                        <!-- Table View -->
                        <div v-if="tableView"
                            class="overflow-x-auto bg-white shadow-sm rounded-xl border border-gray-100">
                            <table class="min-w-[1024px] w-full divide-y divide-gray-200 text-sm">
                                <thead class="bg-gray-50 text-gray-700 text-xs uppercase sticky top-0 z-10">
                                    <tr>
                                        <th class="px-4 py-3 text-left whitespace-nowrap">Time</th>
                                        <th class="px-4 py-3 text-left whitespace-nowrap">Game</th>
                                        <th class="px-4 py-3 text-left whitespace-nowrap">Pick</th>
                                        <th class="px-4 py-3 text-center whitespace-nowrap">1</th>
                                        <th class="px-4 py-3 text-center whitespace-nowrap">X</th>
                                        <th class="px-4 py-3 text-center whitespace-nowrap">2</th>
                                        <th class="px-4 py-3 text-center whitespace-nowrap">Odds</th>
                                        <th class="px-4 py-3 text-center whitespace-nowrap">Rank</th>
                                        <th class="px-4 py-3 text-right whitespace-nowrap">Action</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-gray-100">
                                    <tr v-for="match in paginatedMatchess" :key="match.id"
                                        class="hover:bg-blue-50/40 transition">
                                        <td class="px-4 py-2 whitespace-nowrap">{{ match.time_str }} <div
                                                class="mt-3 flex flex-wrap gap-2" v-if="getMatchTags(match).length">
                                                <span v-for="tag in getMatchTags(match)" :key="tag"
                                                    class="text-[11px] px-2 py-0.5 rounded-full font-medium bg-yellow-100 text-yellow-800">
                                                    {{ tag }}
                                                </span>
                                            </div>
                                        </td>


                                        <!-- Game Column: Teams + Stats -->
                                        <td class="px-4 py-2">
                                            <div class="font-medium text-gray-800">{{ match.home_team }} <span
                                                    class="text-gray-400">vs</span> {{ match.away_team }}</div>

                                            <div
                                                class="grid grid-cols-1 md:grid-cols-2 gap-2 text-[11px] text-gray-700 mt-2">
                                                <!-- Home Team Stats -->
                                                <div class="bg-green-50 p-2 rounded-md">
                                                    <strong class="block text-green-700 text-[12px] mb-1">🏠 Home
                                                        Stats</strong>

                                                    <div class="flex flex-wrap gap-x-2 gap-y-1">
                                                        <span>🎯 GP: {{ match.home_gp }}</span>
                                                        <span>✅ W: {{ match.home_w }}</span>
                                                        <span>➖ D: {{ match.home_d }}</span>
                                                        <span>❌ L: {{ match.home_l }}</span>
                                                        <span>⚽ GF: {{ match.home_gf }}</span>
                                                        <span>🛡️ GA: {{ match.home_ga }}</span>
                                                        <span>📊 GD: {{ match.home_gd }}</span>
                                                        <span>🏆 Pts: {{ match.home_pts }}</span>

                                                    </div>
                                                </div>

                                                <!-- Away Team Stats -->
                                                <div class="bg-blue-50 p-2 rounded-md">
                                                    <strong class="block text-blue-700 text-[12px] mb-1">🚗 Away
                                                        Stats</strong>

                                                    <div class="flex flex-wrap gap-x-2 gap-y-1">
                                                        <span>🎯 GP: {{ match.home_gp }}</span>
                                                        <span>✅ W: {{ match.home_w }}</span>
                                                        <span>➖ D: {{ match.home_d }}</span>
                                                        <span>❌ L: {{ match.home_l }}</span>
                                                        <span>⚽ GF: {{ match.home_gf }}</span>
                                                        <span>🛡️ GA: {{ match.home_ga }}</span>
                                                        <span>📊 GD: {{ match.home_gd }}</span>
                                                        <span>🏆 Pts: {{ match.home_pts }}</span>

                                                    </div>
                                                </div>
                                            </div>
                                        </td>

                                        <!-- Pick -->
                                        <td class="px-4 py-2">
                                            <span class="text-xs font-semibold px-2 py-1 rounded-full" :class="{
                                                'bg-green-100 text-green-800': match.prediction === '1',
                                                'bg-yellow-100 text-yellow-800': match.prediction === 'X',
                                                'bg-red-100 text-red-800': match.prediction === '2'
                                            }">
                                                {{ match.prediction }}
                                            </span>
                                        </td>

                                        <!-- Probabilities -->
                                        <td class="px-2 py-2 text-center text-xs whitespace-nowrap">{{ match.prob_1 }}%
                                        </td>
                                        <td class="px-2 py-2 text-center text-xs whitespace-nowrap">{{ match.prob_x }}%
                                        </td>
                                        <td class="px-2 py-2 text-center text-xs whitespace-nowrap">{{ match.prob_2 }}%
                                        </td>

                                        <!-- Odds -->
                                        <td class="px-2 py-2 text-center text-xs whitespace-nowrap">
                                            <span v-if="match.live_odds"
                                                class="bg-indigo-100 text-indigo-700 px-2 py-0.5 rounded-full font-medium">
                                                {{ match.live_odds }}
                                            </span>

                                        </td>

                                        <!-- Rank -->
                                        <td class="px-4 py-2 text-center text-xs whitespace-nowrap">
                                            <div class="flex flex-col items-center text-gray-500">
                                                <span>🏠 {{ match.home_rank || '-' }}</span>
                                                <span>🚗 {{ match.away_rank || '-' }}</span>

                                            </div>
                                        </td>

                                        <!-- Action -->
                                        <td class="px-4 py-2 text-right whitespace-nowrap">
                                            <a :href="match.match_url" target="_blank"
                                                class="text-blue-600 hover:underline text-xs font-medium">
                                                Details ?
                                            </a>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>

                            <!-- Pagination -->
                            <div v-if="hasMorePagess" class="p-4 text-center">
                                <button @click="loadMores"
                                    class="px-4 py-2 bg-blue-600 text-white text-sm rounded-lg hover:bg-blue-700 transition">
                                    See More Matches ?
                                </button>
                            </div>
                        </div>


                        <!-- Grid View -->
  <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <div v-for="match in paginatedMatchess" :key="match.id" class="bg-white border border-gray-200 rounded-xl shadow-lg hover:shadow-xl transition-all transform hover:scale-105 overflow-hidden">

      <div class="p-5">
        <!-- Header: Match Teams & Prediction -->
        <div class="flex justify-between items-start mb-4">
          <div>
            <h3 class="font-bold text-lg text-gray-800">{{ match.home_team }} vs {{ match.away_team }}</h3>
            <p class="text-sm text-gray-500 mt-1">{{ match.time_str }}</p>
          </div>
          <span class="text-xs font-bold px-3 py-1 rounded-full" :class="{
            'bg-green-100 text-green-800': match.prediction === '1',
            'bg-yellow-100 text-yellow-800': match.prediction === 'X',
            'bg-red-100 text-red-800': match.prediction === '2'
          }">
            {{ match.prediction }}
          </span>
        </div>

        <!-- Probabilities -->
        <div class="flex justify-between text-sm text-gray-600 mt-4">
          <div class="text-center flex-1">
            <div class="font-semibold text-blue-600">1</div>
            <div>{{ match.prob_1 }}%</div>
          </div>
          <div class="text-center flex-1">
            <div class="font-semibold text-yellow-600">X</div>
            <div>{{ match.prob_x }}%</div>
          </div>
          <div class="text-center flex-1">
            <div class="font-semibold text-red-600">2</div>
            <div>{{ match.prob_2 }}%</div>
          </div>
        </div>

        <!-- Prediction Type -->


        <!-- Ranks -->
        <div class="mt-3 flex justify-between text-sm text-gray-500">
          <span>🏠 {{ match.home_rank || '-' }}</span>
          <span>🚗 {{ match.away_rank || '-' }}</span>
        </div>

        <!-- Live Odds -->
        <span v-if="match.live_odds" class="bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full font-medium mt-2">
          💸 {{ match.live_odds }}
        </span>

        <!-- Extra Tags (GG, Over 2.5, Safe Pick, etc) -->
        <div class="mt-4 flex flex-wrap gap-2" v-if="getMatchTags(match).length">
          <span v-for="tag in getMatchTags(match)" :key="tag" class="text-xs px-3 py-1 rounded-full bg-yellow-100 text-yellow-800">
            {{ tag }}
          </span>
        </div>

        <!-- Enhanced Stats -->
        <div class="grid grid-cols-2 gap-4 text-xs text-gray-700 mt-4">
          <!-- Home Stats -->
          <div class="bg-green-50 p-3 rounded-md">
            <strong class="block text-green-700 mb-1">🏠 Home Stats</strong>
            <div class="flex flex-wrap gap-x-2 gap-y-1">
              <span>🎯 GP: {{ match.home_gp }}</span>
              <span>✅ W: {{ match.home_w }}</span>
              <span>➖ D: {{ match.home_d }}</span>
              <span>❌ L: {{ match.home_l }}</span>
              <span>⚽ GF: {{ match.home_gf }}</span>
              <span>🛡️ GA: {{ match.home_ga }}</span>
              <span>📊 GD: {{ match.home_gd }}</span>
              <span>🏆 Pts: {{ match.home_pts }}</span>
            </div>
          </div>

          <!-- Away Stats -->
          <div class="bg-blue-50 p-3 rounded-md">
            <strong class="block text-blue-700 mb-1">🚗 Away Stats</strong>
            <div class="flex flex-wrap gap-x-2 gap-y-1">
              <span>🎯 GP: {{ match.away_gp }}</span>
              <span>✅ W: {{ match.away_w }}</span>
              <span>➖ D: {{ match.away_d }}</span>
              <span>❌ L: {{ match.away_l }}</span>
              <span>⚽ GF: {{ match.away_gf }}</span>
              <span>🛡️ GA: {{ match.away_ga }}</span>
              <span>📊 GD: {{ match.away_gd }}</span>
              <span>🏆 Pts: {{ match.away_pts }}</span>
            </div>
          </div>
        </div>
      </div>

                                <!-- Details Link -->
                                <a :href="match.match_url" target="_blank"
                                    class="text-xs text-blue-600 hover:underline text-center block bg-gray-50 py-2 font-medium">
                                    View Details ?
                                </a>
                            </div>

                            <!-- See More (Grid version) -->
                            <div v-if="hasMorePagess" class="col-span-full p-4 text-center">
                                <button @click="loadMores"
                                    class="px-4 py-2 bg-blue-600 text-white text-sm rounded-lg hover:bg-blue-700 transition">
                                    See More Matches ?
                                </button>
                            </div>
                        </div>

                    </div>


                </div>
            </div>
        </div>
    </div>
    <!-- Floating Footer -->
    <footer
        class="fixed bottom-4 right-4 bg-white/80 backdrop-blur-sm border border-gray-200 rounded-full shadow-md px-4 py-1.5 text-sm text-gray-600 font-medium flex items-center gap-2 animate-fade-in">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-red-500" viewBox="0 0 24 24" fill="currentColor">
            <path
                d="M12 22c5.52 0 10-4.48 10-10S17.52 2 12 2 2 6.48 2 12s4.48 10 10 10zm0-1.5c-4.69 0-8.5-3.81-8.5-8.5S7.31 3.5 12 3.5 20.5 7.31 20.5 12 16.69 20.5 12 20.5z" />
            <path d="M10.25 15h1.5V9h-1.5v6zm0 2h1.5v-1.5h-1.5V17z" />
        </svg>
        Mahmoud Bouhlel © {{ new Date().getFullYear() }}
    </footer>

</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

// State
const matches = ref([])
const loading = ref(true)
const error = ref(null)
const showFilters = ref(false)
const showAllMustWatch = ref(false)
const tableView = ref(false)
const currentPage = ref(1)
const rowsPerPage = 50
const page = ref(1)
const perPage = 50
const tagFilter = ref('')
// Tag filter
if (tagFilter.value) {
    result = result.filter(match => {
        const tags = getMatchTags(match)
        return tags.some(tag => tag.toLowerCase().includes(tagFilter.value.toLowerCase()))
    })
}
const adContainer = ref(null);



const paginatedMatchess = computed(() => {
    return filteredMatches.value.slice(0, page.value * perPage)
})

const hasMorePagess = computed(() => {
    return filteredMatches.value.length > paginatedMatchess.value.length
})

const loadMores = () => {
    page.value++
}

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

const mustWatchMatches = computed(() =>
    filteredMatches.value
        .filter(m => {
            const home = Number(m.home_rank)
            const away = Number(m.away_rank)
            const top4 = [1, 2, 3, 4]
            return (top4.includes(home) && away >= 10) || (top4.includes(away) && home >= 10)
        })
        .sort((a, b) => getHighestProbability(b) - getHighestProbability(a))
        .slice(0, 10)
)


const paginatedMatches = computed(() => {
    const start = (currentPage.value - 1) * rowsPerPage
    const end = start + rowsPerPage
    return filteredMatches.value.slice(start, end)
})

const hasMorePages = computed(() => {
    return filteredMatches.value.length > currentPage.value * rowsPerPage
})

const loadMore = () => {
    currentPage.value++
}


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
const onlineUsers = ref(0)

onMounted(() => {
    // Simulate random active users
    onlineUsers.value = Math.floor(20 + Math.random() * 100)

    // Optional: update every 30 seconds
    setInterval(() => {
        onlineUsers.value = Math.floor(20 + Math.random() * 100)
    }, 30000)
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
const todayISODate = new Date().toISOString().split('T')[0]
// Combo Builder State
// Combo Builder State
const comboRisk = ref('conservative')
const comboSize = ref(3)
const smartCombo = ref([])
const homeRankLimit = ref(10)
const awayRankLimit = ref(10)

const generateSmartCombo = () => {
    const threshold = {
        conservative: 70,
        balanced: 60,
        risky: 50
    }[comboRisk.value]

    const eligible = filteredMatches.value.filter(match => {
        const prob = getHighestProbability(match)
        const homeValid = !match.home_rank || match.home_rank <= homeRankLimit.value
        const awayValid = !match.away_rank || match.away_rank <= awayRankLimit.value
        return prob >= threshold && homeValid && awayValid
    })

    const sorted = eligible.sort((a, b) => getHighestProbability(b) - getHighestProbability(a))
    smartCombo.value = sorted.slice(0, comboSize.value)
}




// Combo stats
const comboConfidence = computed(() => {
    if (!smartCombo.value.length) return 0
    const probs = smartCombo.value.map(m => getHighestProbability(m) / 100)
    return Math.round(probs.reduce((acc, p) => acc * p, 1) * 100)
})

const estimatedComboReturn = computed(() => {
    if (!smartCombo.value.length) return 0
    const odds = smartCombo.value.map(m => 100 / getHighestProbability(m))
    return odds.reduce((acc, o) => acc * o, 1).toFixed(2)
})


const top5Today = computed(() => {
    return bestBets.value
        .filter(match => match.iso_time.startsWith(todayISODate)) // only today's matches
        .slice(0, 5)
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
function getMatchTags(match) {
    const hGF = parseInt(match.home_gf || 0);
    const hGA = parseInt(match.home_ga || 0);
    const aGF = parseInt(match.away_gf || 0);
    const aGA = parseInt(match.away_ga || 0);
    const hPts = parseInt(match.home_pts || 0);
    const aPts = parseInt(match.away_pts || 0);

    const totalGoals = hGF + hGA + aGF + aGA;
    const tags = [];

    if (totalGoals > 70 || (hGF > 30 && aGF > 30)) {
        tags.push('?? Over 2.5 Goals');
    }

    if (Math.abs(hPts - aPts) > 20 && (hPts > 0 || aPts > 0)) {
        tags.push('? Safe Pick');
    }

    return tags;
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
  // Load matches
  fetchData();

  // Online users simulation
  onlineUsers.value = Math.floor(20 + Math.random() * 100);
  setInterval(() => {
    onlineUsers.value = Math.floor(20 + Math.random() * 100);
  }, 30000);

  // Inject ad script
  if (adContainer.value) {
    const script1 = document.createElement('script');
    script1.type = 'text/javascript';
    script1.innerHTML = `
      atOptions = {
        'key': 'a40af2ddee7a4e17cbd9b9ffc7dab35c',
        'format': 'iframe',
        'height': 300,
        'width': 160,
        'params': {}
      };
    `;
    const script2 = document.createElement('script');
    script2.type = 'text/javascript';
    script2.src = '//www.highperformanceformat.com/a40af2ddee7a4e17cbd9b9ffc7dab35c/invoke.js';
    adContainer.value.appendChild(script1);
    adContainer.value.appendChild(script2);
  }
});

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
button:focus,
select:focus,
input:focus {
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

    .lg\:col-span-1,
    .lg\:col-span-3 {
        grid-column: span 1;
    }
}

@keyframes fade-in-up {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fade-in {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.animate-fade-in-up {
    animation: fade-in-up 0.8s ease-out both;
}

.animate-fade-in {
    animation: fade-in 1s ease-out both;
}
</style>
