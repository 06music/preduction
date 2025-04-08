<template>
    <div class="min-h-screen bg-gray-50 p-4 md:p-6">
        <div class="">
            <!-- Header Section -->
            <!-- Animated Header Section -->
            <header class="animate-fade-in-up mb-8">
                <div class="flex flex-col justify-between gap-6 md:flex-row md:items-center">
                    <!-- Logo + Title -->
                    <div class="flex items-center gap-4">
                        <!-- Tunisia Flag Logo -->
                        <div class="group relative transition-all duration-300">
                            <img
                                src="https://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Tunisia.svg"
                                alt="Tunisia Logo"
                                class="h-12 w-12 transform rounded-lg border-2 border-white shadow-lg transition-transform duration-300 group-hover:rotate-6"
                            />
                            <div class="absolute -inset-2 -z-10 rounded-lg bg-gradient-to-tr from-red-500/20 to-red-900/10"></div>
                        </div>

                        <div class="transition-transform duration-300 group-hover:scale-105">
                            <h1
                                class="bg-gradient-to-r from-red-700 via-red-500 to-red-400 bg-clip-text text-3xl font-bold tracking-tight text-transparent md:text-4xl"
                            >
                                ⚽ DimaRaba7
                            </h1>
                            <p class="text-sm font-medium text-gray-600">
                                <span class="bg-gradient-to-r from-red-500 to-red-400 bg-clip-text text-transparent"
                                    >Tunisian Football Intelligence</span
                                >
                                • Predictions • Analytics
                            </p>

                            <!-- Online User Count Section -->
                            <p class="mt-1 flex items-center gap-1 text-xs text-gray-500">
                                <!-- User Icon -->
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 text-green-500" viewBox="0 0 24 24" fill="currentColor">
                                    <path
                                        d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4S8 5.79 8 8s1.79 4 4 4zM12 14c-4.42
                 0-8 1.79-8 4v2h16v-2c0-2.21-3.58-4-8-4z"
                                    />
                                </svg>
                                {{ onlineUsers }} visitors online
                            </p>
                        </div>
                    </div>

                    <!-- Buttons -->
                    <div class="flex gap-3">
                        <button
                            @click="fetchData"
                            class="group flex items-center gap-2 rounded-xl border border-gray-100 bg-gradient-to-br from-white to-gray-50 px-4 py-2.5 shadow-sm transition-all hover:border-red-200 hover:shadow-md"
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5 text-red-500 transition-transform duration-300 group-hover:rotate-180"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke="currentColor"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    stroke-width="2"
                                    d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
                                />
                            </svg>
                            <span class="font-medium text-gray-700">Refresh</span>
                        </button>

                        <button
                            @click="showFilters = !showFilters"
                            class="group flex items-center gap-2 rounded-xl border border-gray-100 bg-gradient-to-br from-white to-gray-50 px-4 py-2.5 shadow-sm transition-all hover:border-red-200 hover:shadow-md"
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5 text-red-500 transition-transform duration-300 group-hover:scale-110"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke="currentColor"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    stroke-width="2"
                                    d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"
                                />
                            </svg>
                            <span class="font-medium text-gray-700">{{ showFilters ? 'Hide' : 'Show' }} Filters</span>
                        </button>
                        <button @click="showComboModal = true" class="rounded-lg bg-red-600 px-4 py-2 text-white transition hover:bg-red-700">
                            🎯 Build My Combo
                        </button>
                    </div>
                </div>
            </header>

         <!-- Combo Builder Modal -->
<!-- Combo Builder Modal -->
<div
  v-if="showComboModal"
  class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50 backdrop-blur-sm px-4"
>
  <div
    class="animate-fade-in-up relative w-full max-w-2xl rounded-2xl bg-white p-6 shadow-2xl
           overflow-y-auto max-h-[90vh]"
  >
    <!-- Close Button -->
    <button
      @click="showComboModal = false"
      class="absolute right-3 top-3 text-xl font-bold text-gray-500 hover:text-red-500"
    >
      ×
    </button>

    <!-- Title -->
    <h2 class="mb-4 text-xl font-bold text-gray-800 flex items-center gap-2">
      ⚙️ Smart Combo Generator
    </h2>

    <!-- Controls -->
    <div class="mb-4 space-y-4">
      <!-- Strategy Selector -->
      <div>
        <label class="block text-sm font-medium">Combo Type</label>
        <select
          v-model="comboStrategy"
          class="w-full rounded-lg border p-2 text-sm"
        >
          <option value="best">📊 Top Confidence (1/X/2)</option>
          <option value="goals">⚽ Goal Fest (BTTS / Over)</option>
          <option value="mixed">🔀 Mixed Smart Combo</option>
          <option value="smart_over">📈 Smart Over Picks</option>
          <option value="smart_under">📉 Smart Under Picks</option>
          <option value="home_over">🏠 Home Over 2.5 Goals</option>
          <option value="away_over">🚗 Away Over 2.5 Goals</option>
          <option value="home_under">🏠 Home Under 2.5 Goals</option>
          <option value="away_under">🚗 Away Under 2.5 Goals</option>
          <option value="btts_focus">🎯 BTTS Strategy</option>
          <option value="draw_focus">🧊 Draw Prediction</option>
          <option value="safe_combo">🛡️ Safe Combo Picks</option>
          <option value="super_combo">🧠 All-Star Smart Combo</option>
        </select>
      </div>

      <!-- Date Range -->
      <div class="grid grid-cols-2 gap-3">
        <div>
          <label class="block text-sm font-medium">Start Date</label>
          <input
            type="date"
            v-model="comboStartDate"
            class="w-full rounded-lg border p-2 text-sm"
          />
        </div>
        <div>
          <label class="block text-sm font-medium">End Date</label>
          <input
            type="date"
            v-model="comboEndDate"
            class="w-full rounded-lg border p-2 text-sm"
          />
        </div>
      </div>

      <!-- Match Count -->
      <div>
        <label class="block text-sm font-medium">Number of Matches</label>
        <input
          type="number"
          min="2"
          max="10"
          v-model="comboMatchCount"
          class="w-full rounded-lg border p-2 text-sm"
        />
      </div>

      <!-- Actions -->
      <button
        @click="generateUserCombo"
        class="mt-2 w-full rounded-lg bg-blue-600 py-2 text-white transition hover:bg-blue-700"
      >
        🚀 Generate Combo
      </button>
      <button
        @click="resetComboBuilder"
        class="w-full rounded-lg border border-gray-300 py-2 text-sm text-gray-700 hover:bg-gray-100"
      >
        🔄 Reset
      </button>
    </div>

    <!-- Results -->
    <div v-if="userSmartCombo.length" class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">
      <h3 class="mb-4 text-base font-semibold text-gray-800 flex items-center gap-2">
        💡 Suggested Picks <span class="text-xs text-gray-400">({{ userSmartCombo.length }} matches)</span>
      </h3>

      <ul class="space-y-4">
        <li
          v-for="match in userSmartCombo"
          :key="match.id"
          class="border-b pb-4 last:border-none"
        >
          <!-- Date + Link -->
          <div class="flex justify-between items-center text-sm text-gray-600">
            <div>🗓 {{ new Date(match.iso_time).toLocaleDateString() }}</div>
            <a
              :href="match.match_url"
              target="_blank"
              class="text-blue-600 hover:underline font-medium"
            >
              View Match →
            </a>
          </div>

          <!-- Teams + Tip -->
          <div class="mt-1 text-sm font-medium text-gray-800">
            👀 {{ match.home_team }} ({{ match.home_rank || '-' }}) vs {{ match.away_team }} ({{ match.away_rank || '-' }})
          </div>
          <div class="mt-1 text-sm">
            🎯 Suggested Tip:
            <strong class="text-indigo-600">{{ match.tip }}</strong>
          </div>

          <!-- Tip Reason -->
          <div class="mt-1 text-xs italic text-gray-500">
            💬 {{ getTipReason(match, comboStrategy) }}
          </div>

          <!-- Avg Goals -->
          <div class="mt-2 text-xs text-gray-700">
            📊 Avg Goals/Game:
            <strong>{{ getAvgGoals(match) }}</strong>
            <span v-if="getAvgGoals(match) >= 2.8" class="ml-2 text-green-600 font-semibold">
              🟢 High Scoring Alert
            </span>
            <span v-else-if="getAvgGoals(match) <= 2.2" class="ml-2 text-red-500 font-semibold">
              🔴 Low Scoring Trend
            </span>
          </div>


        </li>
      </ul>
    </div>
  </div>
</div>



            <!-- Main Content Grid -->
            <div class="grid grid-cols-1 gap-6 lg:grid-cols-4">
                <!-- Left Sidebar - Stats & Filters -->
                <div class="space-y-6 lg:col-span-1">
                    <!-- Filters Card -->
                <!-- Filters Card -->
<div v-if="showFilters" class="rounded-2xl border border-gray-200 bg-gradient-to-br from-white to-gray-50 p-6 shadow-xl transition duration-300 hover:shadow-lg">
    <h3 class="mb-4 flex items-center gap-2 text-lg font-semibold text-gray-800">
        <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5 text-red-500"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
            />
        </svg>
        <span class="font-semibold">Filter Matches</span>
    </h3>

    <div class="space-y-6">
        <!-- Quick Date Shortcuts -->
<div class="flex gap-2 text-sm">
  <button
    @click="setToday"
    class="rounded-md border border-gray-300 bg-white px-3 py-1.5 font-medium text-gray-700 hover:bg-gray-100"
  >
    📅 Today
  </button>
  <button
    @click="setTomorrow"
    class="rounded-md border border-gray-300 bg-white px-3 py-1.5 font-medium text-gray-700 hover:bg-gray-100"
  >
    ⏭️ Tomorrow
  </button>
</div>

        <!-- Date -->
      <!-- Date Range -->
<div class="grid grid-cols-2 gap-3">
  <div>
    <label class="block text-sm font-medium text-gray-700">Start Date</label>
    <input
      type="date"
      v-model="startDateFilter"
      class="w-full rounded-lg border-gray-300 text-sm shadow-sm focus:border-red-500 focus:ring-red-500 transition-all"
    />
  </div>
  <div>
    <label class="block text-sm font-medium text-gray-700">End Date</label>
    <input
      type="date"
      v-model="endDateFilter"
      class="w-full rounded-lg border-gray-300 text-sm shadow-sm focus:border-red-500 focus:ring-red-500 transition-all"
    />
  </div>
</div>


        <!-- Min Confidence -->
        <div>
            <label class="block text-sm font-medium text-gray-700">Min Confidence</label>
            <select
                v-model="minProbability"
                class="w-full rounded-lg border-gray-300 text-sm shadow-sm focus:border-red-500 focus:ring-red-500 transition-all"
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
    <label class="block text-sm font-medium text-gray-700">Team Quality</label>
    <select
        v-model="topTeamsFilter"
        class="w-full rounded-lg border-gray-300 text-sm shadow-sm focus:border-red-500 focus:ring-red-500 transition-all"
    >
        <option value="false">All Teams</option>
        <option value="1">Top 1 Ranked Only</option>
        <option value="2">Top 2 Ranked Only</option>
        <option value="3">Top 3 Ranked Only</option>
        <option value="4">Top 4 Ranked Only</option>
        <option value="5">Top 5 Ranked Only</option>
    </select>
</div>

<!-- Performance Score Filter -->
<div>
    <label class="block text-sm font-medium text-gray-700">Performance Score</label>
    <select
        v-model="performanceScoreFilter"
        class="w-full rounded-lg border-gray-300 text-sm shadow-sm focus:border-red-500 focus:ring-red-500 transition-all"
    >
        <option value="all">All Scores</option>
        <option value="60-75">60% to 75%</option>
        <option value="75-100">75% to 100%</option>
        <option value="below-60">Below 60%</option>
    </select>
</div>

        <!-- Smart Insights (Tag Filter Buttons) -->
        <div>
            <label class="mb-2 block text-sm font-medium text-gray-700">Smart Insights</label>
            <div class="flex flex-wrap gap-2">
                <button
                    v-for="tag in smartTagOptions"
                    :key="tag.label"
                    @click="toggleTagFilter(tag.value)"
                    :class="[
                        'rounded-full border px-3 py-1 text-sm font-medium transition-all',
                        selectedTags.includes(tag.value)
                            ? 'border-red-300 bg-red-100 text-red-700'
                            : 'border-gray-300 bg-white text-gray-600 hover:bg-gray-100',
                    ]"
                >
                    {{ tag.label }}
                </button>
            </div>
        </div>

        <!-- Advanced Filters -->
        <div class="grid grid-cols-1 gap-4 pt-2">
            <div class="flex items-center gap-2">
                <input
                    type="checkbox"
                    v-model="onlyWithOdds"
                    id="onlyWithOdds"
                    class="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                />
                <label for="onlyWithOdds" class="text-sm text-gray-700">💸 Show only matches with odds</label>
            </div>
            <div class="flex items-center gap-2">
                <input
                    type="checkbox"
                    v-model="onlyWithStats"
                    id="onlyWithStats"
                    class="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                />
                <label for="onlyWithStats" class="text-sm text-gray-700">📊 Show only matches with full stats</label>
            </div>
        </div>

        <!-- Odds Range Filter -->
        <div>
            <label class="mb-1 block text-sm font-medium text-gray-700">🎯 Odds Range</label>
            <div class="mb-1 flex justify-between text-xs text-gray-500">
                <span>Min: {{ minOdds }}</span>
                <span>Max: {{ maxOdds }}</span>
            </div>

            <div class="flex items-center gap-2">
                <input
                    type="range"
                    min="1"
                    max="10"
                    step="0.1"
                    v-model.number="minOdds"
                    class="w-1/2 accent-red-500 transition-all"
                />
                <input
                    type="range"
                    min="1"
                    max="10"
                    step="0.1"
                    v-model.number="maxOdds"
                    class="w-1/2 accent-red-500 transition-all"
                />
            </div>

            <div class="mt-1 text-xs text-gray-400">
                Showing picks with odds between <strong>{{ minOdds }}</strong> and <strong>{{ maxOdds }}</strong>
            </div>
        </div>

        <!-- Predicted Result Filter -->
        <div>
            <label class="mb-1 block text-sm font-medium text-gray-700">Result Prediction</label>
            <select
                v-model="pickFilter"
                class="w-full rounded-lg border-gray-300 text-sm shadow-sm focus:border-red-500 focus:ring-red-500 transition-all"
            >
                <option value="">All Results</option>
                <option value="1">🏠 Home Win</option>
                <option value="X">🤝 Draw</option>
                <option value="2">🚗 Away Win</option>
            </select>
        </div>
<!-- Not Started Filter Button -->
<button
    @click="showNotStarted = !showNotStarted"
    class="group flex items-center gap-2 rounded-xl border border-gray-100 bg-gradient-to-br from-white to-gray-50 px-4 py-2.5 shadow-sm transition-all hover:border-red-200 hover:shadow-md"
>
    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500 transition-transform duration-300 group-hover:scale-110" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m2 0a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
    <span class="font-medium text-gray-700">{{ showNotStarted ? 'Show All Matches' : 'Show Not Started Matches' }}</span>
</button>


        <!-- Actions -->
        <div class="mt-6 flex justify-end gap-3">
            <button
                @click="resetFilters"
                class="rounded-lg border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-all"
            >
                Reset
            </button>
            <button
                @click="applyFilters"
                class="rounded-lg bg-red-600 px-4 py-2 text-sm font-medium text-white hover:bg-red-700 transition-all"
            >
                Apply
            </button>
        </div>
    </div>
</div>


                    <!-- Modern Stats Card -->
                    <div
                        class="animate-fade-in-up rounded-2xl border border-gray-100 bg-white p-6 shadow-md transition-all duration-300 hover:shadow-lg"
                    >
                        <h3 class="mb-6 flex items-center gap-2 text-lg font-semibold text-gray-800">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5 text-red-500"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke="currentColor"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    stroke-width="2"
                                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                                />
                            </svg>
                            Today’s Stats
                        </h3>

                        <div class="grid grid-cols-1 gap-4 text-sm sm:grid-cols-2">
                            <!-- Total Matches -->
                            <div class="flex items-center justify-between rounded-lg bg-gray-50 px-3 py-2 transition hover:bg-gray-100">
                                <div class="flex items-center gap-2 font-medium text-gray-700">
                                    <svg class="h-4 w-4 text-red-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            stroke-width="2"
                                            d="M9 12h6m2 0a9 9 0 11-18 0 9 9 0 0118 0z"
                                        />
                                    </svg>
                                    Total Matches
                                </div>
                                <span class="font-semibold text-gray-800">{{ filteredMatches.length }}</span>
                            </div>

                            <!-- High Confidence -->
                            <div class="flex items-center justify-between rounded-lg bg-green-50 px-3 py-2 transition hover:bg-green-100">
                                <div class="flex items-center gap-2 font-medium text-green-700">
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                                    </svg>
                                    High Confidence
                                </div>
                                <span class="font-semibold text-green-800">{{ highConfidenceMatchesCount }} ({{ highConfidencePercentage }}%)</span>
                            </div>

                            <!-- Top Team Matches -->
                            <div class="flex items-center justify-between rounded-lg bg-yellow-50 px-3 py-2 transition hover:bg-yellow-100">
                                <div class="flex items-center gap-2 font-medium text-yellow-700">
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 17l4-4 4 4m0-8l-4 4-4-4" />
                                    </svg>
                                    Top Team Matches
                                </div>
                                <span class="font-semibold text-yellow-800">{{ topTeamMatchesCount }}</span>
                            </div>

                            <!-- Avg Confidence -->
                            <div class="flex items-center justify-between rounded-lg bg-indigo-50 px-3 py-2 transition hover:bg-indigo-100">
                                <div class="flex items-center gap-2 font-medium text-indigo-700">
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            stroke-width="2"
                                            d="M11 11V7a4 4 0 118 0v4m-4 4h-1a4 4 0 100 8h1a4 4 0 100-8z"
                                        />
                                    </svg>
                                    Avg. Confidence
                                </div>
                                <span class="font-semibold text-indigo-800">{{ averageConfidence }}%</span>
                            </div>
                        </div>
                    </div>

                    <!-- Must-Watch Matches -->
                    <div v-if="mustWatchMatches.length" class="mt-6 overflow-hidden rounded-2xl border border-gray-100 bg-white shadow-sm">
                        <!-- Header -->
                        <div class="border-b border-yellow-100 bg-yellow-50 px-6 py-4">
                            <h2 class="flex items-center gap-2 text-lg font-bold text-yellow-800">
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    class="h-5 w-5 text-yellow-500"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                >
                                    <path
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        stroke-width="2"
                                        d="M13 16h-1v-4h-1m0-4h.01M12 20h.01M9 12h.01M15 12h.01M12 8v.01"
                                    />
                                </svg>
                                Must-Watch Matches Today
                            </h2>
                        </div>

                        <!-- Match List -->
                        <div class="divide-y divide-gray-100">
                            <div
                                v-for="match in showAllMustWatch ? mustWatchMatches : mustWatchMatches.slice(0, 4)"
                                :key="match.id"
                                class="grid grid-cols-1 items-center gap-4 px-6 py-3 transition hover:bg-gray-50 sm:grid-cols-12"
                            >
                                <!-- Time -->
                                <div class="col-span-2 text-xs font-medium text-gray-500 sm:text-sm">🕒 {{ match.time_str }}</div>

                                <!-- Teams -->
                                <div class="col-span-6 flex flex-col text-sm font-semibold text-gray-800 sm:flex-row sm:items-center sm:gap-2">
                                    <span
                                        >{{ match.home_team }}
                                        <span v-if="match.home_rank" class="text-xs font-normal text-gray-400">(#{{ match.home_rank }})</span></span
                                    >
                                    <span class="hidden font-normal text-gray-500 sm:inline">vs</span>
                                    <span
                                        >{{ match.away_team }}
                                        <span v-if="match.away_rank" class="text-xs font-normal text-gray-400">(#{{ match.away_rank }})</span></span
                                    >
                                </div>

                                <!-- Prediction -->
                                <div class="col-span-2 text-sm font-medium text-gray-700">
                                    🧠
                                    {{
                                        match.prediction === '1'
                                            ? 'Home Win'
                                            : match.prediction === 'X'
                                              ? 'Draw'
                                              : match.prediction === '2'
                                                ? 'Away Win'
                                                : 'Unknown'
                                    }}
                                </div>

                                <!-- Hot Pick + View -->
                                <div class="col-span-2 flex items-center justify-between gap-2 sm:justify-end">
                                    <span
                                        v-if="getHighestProbability(match) > 60"
                                        class="rounded-full bg-yellow-100 px-2 py-0.5 text-xs font-semibold text-yellow-800"
                                    >
                                        🔥 Hot Pick
                                    </span>
                                    <a :href="match.match_url" target="_blank" class="text-sm text-blue-600 hover:underline"> 👀 View </a>
                                </div>
                            </div>
                        </div>

                        <!-- See More Button -->
                        <div class="border-t border-gray-100 py-4 text-center">
                            <button @click="showAllMustWatch = !showAllMustWatch" class="text-sm font-medium text-yellow-700 hover:underline">
                                {{ showAllMustWatch ? '🔽 Show Less' : '🔼 See More' }}
                            </button>
                        </div>
                    </div>

                    <div ref="adContainer"></div>
                </div>

                <!-- Main Content Area -->
                <div class="space-y-6 lg:col-span-3">
                    <!-- Best Bets Section -->

                    <!-- Loading State -->
                    <div v-if="loading" class="flex items-center justify-center py-20">
                        <div class="flex animate-pulse flex-col items-center gap-4">
                            <div class="h-12 w-12 rounded-full bg-blue-200"></div>
                            <p class="text-gray-500">Loading predictions...</p>
                        </div>
                    </div>

                    <!-- Error State -->
                    <div v-else-if="error" class="rounded-lg border-l-4 border-red-500 bg-red-50 p-4">
                        <div class="flex items-center">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                class="mr-2 h-6 w-6 text-red-500"
                                fill="none"
                                viewBox="0 0 24 24"
                                stroke="currentColor"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    stroke-width="2"
                                    d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                                />
                            </svg>
                            <p class="font-medium text-red-700">{{ error }}</p>
                        </div>
                    </div>

                    <!-- Empty State -->
                    <div v-else-if="filteredMatches.length === 0" class="py-20 text-center">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            class="mx-auto h-16 w-16 text-gray-300"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="1.5"
                                d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                            />
                        </svg>
                        <p class="mt-4 text-lg text-gray-500">No matches found with current filters</p>
                        <button @click="resetFilters" class="mt-4 rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700">
                            Reset Filters
                        </button>
                    </div>

                    <!-- Regular Matches Grid -->
                    <!-- Regular Matches Section -->
                    <div class="mt-10">
                        <!-- Toggle View Button -->
                        <div class="mb-4 flex justify-end">
                            <button
                                @click="tableView = !tableView"
                                class="flex items-center gap-2 rounded-full border border-gray-200 bg-white px-4 py-2 text-sm shadow-sm transition hover:bg-blue-50"
                            >
                                <svg
                                    v-if="tableView"
                                    xmlns="http://www.w3.org/2000/svg"
                                    class="h-4 w-4 text-blue-600"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                >
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16" />
                                </svg>
                                <svg
                                    v-else
                                    xmlns="http://www.w3.org/2000/svg"
                                    class="h-4 w-4 text-blue-600"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                >
                                    <path
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        stroke-width="2"
                                        d="M4 6h7v7H4zM13 6h7v7h-7zM4 17h7v1H4zM13 17h7v1h-7z"
                                    />
                                </svg>
                                <span class="font-medium text-blue-600">{{ tableView ? 'Grid View' : 'Table View' }}</span>
                            </button>
                        </div>

                        <!-- Table View -->
                        <div v-if="tableView" class="overflow-x-auto rounded-xl border border-gray-100 bg-white shadow-sm">
                            <table class="w-full min-w-[1024px] divide-y divide-gray-200 text-sm">
                                <thead class="sticky top-0 z-10 bg-gray-50 text-xs uppercase text-gray-700">
                                    <tr>
                                        <th class="whitespace-nowrap px-4 py-3 text-left">Time</th>
                                        <th class="whitespace-nowrap px-4 py-3 text-left">Game</th>
                                        <th class="whitespace-nowrap px-4 py-3 text-left">Pick</th>
                                        <th class="whitespace-nowrap px-4 py-3 text-center">1</th>
                                        <th class="whitespace-nowrap px-4 py-3 text-center">X</th>
                                        <th class="whitespace-nowrap px-4 py-3 text-center">2</th>
                                        <th class="whitespace-nowrap px-4 py-3 text-center">Odds</th>
                                        <th class="whitespace-nowrap px-4 py-3 text-center">Rank</th>
                                        <th class="whitespace-nowrap px-4 py-3 text-right">Action</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-gray-100">
                                    <tr v-for="match in paginatedMatchess" :key="match.id" class="transition hover:bg-blue-50/40">
  <td class="whitespace-nowrap px-4 py-2">
    {{ match.time_str }}
    <div class="mt-3 flex flex-wrap gap-2" v-if="getMatchTags(match).length">
      <span
        v-for="tag in getMatchTags(match)"
        :key="tag"
        class="rounded-full px-3 py-1 text-xs font-medium"
        :class="{
          'bg-green-100 text-green-800': tag.includes('Confidence'),
          'bg-blue-100 text-blue-800': tag.includes('Momentum') || tag.includes('Scorer'),
          'bg-orange-100 text-orange-800': tag.includes('Upset') || tag.includes('Streak'),
          'bg-red-100 text-red-800': tag.includes('Poor Form'),
          'bg-yellow-100 text-yellow-800': tag.includes('Over') || tag.includes('Safe'),
          'bg-gray-100 text-gray-800': true,
        }"
      >
        {{ tag }}
      </span>
    </div>
  </td>

  <!-- Game Column: Teams + Stats -->
  <td class="px-4 py-2">
    <div class="font-medium text-gray-800">
      {{ match.home_team }} <span class="text-gray-400">vs</span> {{ match.away_team }}
    </div>

    <div class="mt-2 grid grid-cols-1 gap-2 text-[11px] text-gray-700 md:grid-cols-2">
      <!-- Home Stats -->
      <div class="rounded-md bg-green-50 p-2">
        <strong class="mb-1 block text-[12px] text-green-700">🏠 Home Stats</strong>
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
      <div class="rounded-md bg-blue-50 p-2">
        <strong class="mb-1 block text-[12px] text-blue-700">🚗 Away Stats</strong>
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

    <!-- Performance Score -->
    <div class="mt-3 text-xs text-gray-600">
      🧮 H/A Score:
      <span
        :class="{
          'text-green-600 font-semibold': getHomeAwayPerformanceScore(match) >= 75,
          'text-yellow-600 font-medium': getHomeAwayPerformanceScore(match) >= 60 && getHomeAwayPerformanceScore(match) < 75,
          'text-red-600': getHomeAwayPerformanceScore(match) < 60
        }"
      >
        {{ getHomeAwayPerformanceScore(match) }}%
      </span>
    </div>
  </td>

  <!-- Pick -->
  <td class="px-4 py-2">
    <span
      class="rounded-full px-2 py-1 text-xs font-semibold"
      :class="{
        'bg-green-100 text-green-800': match.prediction === '1',
        'bg-yellow-100 text-yellow-800': match.prediction === 'X',
        'bg-red-100 text-red-800': match.prediction === '2',
      }"
    >
      {{ match.prediction }}
    </span>
  </td>

  <!-- Probabilities -->
  <td class="whitespace-nowrap px-2 py-2 text-center text-xs">{{ match.prob_1 }}%</td>
  <td class="whitespace-nowrap px-2 py-2 text-center text-xs">{{ match.prob_x }}%</td>
  <td class="whitespace-nowrap px-2 py-2 text-center text-xs">{{ match.prob_2 }}%</td>

  <!-- Odds -->
  <td class="whitespace-nowrap px-2 py-2 text-center text-xs">
    <span v-if="match.live_odds" class="rounded-full bg-indigo-100 px-2 py-0.5 font-medium text-indigo-700">
      {{ match.live_odds }}
    </span>
  </td>

  <!-- Rank -->
  <td class="whitespace-nowrap px-4 py-2 text-center text-xs">
    <div class="flex flex-col items-center text-gray-500">
      <span>🏠 {{ match.home_rank || '-' }}</span>
      <span>🚗 {{ match.away_rank || '-' }}</span>
    </div>
  </td>

  <!-- Action -->
  <td class="whitespace-nowrap px-4 py-2 text-right">
    <a :href="match.match_url" target="_blank" class="text-xs font-medium text-blue-600 hover:underline">
      Details ?
    </a>
  </td>
</tr>

                                </tbody>
                            </table>

                            <!-- Pagination -->
                            <div v-if="hasMorePagess" class="p-4 text-center">
                                <button @click="loadMores" class="rounded-lg bg-blue-600 px-4 py-2 text-sm text-white transition hover:bg-blue-700">
                                    See More Matches ?
                                </button>
                            </div>
                        </div>

                        <!-- Grid View -->
                        <div v-else class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
                            <div
                                v-for="match in paginatedMatchess"
                                :key="match.id"
                                class="transform overflow-hidden rounded-xl border border-gray-200 bg-white shadow-lg transition-all hover:scale-105 hover:shadow-xl"
                            >
                                <div class="p-5">
                                    <!-- Header: Match Teams & Prediction -->
                                    <div class="mb-4 flex items-start justify-between">
                                        <div>
                                            <h3 class="text-lg font-bold text-gray-800">{{ match.home_team }} vs {{ match.away_team }}</h3>
                                            <p class="mt-1 text-sm text-gray-500">{{ match.time_str }}</p>
                                        </div>
                                        <span
                                            class="rounded-full px-3 py-1 text-xs font-bold"
                                            :class="{
                                                'bg-green-100 text-green-800': match.prediction === '1',
                                                'bg-yellow-100 text-yellow-800': match.prediction === 'X',
                                                'bg-red-100 text-red-800': match.prediction === '2',
                                            }"
                                        >
                                            {{ match.prediction }}
                                        </span>
                                    </div>

                                    <!-- Probabilities -->
                                    <div class="mt-4 flex justify-between text-sm text-gray-600">
                                        <div class="flex-1 text-center">
                                            <div class="font-semibold text-blue-600">1</div>
                                            <div>{{ match.prob_1 }}%</div>
                                        </div>
                                        <div class="flex-1 text-center">
                                            <div class="font-semibold text-yellow-600">X</div>
                                            <div>{{ match.prob_x }}%</div>
                                        </div>
                                        <div class="flex-1 text-center">
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
<!-- Home/Away Score -->
<div class="mt-3 text-sm text-center text-gray-600">
  <div class="flex justify-center items-center gap-2">
    <span class="text-xl font-semibold text-gray-700">🧮 H/A Score:</span>
    <span
      :class="{
        'text-green-600 font-bold': getHomeAwayPerformanceScore(match) >= 75,
        'text-yellow-600 font-semibold': getHomeAwayPerformanceScore(match) >= 60 && getHomeAwayPerformanceScore(match) < 75,
        'text-red-600 font-semibold': getHomeAwayPerformanceScore(match) < 60
      }"
      class="text-2xl"
    >
      {{ getHomeAwayPerformanceScore(match) }}%
    </span>
  </div>

  <!-- Home and Away Win Rates -->
  <div class="mt-4 text-sm text-gray-700 space-y-2">
    <div class="flex justify-between">
      <span class="flex items-center gap-2 font-medium">
        <span class="text-green-500">🏠</span>
        Home Win Rate:
      </span>
      <span class="font-semibold">{{ getHomeWinRate(match) }}%</span>
    </div>
    <div class="flex justify-between">
      <span class="flex items-center gap-2 font-medium">
        <span class="text-blue-500">🚗</span>
        Away Win Rate:
      </span>
      <span class="font-semibold">{{ getAwayWinRate(match) }}%</span>
    </div>
    <div class="flex justify-between">
      <span class="flex items-center gap-2 font-medium">
        <span class="text-red-500">⚠️</span>
        Away Loss Rate:
      </span>
      <span class="font-semibold">{{ getAwayLossRate(match) }}%</span>
    </div>
  </div>
</div>



                                    <!-- Live Odds -->
                                    <span v-if="match.live_odds" class="mt-2 rounded-full bg-indigo-100 px-3 py-1 font-medium text-indigo-700">
                                        💸 {{ match.live_odds }}
                                    </span>

                                    <!-- Extra Tags (GG, Over 2.5, Safe Pick, etc) -->
                                    <div class="mt-4 flex flex-wrap gap-2" v-if="getMatchTags(match).length">
                                        <span
                                           v-for="tag in getMatchTags(match)"
                                            :key="tag"
                                            class="rounded-full px-3 py-1 text-xs font-medium"
                                            :class="{
                                                'bg-green-100 text-green-800': tag.includes('Confidence'),
                                                'bg-blue-100 text-blue-800': tag.includes('Momentum') || tag.includes('Scorer'),
                                                'bg-orange-100 text-orange-800': tag.includes('Upset') || tag.includes('Streak'),
                                                'bg-red-100 text-red-800': tag.includes('Poor Form'),
                                                'bg-yellow-100 text-yellow-800': tag.includes('Over') || tag.includes('Safe'),
                                                'bg-gray-100 text-gray-800': true,
                                            }"
                                        >
                                            {{ tag }}
                                        </span>
                                    </div>

                                    <!-- Enhanced Stats -->
                                    <div class="mt-4 grid grid-cols-2 gap-4 text-xs text-gray-700">
    <!-- Home Stats -->
    <div class="rounded-md bg-green-50 p-3">
        <strong class="mb-1 block text-green-700">🏠 Home Stats</strong>
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
    <div class="rounded-md bg-blue-50 p-3">
        <strong class="mb-1 block text-blue-700">🚗 Away Stats</strong>
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
                                <a
                                    :href="match.match_url"
                                    target="_blank"
                                    class="block bg-gray-50 py-2 text-center text-xs font-medium text-blue-600 hover:underline"
                                >
                                    View Details ?
                                </a>
                            </div>

                            <!-- See More (Grid version) -->
                            <div v-if="hasMorePagess" class="col-span-full p-4 text-center">
                                <button @click="loadMores" class="rounded-lg bg-blue-600 px-4 py-2 text-sm text-white transition hover:bg-blue-700">
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
        class="animate-fade-in fixed bottom-4 right-4 flex items-center gap-2 rounded-full border border-gray-200 bg-white/80 px-4 py-1.5 text-sm font-medium text-gray-600 shadow-md backdrop-blur-sm"
    >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-red-500" viewBox="0 0 24 24" fill="currentColor">
            <path
                d="M12 22c5.52 0 10-4.48 10-10S17.52 2 12 2 2 6.48 2 12s4.48 10 10 10zm0-1.5c-4.69 0-8.5-3.81-8.5-8.5S7.31 3.5 12 3.5 20.5 7.31 20.5 12 16.69 20.5 12 20.5z"
            />
            <path d="M10.25 15h1.5V9h-1.5v6zm0 2h1.5v-1.5h-1.5V17z" />
        </svg>
        Mahmoud Bouhlel © {{ new Date().getFullYear() }}
    </footer>
</template>

<script setup>
import axios from 'axios';
import { computed, onMounted, ref } from 'vue';

// State
const matches = ref([]);
const loading = ref(true);
const error = ref(null);
const showFilters = ref(false);
const showAllMustWatch = ref(false);
const tableView = ref(false);
const currentPage = ref(1);
const rowsPerPage = 50;
const page = ref(1);
const perPage = 50;
const tagFilter = ref('');
const onlyWithOdds = ref(false);
const onlyWithStats = ref(false);
const showComboModal = ref(false);
const comboStrategy = ref('best');
const comboStartDate = ref('');
const comboEndDate = ref('');
const comboMatchCount = ref(5);
const userSmartCombo = ref([]);
const minOdds = ref('');
const maxOdds = ref('');
const matchTimeFrom = ref('');
const matchTimeTo = ref('');
const HWR_WEIGHT = 0.4;   // Weight of home win rate
const HGS_WEIGHT = 0.3;   // Weight of home goals scored
const ALR_WEIGHT = 0.2;   // Weight of away loss rate
const GD_WEIGHT = 0.1;    // Weight of goal difference
const performanceScoreFilter = ref('all'); // Default to 'all'
const showNotStarted = ref(false); // to toggle between showing all or not started matches


// Function to calculate Home Win Rate
function getHomeWinRate(match) {
  if (!match.home_gp) return 0; // Prevent division by 0
  return ((match.home_w / match.home_gp) * 100).toFixed(1); // Return percentage with 1 decimal place
}

// Function to calculate Away Win Rate
function getAwayWinRate(match) {
  if (!match.away_gp) return 0; // Prevent division by 0
  return ((match.away_w / match.away_gp) * 100).toFixed(1); // Return percentage with 1 decimal place
}

// Function to calculate Away Loss Rate (ALR)
function getAwayLossRate(match) {
  if (!match.away_gp) return 0; // Prevent division by 0
  return ((match.away_l / match.away_gp) * 100).toFixed(1); // Return percentage with 1 decimal place
}


// Home vs Away Model
function calculateHomeAdvantageScore(homeStats, awayStats) {
  const homeWinRate = (homeStats.W / homeStats.GP) * 100;
  const homeGoalsScored = homeStats.GF / homeStats.GP;
  const awayLossRate = (awayStats.L / awayStats.GP) * 100;
  const awayGoalsConceded = awayStats.GA / awayStats.GP;
  const goalDifference = homeStats.GD - awayStats.GD;

  // Calculate total home advantage score
  const score =
    (homeWinRate * HWR_WEIGHT) +
    (homeGoalsScored * HGS_WEIGHT) -
    (awayLossRate * ALR_WEIGHT) -
    (awayGoalsConceded * ALR_WEIGHT) +  // More goals conceded away = worse
    (goalDifference * GD_WEIGHT);       // Better goal difference = better performance

  return score;
}



const generateUserCombo = () => {
  const start = comboStartDate.value ? new Date(comboStartDate.value) : null;
  const end = comboEndDate.value ? new Date(comboEndDate.value) : null;

  let filtered = [...filteredMatches.value].filter((m) => {
    const matchDate = new Date(m.iso_time);
    if (start && matchDate < start) return false;
    if (end && matchDate > end) return false;
    return true;
  });

  const hGF = (m) => m.home_gf || 0;
  const aGF = (m) => m.away_gf || 0;
  const hGA = (m) => m.home_ga || 0;
  const aGA = (m) => m.away_ga || 0;
  const rankGap = (m) => Math.abs((m.home_rank || 0) - (m.away_rank || 0));
  const prob = (m) => getHighestProbability(m);
  const totalGF = (m) => hGF(m) + aGF(m);
  const prediction = (m) => getPredictionType(m);

  switch (comboStrategy.value) {
    case 'smart_over':
      filtered = filtered
        .filter((m) => totalGF(m) > 50 || (hGF(m) > 30 && aGF(m) > 20))
        .map((m) => {
          let tip = 'Over 2.5';
          if (totalGF(m) > 70) tip = 'Over 3.5';
          else if (totalGF(m) > 55) tip = 'Over 2.5';
          else tip = 'Over 1.5';
          return { ...m, tip };
        });
      break;

    case 'smart_under':
      filtered = filtered
        .filter((m) => totalGF(m) < 20 && hGF(m) < 15 && aGF(m) < 15)
        .map((m) => ({
          ...m,
          tip: totalGF(m) < 10 ? 'Under 1.5' : 'Under 2.5',
        }));
      break;

    case 'btts_focus':
      filtered = filtered
        .filter((m) => hGF(m) > 25 && aGF(m) > 25 && hGA(m) > 20 && aGA(m) > 20)
        .map((m) => ({ ...m, tip: 'BTTS' }));
      break;

    case 'draw_focus':
      filtered = filtered
        .filter((m) => rankGap(m) <= 2 && Math.abs(m.prob_1 - m.prob_2) <= 10)
        .map((m) => ({ ...m, tip: 'Draw' }));
      break;

    case 'safe_combo':
      filtered = filtered
        .filter((m) => prob(m) >= 70 && rankGap(m) >= 5)
        .map((m) => ({
          ...m,
          tip: prediction(m) === 'Draw' ? 'Double Chance' : `${prediction(m)} - Safe`,
        }));
      break;

    case 'home_over':
      filtered = filtered
        .filter((m) => hGF(m) > 30 && aGA(m) > 25)
        .map((m) => ({
          ...m,
          tip: 'Home Over 2.5',
        }));
      break;

    case 'away_over':
      filtered = filtered
        .filter((m) => aGF(m) > 30 && hGA(m) > 25)
        .map((m) => ({
          ...m,
          tip: 'Away Over 2.5',
        }));
      break;

    case 'home_under':
      filtered = filtered
        .filter((m) => hGF(m) < 15 && aGA(m) < 15)
        .map((m) => ({
          ...m,
          tip: 'Home Under 2.5',
        }));
      break;

    case 'away_under':
      filtered = filtered
        .filter((m) => aGF(m) < 15 && hGA(m) < 15)
        .map((m) => ({
          ...m,
          tip: 'Away Under 2.5',
        }));
      break;

    case 'mixed':
      filtered = filtered.map((m, i) => {
        const tags = getMatchTags(m);
        let tip = prediction(m);
        if (tags.includes('🎯 Over 2.5 Goals')) tip = 'Over 2.5';
        if (tags.includes('🎯 Consistent Scorer')) tip = 'BTTS';
        if (i % 3 === 0) tip = 'Over 1.5';
        if (i % 4 === 0) tip = 'Draw';
        return { ...m, tip };
      });
      break;

    case 'goals':
      filtered = filtered
        .filter((m) => totalGF(m) > 60)
        .map((m) => ({ ...m, tip: 'Over 2.5 Goals' }));
      break;

    case 'super_combo':
      // Mix of Over, BTTS, 1X2, Safe
      filtered = filtered
        .filter((m) => prob(m) > 60 || totalGF(m) > 50)
        .map((m, i) => {
          const p = prediction(m);
          if (i % 2 === 0 && totalGF(m) > 60) return { ...m, tip: 'Over 2.5' };
          if (i % 3 === 0) return { ...m, tip: 'BTTS' };
          if (i % 4 === 0) return { ...m, tip: 'Draw' };
          if (prob(m) > 70 && rankGap(m) > 5) return { ...m, tip: `${p} - Safe` };
          return { ...m, tip: p };
        });
      break;

    default:
      // Fallback to "best"
      filtered = filtered
        .filter((m) => prob(m) > 60)
        .sort((a, b) => prob(b) - prob(a))
        .map((m) => ({
          ...m,
          tip: prediction(m),
        }));
      break;
  }

  // If no results, fallback to top confidence
  if (filtered.length === 0) {
    filtered = [...filteredMatches.value]
      .filter((m) => prob(m) > 60)
      .sort((a, b) => prob(b) - prob(a))
      .map((m) => ({
        ...m,
        tip: prediction(m),
      }));
  }

  userSmartCombo.value = filtered.slice(0, comboMatchCount.value);
};


function getTipReason(match, type = 'best') {
    const highestProb = getHighestProbability(match);
    const goalSum = (match.home_gf || 0) + (match.away_gf || 0);
    const rankGap = Math.abs((match.home_rank || 0) - (match.away_rank || 0));

    if (type === 'best') {
        if (highestProb >= 75) return 'High confidence from model ';
        if (highestProb >= 65) return 'Consistent team + strong form';
        return 'Good value based on ranking and stats';
    }

    if (type === 'goals') {
        if (goalSum >= 70) return 'Both teams average high goals';
        if (match.home_gf >= 35 && match.away_gf >= 30) return 'Strong attack on both sides';
        return 'Scoring trend detected in last 5 games';
    }

    if (type === 'mixed') {
        const tags = getMatchTags(match);
        if (tags.includes('🎯 Over 2.5 Goals')) return 'Over trend supported by team GF stats';
        if (tags.includes('🎯 Consistent Scorer')) return 'Scoring form: one side scores regularly';
        if (tags.includes('🛡️ Safe Pick')) return 'Wide point gap: safe pick scenario';
        if (tags.includes('😮 Upset Alert')) return 'Low-ranked team could surprise';
        return 'Smart logic based on combined tags';
    }

    return 'Based on model prediction and smart filters';
}

const selectedTags = ref([]);
const smartTagOptions = [
    { label: '📉 Home Negative GD', value: 'home_negative_gd' },
{ label: '📉 Away Negative GD', value: 'away_negative_gd' },
{ label: '📉 Both Teams Negative GD', value: 'both_negative_gd' },


    { label: '🎯 Consistent Scorer', value: 'scorer' },
    { label: '🔥 Streak Team', value: 'streak' },
    { label: '⚡ Attacking Momentum', value: 'momentum' },
    { label: '😮 Upset Alert', value: 'upset' },
];
// Tag filter
if (tagFilter.value) {
    result = result.filter((match) => {
        const tags = getMatchTags(match);
        return tags.some((tag) => tag.toLowerCase().includes(tagFilter.value.toLowerCase()));
    });
}
// Odds Range filter
// Odds Range filter
if (minOdds.value || maxOdds.value) {
  const min = parseFloat(minOdds.value) || 0;
  const max = parseFloat(maxOdds.value) || Infinity;

  result = result.filter((match) => {
    const odds = parseFloat(match.live_odds);
    return !isNaN(odds) && odds >= min && odds <= max;
  });
}


const adContainer = ref(null);

const paginatedMatchess = computed(() => {
    return filteredMatches.value.slice(0, page.value * perPage);
});

const hasMorePagess = computed(() => {
    return filteredMatches.value.length > paginatedMatchess.value.length;
});

const loadMores = () => {
    page.value++;
};


// Filters
const todayISODate = new Date().toISOString().split('T')[0];

const dateFilter = ref(todayISODate);
const startDateFilter = ref(todayISODate);
const endDateFilter = ref(todayISODate);
const minProbability = ref('0');
const leagueFilter = ref('');
const topTeamsFilter = ref('false');
const sortOption = ref('highest-prob');
const timeFilter = ref('');
const pickFilter = ref('');

// Sample data to ensure matches show up
const sampleMatches = [

];

const mustWatchMatches = computed(() =>
    filteredMatches.value
        .filter((m) => {
            const home = Number(m.home_rank);
            const away = Number(m.away_rank);
            const highestProb = getHighestProbability(m);
            const goalSum = (m.home_gf || 0) + (m.away_gf || 0);
            const rankDiff = Math.abs(home - away);

            // Must meet one of these 3:
            return (
                // 1. 🔥 Big Rank Clash (like 1st vs 2nd or 3rd)
                (home <= 3 && away <= 3) ||
                // 2. 😮 Potential Upset (top team vs rank >10)
                (((home <= 3 && away >= 10) || (away <= 3 && home >= 10)) && highestProb < 70) ||
                // 3. 🎯 High Scoring Drama
                (goalSum > 60 && rankDiff <= 5)
            );
        })
        // Rank by confidence *and* tightness of match
        .sort((a, b) => {
            const aScore = getHighestProbability(a) - Math.abs(a.home_rank - a.away_rank);
            const bScore = getHighestProbability(b) - Math.abs(b.home_rank - b.away_rank);
            return bScore - aScore;
        })
        .slice(0, 10),
);
const resetComboBuilder = () => {
  comboStartDate.value = '';
  comboEndDate.value = '';
  comboMatchCount.value = 5;
  comboStrategy.value = 'best';
  userSmartCombo.value = [];

  // Optionally scroll back to top of modal or focus UI
  setTimeout(() => {
    const modal = document.querySelector('.smart-combo-modal');
    if (modal) modal.scrollTop = 0;
  }, 100);
};

const paginatedMatches = computed(() => {
    const start = (currentPage.value - 1) * rowsPerPage;
    const end = start + rowsPerPage;
    return filteredMatches.value.slice(start, end);
});

const hasMorePages = computed(() => {
    return filteredMatches.value.length > currentPage.value * rowsPerPage;
});

const loadMore = () => {
    currentPage.value++;
};

// Computed: Stats
const highConfidenceMatchesCount = computed(() => {
    return filteredMatches.value.filter((match) => match.prob_1 >= 70 || match.prob_x >= 70 || match.prob_2 >= 70).length;
});

const highConfidencePercentage = computed(() => {
    if (filteredMatches.value.length === 0) return 0;
    return Math.round((highConfidenceMatchesCount.value / filteredMatches.value.length) * 100);
});

const topTeamMatchesCount = computed(() => {
    return filteredMatches.value.filter((match) => isTopRanked(match.home_rank) || isTopRanked(match.away_rank)).length;
});

const averageConfidence = computed(() => {
    if (filteredMatches.value.length === 0) return 0;

    const total = filteredMatches.value.reduce((sum, match) => {
        return sum + Math.max(match.prob_1, match.prob_x, match.prob_2);
    }, 0);

    return Math.round(total / filteredMatches.value.length);
});

// Computed: Filtered Matches
const filteredMatches = computed(() => {
    let result = [...matches.value];

    // Filter by odds
    if (onlyWithOdds.value) {
        result = result.filter((match) => !!match.live_odds && match.live_odds !== '-' && match.live_odds !== '');
    }
// Result Prediction (1/X/2) filter
if (pickFilter.value) {
  result = result.filter((match) => match.prediction === pickFilter.value);
}


    // Filter by stats (basic check: has GP + PTS for both sides)
    if (onlyWithStats.value) {
        result = result.filter((match) => match.home_gp && match.away_gp && match.home_pts && match.away_pts);
    }

    if (startDateFilter.value || endDateFilter.value) {
  const start = startDateFilter.value ? new Date(startDateFilter.value) : null;
  const end = endDateFilter.value ? new Date(endDateFilter.value) : null;

  result = result.filter((match) => {
    const matchDate = new Date(match.iso_time);
    if (start && matchDate < start) return false;
    if (end && matchDate > end) return false;
    return true;
  });
}


    if (matchTimeFrom.value && matchTimeTo.value) {
  const [startHour, startMinute] = matchTimeFrom.value.split(':').map(Number);
  const [endHour, endMinute] = matchTimeTo.value.split(':').map(Number);

  result = result.filter((match) => {
    if (!match.time_str) return false;
    const [matchHour, matchMinute] = match.time_str.split(':').map(Number);

    const matchTime = matchHour * 60 + matchMinute;
    const startTime = startHour * 60 + startMinute;
    const endTime = endHour * 60 + endMinute;

    return matchTime >= startTime && matchTime <= endTime;
  });
}

   if (performanceScoreFilter.value !== 'all') {
        result = result.filter((match) => {
            const performanceScore = getHomeAwayPerformanceScore(match);

            // Filter based on selected score ranges
            if (performanceScoreFilter.value === '60-75') {
                return performanceScore >= 60 && performanceScore < 75;
            } else if (performanceScoreFilter.value === '75-100') {
                return performanceScore >= 75 && performanceScore <= 100;
            } else if (performanceScoreFilter.value === 'below-60') {
                return performanceScore < 60;
            }
            return true; // If filter is "all", return all
        });
    }


    // Filter for matches that have not started yet
    if (showNotStarted.value) {
        const now = new Date(); // Get the current date and time

        result = result.filter((match) => {
            // Parse match.time_str (DD/MM/YYYY HH:MM) to a Date object
            const [day, month, yearAndTime] = match.time_str.split('/'); // Split the day, month, year+time
            const [year, time] = yearAndTime.split(' '); // Split the year and time
            const [hour, minute] = time.split(':'); // Split the time into hour and minute

            // Create a new Date object using the parsed parts
            const matchDate = new Date(`${month}/${day}/${year} ${hour}:${minute}`);

            return matchDate > now; // Only include matches that are in the future
        });
        result.sort((a, b) => {
  const [dayA, monthA, yearAndTimeA] = a.time_str.split('/');
  const [yearA, timeA] = yearAndTimeA.split(' ');
  const [hourA, minuteA] = timeA.split(':');
  const dateA = new Date(`${monthA}/${dayA}/${yearA} ${hourA}:${minuteA}`);

  const [dayB, monthB, yearAndTimeB] = b.time_str.split('/');
  const [yearB, timeB] = yearAndTimeB.split(' ');
  const [hourB, minuteB] = timeB.split(':');
  const dateB = new Date(`${monthB}/${dayB}/${yearB} ${hourB}:${minuteB}`);

  return dateA - dateB;
});

    }
    // Time of Day filter
    if (timeFilter.value) {
        result = result.filter((match) => {
            if (!match.time_str) return false;
            const [hours] = match.time_str.split(':').map(Number);
            if (timeFilter.value === 'morning') return hours >= 0 && hours < 12;
            if (timeFilter.value === 'afternoon') return hours >= 12 && hours < 18;
            if (timeFilter.value === 'evening') return hours >= 18 && hours <= 23;
            return true;
        });
    }
    if (selectedTags.value.length > 0) {
        result = result.filter((match) => {
            const tags = getMatchTags(match);
            return selectedTags.value.every((tag) => tags.some((t) => t.toLowerCase().includes(tag)));
        });
    }
    if (selectedTags.value.includes('negative_gd')) {
    result = result.filter((match) => {
        return (match.home_gd < 0 || match.away_gd < 0);
    });
}

    // Odds Range filter (inside filteredMatches computed!)
if (minOdds.value || maxOdds.value) {
    const min = parseFloat(minOdds.value) || 0;
    const max = parseFloat(maxOdds.value) || Infinity;

    result = result.filter((match) => {
        const odds = parseFloat(match.live_odds);
        return !isNaN(odds) && odds >= min && odds <= max;
    });
}

    // Min probability filter
    if (minProbability.value > 0) {
        const minProb = Number(minProbability.value);
        result = result.filter((match) => match.prob_1 >= minProb || match.prob_x >= minProb || match.prob_2 >= minProb);
    }

    // League filter
    if (leagueFilter.value) {
        result = result.filter((match) => match.league === leagueFilter.value);
    }

   // Top teams filter
if (topTeamsFilter.value !== 'false') {
    const maxRank = parseInt(topTeamsFilter.value);  // Get the selected rank (1 to 5)

    result = result.filter((match) => {
        return (isTopRanked(match.home_rank, maxRank) || isTopRanked(match.away_rank, maxRank));
    });
}


    // Apply sorting
    if (sortOption.value === 'highest-prob') {
        result.sort((a, b) => {
            const aMax = Math.max(a.prob_1, a.prob_x, a.prob_2);
            const bMax = Math.max(b.prob_1, b.prob_x, b.prob_2);
            return bMax - aMax;
        });
    } else if (sortOption.value === 'time') {
        result.sort((a, b) => new Date(a.iso_time) - new Date(b.iso_time));
    } else if (sortOption.value === 'league') {
        result.sort((a, b) => a.league.localeCompare(b.league));
    }

    return result;
});
const onlineUsers = ref(0);
function setToday() {
  const today = new Date().toISOString().split('T')[0];
  startDateFilter.value = today;
  endDateFilter.value = today;
}

function setTomorrow() {
  const tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1);
  const isoTomorrow = tomorrow.toISOString().split('T')[0];
  startDateFilter.value = isoTomorrow;
  endDateFilter.value = isoTomorrow;
}

onMounted(() => {
    // Simulate random active users
    onlineUsers.value = Math.floor(20 + Math.random() * 100);

    // Optional: update every 30 seconds
    setInterval(() => {
        onlineUsers.value = Math.floor(20 + Math.random() * 100);
    }, 30000);
});

// Computed: Best Bets
const bestBets = computed(() => {
    if (filteredMatches.value.length === 0) return [];

    const highProbMatches = filteredMatches.value.filter((match) => match.prob_1 > 70 || match.prob_x > 70 || match.prob_2 > 70);

    return highProbMatches
        .sort((a, b) => {
            const aMax = Math.max(a.prob_1, a.prob_x, a.prob_2);
            const bMax = Math.max(b.prob_1, b.prob_x, b.prob_2);
            return bMax - aMax;
        })
        .slice(0, 3);
});
function getAvgGoals(match) {
  const hGF = parseFloat(match.home_gf) || 0;
  const hGA = parseFloat(match.home_ga) || 0;
  const aGF = parseFloat(match.away_gf) || 0;
  const aGA = parseFloat(match.away_ga) || 0;
  const hGP = parseFloat(match.home_gp) || 0;
  const aGP = parseFloat(match.away_gp) || 0;

  const totalGoals = hGF + hGA + aGF + aGA;
  const totalGames = hGP + aGP;

  if (totalGames === 0) return 0; // fallback to 0 if no data

  return +(totalGoals / totalGames).toFixed(2);
}
function getFormTrend(match, side = 'home') {
  const w = parseInt(match[`${side}_w`] || 0);
  const d = parseInt(match[`${side}_d`] || 0);
  const l = parseInt(match[`${side}_l`] || 0);

  const trend = [];
  for (let i = 0; i < w; i++) trend.push('✅');
  for (let i = 0; i < d; i++) trend.push('➖');
  for (let i = 0; i < l; i++) trend.push('❌');

  return trend.slice(0, 5).join(' / ');
}


// Combo Builder State
// Combo Builder State
const comboRisk = ref('conservative');
const comboSize = ref(3);
const smartCombo = ref([]);
const homeRankLimit = ref(10);
const awayRankLimit = ref(10);

const generateSmartCombo = () => {
    const threshold = {
        conservative: 70,
        balanced: 60,
        risky: 50,
    }[comboRisk.value];

    const eligible = filteredMatches.value.filter((match) => {
        const prob = getHighestProbability(match);
        const homeValid = !match.home_rank || match.home_rank <= homeRankLimit.value;
        const awayValid = !match.away_rank || match.away_rank <= awayRankLimit.value;
        return prob >= threshold && homeValid && awayValid;
    });

    const sorted = eligible.sort((a, b) => getHighestProbability(b) - getHighestProbability(a));
    smartCombo.value = sorted.slice(0, comboSize.value);
};

// Combo stats
const comboConfidence = computed(() => {
    if (!smartCombo.value.length) return 0;
    const probs = smartCombo.value.map((m) => getHighestProbability(m) / 100);
    return Math.round(probs.reduce((acc, p) => acc * p, 1) * 100);
});
function getHomeAwayPerformanceScore(match) {
  const homeWinRate = (match.home_w / match.home_gp) || 0;
  const awayLossRate = (match.away_l / match.away_gp) || 0;
  const homeGF = match.home_gf / match.home_gp || 0;
  const awayGA = match.away_ga / match.away_gp || 0;

  const score = homeWinRate * 0.4 + (homeGF / 3) * 0.3 + awayLossRate * 0.2 + (awayGA / 2.5) * 0.1;

  return Math.round(score * 100); // Return score as percentage
}

const estimatedComboReturn = computed(() => {
    if (!smartCombo.value.length) return 0;
    const odds = smartCombo.value.map((m) => 100 / getHighestProbability(m));
    return odds.reduce((acc, o) => acc * o, 1).toFixed(2);
});

const top5Today = computed(() => {
    return bestBets.value
        .filter((match) => match.iso_time.startsWith(todayISODate)) // only today's matches
        .slice(0, 5);
});

// Utils
function isTopRanked(rank, maxRank) {
    return rank <= maxRank;
}

const getHighestProbability = (match) => {
    return Math.max(match.prob_1, match.prob_x, match.prob_2);
};

const getPredictionType = (match) => {
    const maxProb = getHighestProbability(match);
    if (maxProb === match.prob_1) return 'Home Win';
    if (maxProb === match.prob_x) return 'Draw';
    return 'Away Win';
};

const formatDate = (dateString) => {
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
};

// Sorting
const applySorting = () => {
    // Sorting is now handled in the filteredMatches computed property
};

// Filters actions
const applyFilters = () => {
    showFilters.value = false;
};

const resetFilters = () => {
    dateFilter.value = '';
    minProbability.value = '0';
    leagueFilter.value = '';
    topTeamsFilter.value = 'false';
    sortOption.value = 'highest-prob';
    timeFilter.value = '';
    minOdds.value = '';       // 👈 Reset min odds
    maxOdds.value = '';       // 👈 Reset max odds
    selectedTags.value = [];  // Optional: reset tag filters
};
function getMatchTags(match) {
    const tags = [];

    const hGF = parseInt(match.home_gf || 0);
    const hGA = parseInt(match.home_ga || 0);
    const aGF = parseInt(match.away_gf || 0);
    const aGA = parseInt(match.away_ga || 0);
    const hW = parseInt(match.home_w || 0);
    const hL = parseInt(match.home_l || 0);
    const aW = parseInt(match.away_w || 0);
    const aL = parseInt(match.away_l || 0);
    const hPts = parseInt(match.home_pts || 0);
    const aPts = parseInt(match.away_pts || 0);
    const homeRank = parseInt(match.home_rank || 0);
    const awayRank = parseInt(match.away_rank || 0);

    const totalGF = hGF + aGF;
    const totalGA = hGA + aGA;
    const highestProb = getHighestProbability(match);

    // 💡 Confidence Level Tags
    if (highestProb >= 75) {
        tags.push(`💡 Pick Confidence: High — ${highestProb}%`);
    } else if (highestProb >= 60) {
        tags.push('🧠 AI Confidence: Medium');
    }
    if (match.home_gd < 0 && match.away_gd < 0) {
  tags.push('📉 Both Teams Negative GD');
} else if (match.home_gd < 0) {
  tags.push('📉 Home Negative GD');
} else if (match.away_gd < 0) {
  tags.push('📉 Away Negative GD');
}


    // ⚡ Attacking Momentum
    if (totalGF > totalGA + 10) {
        tags.push('⚡ Attacking Momentum');
    }

    // 😮 Upset Alert
    if (homeRank > awayRank && match.prob_1 > 60) {
        tags.push('😮 Upset Alert');
    }

    // 🎯 Consistent Scorer (very high GF)
    if (hGF > 40 || aGF > 40) {
        tags.push('🎯 Consistent Scorer');
    }

    // 🔥 Streak Team (5+ wins)
    if (hW >= 5 || aW >= 5) {
        tags.push('🔥 Streak Team');
    }

    // 📉 Poor Form (more losses than wins)
    if (match.home_gp >= 5 && match.home_l > match.home_w) {
        tags.push('📉 Home Poor Form');
    }
    if (match.away_gp >= 5 && match.away_l > match.away_w) {
        tags.push('📉 Away Poor Form');
    }

    // 🎯 Over 2.5 Goals
    if (totalGF + totalGA > 70 || (hGF > 30 && aGF > 30)) {
        tags.push('🎯 Over 2.5 Goals');
    }

    // 🛡️ Safe Pick
    if (Math.abs(hPts - aPts) > 20 && (hPts > 0 || aPts > 0)) {
        tags.push('🛡️ Safe Pick');
    }

    return tags;
}

// Fetch Matches
const fetchData = async () => {
    loading.value = true;
    error.value = null;
    try {
        // Try to fetch from API first
        const res = await axios.get('/forebet-data');
        matches.value = res.data.map((match) => ({
            ...match,
            league: match.game.split(' - ')[0] || match.league,
        }));
    } catch (e) {
        console.error('Error loading predictions', e);
        // If API fails, use sample data
        matches.value = sampleMatches.map((match) => ({
            ...match,
            league: match.game.split(' - ')[0] || match.league,
        }));
        error.value = 'Using sample data - API unavailable';
    } finally {
        loading.value = false;
    }
};
const toggleTagFilter = (tag) => {
    const index = selectedTags.value.indexOf(tag);
    if (index === -1) selectedTags.value.push(tag);
    else selectedTags.value.splice(index, 1);
};
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
        'key': 'c68164d29f3923a1e7a7ff9be7d2e396',
        'format': 'iframe',
       'height' : 50,
		'width' : 320,
		'params' : {}
      };
    `;
        const script2 = document.createElement('script');
        script2.type = 'text/javascript';
        script2.src = '//www.highperformanceformat.com/c68164d29f3923a1e7a7ff9be7d2e396/invoke.js';
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
    transition:
        background-color 0.2s ease,
        border-color 0.2s ease;
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
    box-shadow:
        0 4px 6px -1px rgba(0, 0, 0, 0.1),
        0 2px 4px -1px rgba(0, 0, 0, 0.06);
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
