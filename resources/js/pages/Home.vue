<template>
    <div class="min-h-screen bg-gray-50 p-4 md:p-6">
        <div class="">
            <!-- Header Section -->
            <!-- Animated Header Section -->
            <header
                class="mb-8 backdrop-blur-sm animate-fade-in bg-white/90 p-5 rounded-2xl shadow-lg border border-gray-100">
                <div class="flex flex-col justify-between gap-6 md:flex-row md:items-center">
                    <!-- Logo + Title -->
                    <div class="flex items-center gap-4">
                        <!-- Tunisia Flag Logo with modern treatment -->
                        <div
                            class="relative overflow-hidden rounded-xl transition-all duration-300 hover:shadow-red-200/50 hover:shadow-lg">
                            <div
                                class="absolute inset-0 bg-gradient-to-br from-red-600/20 to-red-900/10 animate-pulse-slow">
                            </div>
                            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Tunisia.svg"
                                alt="Tunisia Logo"
                                class="h-14 w-14 relative z-10 transform rounded-xl transition-all duration-300 hover:-rotate-6" />
                        </div>

                        <div class="transition-all duration-300 hover:translate-x-1">
                            <h1
                                class="bg-gradient-to-r from-red-700 via-red-600 to-red-500 bg-clip-text text-3xl font-extrabold tracking-tight text-transparent md:text-4xl">
                                ⚽ DimaRaba7
                            </h1>
                            <p class="text-sm font-medium text-gray-600">
                                <span
                                    class="bg-gradient-to-r from-red-600 to-red-400 bg-clip-text text-transparent font-semibold">
                                    Tunisian Football Intelligence
                                </span>
                                • Predictions • Analytics
                            </p>

                            <!-- Online User Count with modern icon -->
                            <div class="mt-2 flex items-center gap-2">
                                <div class="flex h-5 items-center">
                                    <span class="relative flex h-3 w-3">
                                        <span
                                            class="absolute inline-flex h-full w-full animate-ping rounded-full bg-green-400 opacity-75"></span>
                                        <span class="relative inline-flex h-3 w-3 rounded-full bg-green-500"></span>
                                    </span>
                                </div>
                                <p class="text-xs font-medium text-gray-500">{{ onlineUsers }} visitors online</p>
                            </div>
                        </div>
                    </div>

                    <!-- Action Buttons -->
                    <div class="flex gap-3">
                        <button @click="fetchData"
                            class="group flex items-center gap-2 rounded-xl bg-gradient-to-br from-white to-gray-50 px-4 py-2.5 shadow-sm transition-all hover:shadow-md border border-gray-100 hover:border-red-200">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5 text-red-500 transition-transform duration-500 group-hover:rotate-180"
                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                            </svg>
                            <span class="font-medium text-gray-700">Refresh</span>
                        </button>

                        <button @click="showFilters = !showFilters"
                            class="group relative flex items-center gap-2 rounded-xl bg-gradient-to-r from-red-600 to-red-500 px-5 py-2.5 text-white shadow-md transition-all hover:shadow-lg hover:from-red-700 hover:to-red-600">
                            <svg xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5 text-white transition-transform duration-300 group-hover:scale-110"
                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
                            </svg>
                            <span class="font-medium">{{ showFilters ? "Hide" : "Show" }} Filters</span>
                        </button>
                    </div>
                </div>
            </header>
            <div v-if="!isVIP" class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50">
                <div class="bg-white rounded-lg p-6 shadow-lg w-full max-w-sm text-center space-y-4">
                    <h2 class="text-xl font-bold text-gray-800">VIP Access</h2>
                    <input v-model="vipCodeInput" placeholder="Enter VIP Code"
                        class="w-full border rounded-lg p-2 text-center" @keyup.enter="checkVIPCode" />

                    <button @click="checkVIPCode"
                        class="w-full bg-red-600 hover:bg-red-700 text-white rounded-lg p-2 font-medium">
                        Enter
                    </button>

                    <p v-if="vipError" class="text-red-500 text-sm">{{ vipError }}</p>
                </div>
            </div>
            <!-- Combo Builder Modal -->
            <!-- Combo Builder Modal -->
            <div v-if="showComboModal"
                class="fixed inset-0 z-50 flex items-center justify-center bg-gradient-to-br from-gray-900/80 to-blue-900/80 backdrop-blur-md px-4 transition-opacity duration-300"
                @click="showComboModal = false">
                <div class="relative w-full max-w-3xl rounded-2xl bg-white/95 dark:bg-gray-800/95 p-8 shadow-xl backdrop-blur-lg overflow-y-auto max-h-[92vh] animate-slide-in-up"
                    @click.stop>
                    <!-- Close Button -->
                    <button @click="showComboModal = false"
                        class="absolute right-4 top-4 text-2xl font-semibold text-gray-400 hover:text-red-500 transition-colors"
                        aria-label="Close modal">
                        &times;
                    </button>

                    <!-- Title -->
                    <h2 class="mb-6 text-2xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
                        <span class="text-blue-500">⚙️</span> Smart Combo Generator
                    </h2>

                    <!-- Controls -->
                    <div class="space-y-6">
                        <!-- Strategy Selector -->
                        <div class="relative">
                            <label class="block text-sm font-medium text-gray-700 dark:text-gray-200 mb-1">
                                Combo Type
                                <span class="ml-1 text-xs text-gray-400"
                                    v-tooltip="'Select a strategy to generate your combo'">ℹ️</span>
                            </label>
                            <select v-model="comboStrategy"
                                class="w-full rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 text-sm text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 transition">
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

                        <!-- Min Avg Goals -->
                        <div>
                            <label class="block text-sm font-medium text-gray-700 dark:text-gray-200 mb-1">
                                Minimum Avg Goals
                                <span class="ml-1 text-xs text-gray-400"
                                    v-tooltip="'Only show matches with at least this average goals'">ℹ️</span>
                            </label>
                            <input type="number" min="0" step="0.1" v-model="minAvgGoals" placeholder="e.g., 2.5"
                                class="w-full rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 text-sm text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500" />
                        </div>

                        <!-- Min Confidence -->
                        <div class="mt-4">
                            <label class="block text-sm font-medium text-gray-700 dark:text-gray-200 mb-1">
                                Minimum Confidence %
                                <span class="ml-1 text-xs text-gray-400"
                                    v-tooltip="'Only show matches with at least this confidence'">ℹ️</span>
                            </label>
                            <input type="number" min="0" max="100" step="1" v-model="minConfidence"
                                placeholder="e.g., 70"
                                class="w-full rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 text-sm text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500" />
                        </div>

                        <!-- Match Count -->
                        <div>
                            <label class="block text-sm font-medium text-gray-700 dark:text-gray-200 mb-1">
                                Number of Matches
                                <span class="ml-1 text-xs text-gray-400"
                                    v-tooltip="'Choose 2-10 matches for your combo'">ℹ️</span>
                            </label>
                            <input type="number" min="2" max="10" v-model="comboMatchCount"
                                class="w-full rounded-xl border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 text-sm text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500"
                                :class="{ 'border-red-500': matchCountError }" @input="validateMatchCount" />
                            <p v-if="matchCountError" class="text-xs text-red-500">
                                {{ matchCountError }}
                            </p>
                        </div>

                        <!-- Actions -->
                        <div class="flex gap-4">
                            <button @click="generateUserCombo"
                                class="flex-1 rounded-xl bg-blue-600 py-3 text-white font-medium transition hover:bg-blue-700 disabled:opacity-50">
                                <span v-if="isGenerating" class="flex items-center justify-center gap-2">
                                    <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg"
                                        fill="none" viewBox="0 0 24 24">
                                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor"
                                            stroke-width="4" />
                                        <path class="opacity-75" fill="currentColor"
                                            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                                    </svg>
                                    Generating...
                                </span>
                                <span v-else>🚀 Generate Combo</span>
                            </button>

                            <button @click="resetComboBuilder"
                                class="flex-1 rounded-xl border border-gray-300 dark:border-gray-600 py-3 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 transition">
                                🔄 Reset
                            </button>
                        </div>
                    </div>

                    <!-- Results -->
                    <div v-if="userSmartCombo.length"
                        class="mt-8 rounded-xl border border-gray-200 dark:border-gray-600 bg-white/50 dark:bg-gray-700/50 p-6 shadow-sm">
                        <div class="flex justify-between items-center mb-4">
                            <h3 class="text-lg font-semibold text-gray-800 dark:text-white flex items-center gap-2">
                                💡 Suggested Picks
                                <span class="text-xs text-gray-400">({{ userSmartCombo.length }} matches)</span>
                            </h3>
                            <button @click="copyCombo"
                                class="text-sm text-blue-600 hover:underline flex items-center gap-1"
                                v-tooltip="'Copy combo to clipboard'">
                                📋 Copy
                            </button>
                        </div>

                        <ul class="space-y-4">
                            <li v-for="match in filteredCombo" :key="match.id"
                                class="border-b border-gray-200 dark:border-gray-600 pb-4 last:border-none animate-fade-in">
                                <!-- Collapsible Match Card -->
                                <div class="flex justify-between items-center cursor-pointer"
                                    @click="toggleMatchDetails(match.id)">
                                    <div class="text-sm text-gray-600 dark:text-gray-300">
                                        🗓 {{ new Date(match.iso_time).toLocaleDateString() }}
                                    </div>
                                    <div class="text-sm font-medium text-blue-600 hover:underline">
                                        <a :href="match.match_url" target="_blank">View Match →</a>
                                    </div>
                                </div>

                                <!-- Teams + Tip -->
                                <div class="mt-2 text-sm font-medium text-gray-800 dark:text-white">
                                    👀 {{ match.home_team }} ({{ match.home_rank || "-" }}) vs
                                    {{ match.away_team }} ({{ match.away_rank || "-" }})
                                </div>
                                <div class="mt-1 text-sm">
                                    🎯 Suggested Tip:
                                    <strong class="text-indigo-600">{{ match.tip }}</strong>

                                    <span class="ml-2 text-xs text-gray-400" :class="getConfidenceColor(match)">({{
                                        getConfidence(match) }}%)</span>
                                </div>

                                <!-- Collapsible Details -->
                                <div class="mt-2 text-xs text-gray-500 dark:text-gray-400 space-y-2 animate-fade-in">
                                    <div class="italic">💬 {{ getTipReason(match, comboStrategy) }}</div>
                                    <div>
                                        📊 Avg Goals/Game:
                                        <strong>{{ getAvgGoals(match) }}</strong>
                                        <span v-if="getAvgGoals(match) >= 2.8"
                                            class="ml-2 text-green-500 font-semibold">
                                            🟢 High Scoring Alert
                                        </span>
                                        <span v-else-if="getAvgGoals(match) <= 2.2"
                                            class="ml-2 text-red-500 font-semibold">
                                            🔴 Low Scoring Trend
                                        </span>
                                    </div>
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
                    <div v-if="showFilters"
                        class="rounded-2xl bg-white p-6 shadow-xl transition-all duration-300 hover:shadow-2xl border border-gray-100">
                        <!-- Header with animated badge -->
                        <div class="mb-6 flex items-center justify-between">
                            <div class="flex items-center gap-3">
                                <div class="flex h-10 w-10 items-center justify-center rounded-full bg-indigo-50">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-indigo-600" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                                    </svg>
                                </div>
                                <h3 class="text-xl font-bold text-gray-800">Filter Matches</h3>
                            </div>
                            <span
                                class="inline-flex animate-pulse items-center rounded-full bg-indigo-100 px-3 py-1 text-sm font-medium text-indigo-800">
                                {{ filteredMatches.length }} matches
                            </span>
                        </div>

                        <!-- Filter Sections -->
                        <div class="space-y-8">
                            <!-- Date & Time Section -->
                            <div class="rounded-xl bg-gray-50 p-4">
                                <h4 class="mb-4 flex items-center text-base font-semibold text-gray-800">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="mr-2 h-5 w-5 text-indigo-600"
                                        fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                    </svg>
                                    Date & Time
                                </h4>

                                <!-- Quick Date Shortcuts -->
                                <div class="mb-4 flex gap-2 text-sm">
                                    <button @click="setToday"
                                        class="flex items-center rounded-lg bg-white px-4 py-2 font-medium text-gray-700 shadow-sm transition-all hover:bg-indigo-50 hover:text-indigo-700">
                                        <span class="mr-1">📅</span> Today
                                    </button>
                                    <button @click="setTomorrow"
                                        class="flex items-center rounded-lg bg-white px-4 py-2 font-medium text-gray-700 shadow-sm transition-all hover:bg-indigo-50 hover:text-indigo-700">
                                        <span class="mr-1">⏭️</span> Tomorrow
                                    </button>
                                </div>

                                <!-- Date Range -->
                                <div class="mb-4 grid grid-cols-2 gap-3">
                                    <div>
                                        <label class="mb-1 block text-sm font-medium text-gray-600">Start Date</label>
                                        <input type="date" v-model="startDateFilter"
                                            class="w-full rounded-lg border-gray-200 bg-white text-sm shadow-sm transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500" />
                                    </div>
                                    <div>
                                        <label class="mb-1 block text-sm font-medium text-gray-600">End Date</label>
                                        <input type="date" v-model="endDateFilter"
                                            class="w-full rounded-lg border-gray-200 bg-white text-sm shadow-sm transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500" />
                                    </div>
                                </div>

                                <!-- Time Range Filter -->
                                <div>
                                    <label class="mb-1 block text-sm font-medium text-gray-600">Time Range</label>
                                    <div class="flex items-center gap-2">
                                        <div class="w-1/2">
                                            <label class="mb-1 block text-xs text-gray-500">From</label>
                                            <input type="time" v-model="timeRangeStart"
                                                class="w-full rounded-lg border-gray-200 bg-white text-sm shadow-sm transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500" />
                                        </div>
                                        <div class="w-1/2">
                                            <label class="mb-1 block text-xs text-gray-500">To</label>
                                            <input type="time" v-model="timeRangeEnd"
                                                class="w-full rounded-lg border-gray-200 bg-white text-sm shadow-sm transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500" />
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Team & League Section -->
                            <div class="rounded-xl bg-gray-50 p-4">
                                <h4 class="mb-4 flex items-center text-base font-semibold text-gray-800">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="mr-2 h-5 w-5 text-indigo-600"
                                        fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                    Team & League
                                </h4>

                                <!-- League Filter -->
                                <div class="mb-4">
                                    <label class="mb-1 block text-sm font-medium text-gray-600">🌍 League</label>
                                    <select v-model="leagueFilter"
                                        class="w-full rounded-lg border-gray-200 bg-white text-sm shadow-sm transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500">
                                        <option value="">All Leagues</option>
                                        <option v-for="league in uniqueLeagues" :key="league" :value="league">
                                            {{ league }}
                                        </option>
                                    </select>
                                </div>

                                <!-- Top Teams Only -->
                                <div>
                                    <label class="mb-1 block text-sm font-medium text-gray-600">Team Quality</label>
                                    <select v-model="topTeamsFilter"
                                        class="w-full rounded-lg border-gray-200 bg-white text-sm shadow-sm transition-all focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500">
                                        <option value="false">All Teams</option>
                                        <option value="1">Top 1 Ranked Only</option>
                                        <option value="2">Top 2 Ranked Only</option>
                                        <option value="3">Top 3 Ranked Only</option>
                                        <option value="4">Top 4 Ranked Only</option>
                                        <option value="5">Top 5 Ranked Only</option>
                                    </select>
                                </div>
                            </div>

                            <!-- Collapsible Performance Stats Section -->
                            <div class="mt-6 space-y-4">
                                <!-- Toggle Button -->
                                <button @click="showPerformanceStats = !showPerformanceStats"
                                    class="flex w-full items-center justify-between rounded-xl border border-gray-200 bg-white p-4 shadow-sm transition-all hover:bg-gray-50 hover:shadow">
                                    <div class="flex items-center gap-3">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-indigo-600"
                                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                                        </svg>
                                        <span class="text-lg font-semibold text-gray-800">Performance Stats</span>
                                    </div>
                                    <div class="flex items-center gap-2">
                                        <span class="text-sm font-medium text-gray-500">
                                            {{ showPerformanceStats ? 'Hide Stats' : 'Show Stats' }}
                                        </span>
                                        <svg xmlns="http://www.w3.org/2000/svg"
                                            class="h-5 w-5 text-gray-500 transition-transform"
                                            :class="showPerformanceStats ? 'rotate-180' : ''" fill="none"
                                            viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M19 9l-7 7-7-7" />
                                        </svg>
                                    </div>
                                </button>

                                <!-- Performance Stats Content (Collapsible) -->
                                <div v-show="showPerformanceStats"
                                    class="rounded-xl border border-gray-200 bg-white p-6 shadow-lg transition-all duration-300">
                                    <!-- Win Rates Section -->
                                    <div class="mb-6">
                                        <h5 class="mb-4 flex items-center text-base font-semibold text-gray-700">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="mr-2 h-5 w-5 text-green-600"
                                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                            </svg>
                                            Win Rates
                                        </h5>

                                        <div class="grid grid-cols-1 gap-5 lg:grid-cols-2">
                                            <!-- Home Win Rate Range Filter -->
                                            <div
                                                class="group rounded-lg bg-green-50 p-4 transition-all hover:bg-green-100">
                                                <div class="mb-2 flex items-center justify-between">
                                                    <label class="text-sm font-medium text-green-700">
                                                        🏠 Home Win Rate
                                                    </label>
                                                    <span
                                                        class="rounded-full bg-green-600 px-2.5 py-1 text-xs font-medium text-white">
                                                        {{ homeWinRateMin }}% - {{ homeWinRateMax }}%
                                                    </span>
                                                </div>
                                                <div class="flex items-center gap-3">
                                                    <input type="range" min="0" max="100" step="1"
                                                        v-model.number="homeWinRateMin"
                                                        class="h-2 w-1/2 appearance-none rounded-lg bg-green-200 accent-green-600" />
                                                    <input type="range" min="0" max="100" step="1"
                                                        v-model.number="homeWinRateMax"
                                                        class="h-2 w-1/2 appearance-none rounded-lg bg-green-200 accent-green-600" />
                                                </div>
                                            </div>

                                            <!-- Away Win Rate Range Filter -->
                                            <div
                                                class="group rounded-lg bg-blue-50 p-4 transition-all hover:bg-blue-100">
                                                <div class="mb-2 flex items-center justify-between">
                                                    <label class="text-sm font-medium text-blue-700">
                                                        🚗 Away Win Rate
                                                    </label>
                                                    <span
                                                        class="rounded-full bg-blue-600 px-2.5 py-1 text-xs font-medium text-white">
                                                        {{ awayWinRateMin }}% - {{ awayWinRateMax }}%
                                                    </span>
                                                </div>
                                                <div class="flex items-center gap-3">
                                                    <input type="range" min="0" max="100" step="1"
                                                        v-model.number="awayWinRateMin"
                                                        class="h-2 w-1/2 appearance-none rounded-lg bg-blue-200 accent-blue-600" />
                                                    <input type="range" min="0" max="100" step="1"
                                                        v-model.number="awayWinRateMax"
                                                        class="h-2 w-1/2 appearance-none rounded-lg bg-blue-200 accent-blue-600" />
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Loss Rates Section -->
                                    <div class="mb-6">
                                        <h5 class="mb-4 flex items-center text-base font-semibold text-gray-700">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="mr-2 h-5 w-5 text-red-600"
                                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                            </svg>
                                            Loss Rates
                                        </h5>

                                        <div class="grid grid-cols-1 gap-5 lg:grid-cols-2">
                                            <!-- Home Loss Rate Range Filter -->
                                            <div class="group rounded-lg bg-red-50 p-4 transition-all hover:bg-red-100">
                                                <div class="mb-2 flex items-center justify-between">
                                                    <label class="text-sm font-medium text-red-700">
                                                        🏠❌ Home Loss Rate
                                                    </label>
                                                    <span
                                                        class="rounded-full bg-red-600 px-2.5 py-1 text-xs font-medium text-white">
                                                        {{ homeLossRateMin }}% - {{ homeLossRateMax }}%
                                                    </span>
                                                </div>
                                                <div class="flex items-center gap-3">
                                                    <input type="range" min="0" max="100" step="1"
                                                        v-model.number="homeLossRateMin"
                                                        class="h-2 w-1/2 appearance-none rounded-lg bg-red-200 accent-red-600" />
                                                    <input type="range" min="0" max="100" step="1"
                                                        v-model.number="homeLossRateMax"
                                                        class="h-2 w-1/2 appearance-none rounded-lg bg-red-200 accent-red-600" />
                                                </div>
                                            </div>

                                            <!-- Away Loss Rate Range Filter -->
                                            <div class="group rounded-lg bg-red-50 p-4 transition-all hover:bg-red-100">
                                                <div class="mb-2 flex items-center justify-between">
                                                    <label class="text-sm font-medium text-red-700">
                                                        ⚠️ Away Loss Rate
                                                    </label>
                                                    <span
                                                        class="rounded-full bg-red-600 px-2.5 py-1 text-xs font-medium text-white">
                                                        {{ awayLossRateMin }}% - {{ awayLossRateMax }}%
                                                    </span>
                                                </div>
                                                <div class="flex items-center gap-3">
                                                    <input type="range" min="0" max="100" step="1"
                                                        v-model.number="awayLossRateMin"
                                                        class="h-2 w-1/2 appearance-none rounded-lg bg-red-200 accent-red-600" />
                                                    <input type="range" min="0" max="100" step="1"
                                                        v-model.number="awayLossRateMax"
                                                        class="h-2 w-1/2 appearance-none rounded-lg bg-red-200 accent-red-600" />
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Goals Section -->
                                    <div>
                                        <h5 class="mb-4 flex items-center text-base font-semibold text-gray-700">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="mr-2 h-5 w-5 text-amber-600"
                                                fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                    d="M13 10V3L4 14h7v7l9-11h-7z" />
                                            </svg>
                                            Goals Statistics
                                        </h5>

                                        <div class="grid grid-cols-1 gap-5 md:grid-cols-2">
                                            <!-- Home GF Filter -->
                                            <div
                                                class="group rounded-lg bg-green-50 p-4 transition-all hover:bg-green-100">
                                                <div class="mb-2 flex items-center justify-between">
                                                    <label class="text-sm font-medium text-green-700">
                                                        🏠 Home Goals For
                                                    </label>
                                                    <span
                                                        class="rounded-full bg-green-600 px-2.5 py-1 text-xs font-medium text-white">
                                                        Min: {{ minHomeGF }}
                                                    </span>
                                                </div>
                                                <input type="range" min="0" max="100" step="1"
                                                    v-model.number="minHomeGF"
                                                    class="h-2 w-full appearance-none rounded-lg bg-green-200 accent-green-600" />
                                            </div>

                                            <!-- Away GF Filter -->
                                            <div
                                                class="group rounded-lg bg-blue-50 p-4 transition-all hover:bg-blue-100">
                                                <div class="mb-2 flex items-center justify-between">
                                                    <label class="text-sm font-medium text-blue-700">
                                                        🚗 Away Goals For
                                                    </label>
                                                    <span
                                                        class="rounded-full bg-blue-600 px-2.5 py-1 text-xs font-medium text-white">
                                                        Min: {{ minAwayGF }}
                                                    </span>
                                                </div>
                                                <input type="range" min="0" max="100" step="1"
                                                    v-model.number="minAwayGF"
                                                    class="h-2 w-full appearance-none rounded-lg bg-blue-200 accent-blue-600" />
                                            </div>

                                            <!-- Home GA Filter -->
                                            <div class="group rounded-lg bg-red-50 p-4 transition-all hover:bg-red-100">
                                                <div class="mb-2 flex items-center justify-between">
                                                    <label class="text-sm font-medium text-red-700">
                                                        🏠 Home Goals Against
                                                    </label>
                                                    <span
                                                        class="rounded-full bg-red-600 px-2.5 py-1 text-xs font-medium text-white">
                                                        Min: {{ minHomeGA }}
                                                    </span>
                                                </div>
                                                <input type="range" min="0" max="100" step="1"
                                                    v-model.number="minHomeGA"
                                                    class="h-2 w-full appearance-none rounded-lg bg-red-200 accent-red-600" />
                                            </div>

                                            <!-- Away GA Filter -->
                                            <div class="group rounded-lg bg-red-50 p-4 transition-all hover:bg-red-100">
                                                <div class="mb-2 flex items-center justify-between">
                                                    <label class="text-sm font-medium text-red-700">
                                                        🚗 Away Goals Against
                                                    </label>
                                                    <span
                                                        class="rounded-full bg-red-600 px-2.5 py-1 text-xs font-medium text-white">
                                                        Min: {{ minAwayGA }}
                                                    </span>
                                                </div>
                                                <input type="range" min="0" max="100" step="1"
                                                    v-model.number="minAwayGA"
                                                    class="h-2 w-full appearance-none rounded-lg bg-red-200 accent-red-600" />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Collapsible Advanced Filters -->
                            <div class="space-y-4">
                                <!-- Toggle Button -->
                                <button @click="showAdvancedFilters = !showAdvancedFilters"
                                    class="flex w-full items-center justify-between rounded-xl border border-gray-200 bg-white p-4 shadow-sm transition-all hover:bg-gray-50 hover:shadow">
                                    <div class="flex items-center gap-3">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-indigo-600"
                                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                                        </svg>
                                        <span class="text-lg font-semibold text-gray-800">Advanced Filters</span>
                                    </div>
                                    <div class="flex items-center gap-2">
                                        <span class="text-sm font-medium text-gray-500">
                                            {{ showAdvancedFilters ? 'Hide Filters' : 'Show Filters' }}
                                        </span>
                                        <svg xmlns="http://www.w3.org/2000/svg"
                                            class="h-5 w-5 text-gray-500 transition-transform"
                                            :class="showAdvancedFilters ? 'rotate-180' : ''" fill="none"
                                            viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M19 9l-7 7-7-7" />
                                        </svg>
                                    </div>
                                </button>

                                <!-- Advanced Filters Content (Collapsible) -->
                                <div v-show="showAdvancedFilters"
                                    class="rounded-xl border border-gray-200 bg-white p-6 shadow-lg transition-all duration-300">
                                    <div class="mb-6 grid grid-cols-1 gap-5 md:grid-cols-2">
                                        <!-- H/A Score Filter -->
                                        <div class="group rounded-lg bg-gray-50 p-4 transition-all hover:bg-gray-100">
                                            <label class="mb-2 block text-sm font-medium text-gray-700">
                                                H/A Performance Score
                                            </label>
                                            <select v-model="haScoreFilter"
                                                class="w-full rounded-lg border-gray-200 bg-white px-4 py-2.5 text-sm shadow-sm transition-all focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/50">
                                                <option value="all">All Scores</option>
                                                <option value="0-30">0–30% (Poor)</option>
                                                <option value="30-60">30–60% (Average)</option>
                                                <option value="60-70">60–70% (Good)</option>
                                                <option value="70-80">70–80% (Very Good)</option>
                                                <option value="80-100">80–100% (Excellent)</option>
                                            </select>
                                        </div>

                                        <!-- Predicted Result Filter -->
                                        <div class="group rounded-lg bg-gray-50 p-4 transition-all hover:bg-gray-100">
                                            <label class="mb-2 block text-sm font-medium text-gray-700">
                                                Result Prediction score
                                            </label>
                                            <select v-model="pickFilter"
                                                class="w-full rounded-lg border-gray-200 bg-white px-4 py-2.5 text-sm shadow-sm transition-all focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/50">
                                                <option value="">All Results</option>
                                                <option value="1">🏠 Home Win</option>
                                                <option value="X">🤝 Draw</option>
                                                <option value="2">🚗 Away Win</option>
                                            </select>
                                        </div>

                                        <!-- GP Filter Slider -->
                                        <div
                                            class="group rounded-lg bg-indigo-50 p-4 transition-all hover:bg-indigo-100">
                                            <div class="mb-2 flex items-center justify-between">
                                                <label class="text-sm font-medium text-indigo-700">
                                                    Minimum Games Played
                                                </label>
                                                <span
                                                    class="rounded-full bg-indigo-600 px-2.5 py-1 text-xs font-medium text-white">
                                                    {{ minGP }}
                                                </span>
                                            </div>
                                            <input type="range" min="1" max="30" step="1" v-model.number="minGP"
                                                class="h-2 w-full appearance-none rounded-lg bg-indigo-200 accent-indigo-600" />
                                        </div>

                                        <!-- Win Gap Filter -->
                                        <div
                                            class="group rounded-lg bg-purple-50 p-4 transition-all hover:bg-purple-100">
                                            <div class="mb-2 flex items-center justify-between">
                                                <label class="text-sm font-medium text-purple-700">
                                                    🏆 Win Gap in Games Played
                                                </label>
                                                <span
                                                    class="rounded-full bg-purple-600 px-2.5 py-1 text-xs font-medium text-white">
                                                    {{ winGapMin }}
                                                </span>
                                            </div>
                                            <input type="range" min="0" max="50" step="1" v-model.number="winGapMin"
                                                class="h-2 w-full appearance-none rounded-lg bg-purple-200 accent-purple-600" />
                                        </div>

                                        <!-- Negative GD Slider -->
                                        <div class="group rounded-lg bg-red-50 p-4 transition-all hover:bg-red-100">
                                            <div class="mb-2 flex items-center justify-between">
                                                <label class="text-sm font-medium text-red-700">
                                                    Max Negative Goal Difference
                                                </label>
                                                <span
                                                    class="rounded-full bg-red-600 px-2.5 py-1 text-xs font-medium text-white">
                                                    {{ maxNegativeGD }}
                                                </span>
                                            </div>
                                            <input type="range" min="-50" max="0" step="1"
                                                v-model.number="maxNegativeGD"
                                                class="h-2 w-full appearance-none rounded-lg bg-red-200 accent-red-600" />
                                        </div>

                                        <!-- High Scoring Team Slider -->
                                        <div class="group rounded-lg bg-green-50 p-4 transition-all hover:bg-green-100">
                                            <div class="mb-2 flex items-center justify-between">
                                                <label class="text-sm font-medium text-green-700">
                                                    Minimum Goals For
                                                </label>
                                                <span
                                                    class="rounded-full bg-green-600 px-2.5 py-1 text-xs font-medium text-white">
                                                    {{ minGF }}
                                                </span>
                                            </div>
                                            <input type="range" min="0" max="100" step="1" v-model.number="minGF"
                                                class="h-2 w-full appearance-none rounded-lg bg-green-200 accent-green-600" />
                                        </div>
                                    </div>

                                    <!-- Odds Range Filter -->
                                    <div class="mb-6 rounded-lg bg-amber-50 p-4 transition-all hover:bg-amber-100">
                                        <div class="mb-2 flex items-center justify-between">
                                            <label class="text-sm font-medium text-amber-700">
                                                🎯 Odds Range
                                            </label>
                                            <span
                                                class="rounded-full bg-amber-600 px-2.5 py-1 text-xs font-medium text-white">
                                                {{ minOdds }} - {{ maxOdds }}
                                            </span>
                                        </div>
                                        <div class="flex items-center gap-3">
                                            <input type="range" min="1" max="10" step="0.1" v-model.number="minOdds"
                                                class="h-2 w-1/2 appearance-none rounded-lg bg-amber-200 accent-amber-600" />
                                            <input type="range" min="1" max="10" step="0.1" v-model.number="maxOdds"
                                                class="h-2 w-1/2 appearance-none rounded-lg bg-amber-200 accent-amber-600" />
                                        </div>
                                    </div>

                                    <!-- Checkboxes -->
                                    <div class="mb-6 grid grid-cols-1 gap-3 sm:grid-cols-2">
                                        <div
                                            class="flex items-center rounded-lg bg-white p-3 shadow-sm transition-all hover:shadow">
                                            <input type="checkbox" v-model="onlyWithOdds" id="onlyWithOdds"
                                                class="h-5 w-5 rounded border-gray-300 text-indigo-600 transition focus:ring-indigo-500" />
                                            <label for="onlyWithOdds" class="ml-3 text-sm font-medium text-gray-700">
                                                💸 Show only matches with odds
                                            </label>
                                        </div>
                                        <div
                                            class="flex items-center rounded-lg bg-white p-3 shadow-sm transition-all hover:shadow">
                                            <input type="checkbox" v-model="onlyWithStats" id="onlyWithStats"
                                                class="h-5 w-5 rounded border-gray-300 text-indigo-600 transition focus:ring-indigo-500" />
                                            <label for="onlyWithStats" class="ml-3 text-sm font-medium text-gray-700">
                                                📊 Show only matches with full stats
                                            </label>
                                        </div>
                                    </div>

                                    <!-- Not Started Filter Button -->
                                    <button @click="showNotStarted = !showNotStarted"
                                        class="group flex w-full items-center justify-center gap-3 rounded-lg bg-gradient-to-r from-indigo-500 to-indigo-600 px-5 py-3 text-white shadow-md transition-all hover:from-indigo-600 hover:to-indigo-700 hover:shadow-lg">
                                        <svg xmlns="http://www.w3.org/2000/svg"
                                            class="h-5 w-5 text-white transition-transform duration-300 group-hover:scale-110"
                                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M9 12h6m2 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                                        </svg>
                                        <span class="font-medium">
                                            {{ showNotStarted ? "Show All Matches" : "Show Not Started Matches" }}
                                        </span>
                                    </button>
                                </div>
                            </div>

                            <!-- Smart Insights (Tag Filter Buttons) -->
                            <div class="rounded-xl bg-gray-50 p-4">
                                <h4 class="mb-4 flex items-center text-base font-semibold text-gray-800">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="mr-2 h-5 w-5 text-indigo-600"
                                        fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                                    </svg>
                                    Smart Insights
                                </h4>
                                <div class="flex flex-wrap gap-2">
                                    <button v-for="tag in smartTagOptions" :key="tag.label"
                                        @click="toggleTagFilter(tag.value)" :class="[
                                            'rounded-full px-3 py-1.5 text-sm font-medium transition-all',
                                            selectedTags.includes(tag.value)
                                                ? 'bg-indigo-100 text-indigo-800 shadow-sm'
                                                : 'bg-white text-gray-600 hover:bg-gray-100',
                                        ]">
                                        {{ tag.label }}
                                    </button>
                                </div>
                            </div>

                            <!-- Quick Load Combo Buttons -->
                            <div class="rounded-xl bg-gray-50 p-4">
                                <h4 class="mb-4 flex items-center text-base font-semibold text-gray-800">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="mr-2 h-5 w-5 text-indigo-600"
                                        fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M13 10V3L4 14h7v7l9-11h-7z" />
                                    </svg>
                                    Quick Load Combos
                                </h4>

                                <div class="flex flex-wrap gap-2">
                                    <button @click="loadStrongHomeWin"
                                        class="rounded-lg bg-gradient-to-br from-green-500 to-green-600 px-3 py-1.5 text-sm font-medium text-white shadow-sm transition-all hover:shadow-md">
                                        🏠 Strong Home Win
                                    </button>

                                    <button @click="loadStrongAwayWin"
                                        class="rounded-lg bg-gradient-to-br from-blue-500 to-blue-600 px-3 py-1.5 text-sm font-medium text-white shadow-sm transition-all hover:shadow-md">
                                        🚗 Strong Away Win
                                    </button>





                                    <button @click="loadHomeCollapse"
                                        class="rounded-lg bg-gradient-to-br from-red-500 to-red-600 px-3 py-1.5 text-sm font-medium text-white shadow-sm transition-all hover:shadow-md">
                                        💣 Home Collapse
                                    </button>

                                    <button @click="loadAwayCollapse"
                                        class="rounded-lg bg-gradient-to-br from-red-400 to-red-500 px-3 py-1.5 text-sm font-medium text-white shadow-sm transition-all hover:shadow-md">
                                        🚗💥 Away Collapse
                                    </button>



                                    <button @click="loadBTTSFocus"
                                        class="rounded-lg bg-gradient-to-br from-orange-500 to-orange-600 px-3 py-1.5 text-sm font-medium text-white shadow-sm transition-all hover:shadow-md">
                                        🎯 BTTS Focus
                                    </button>





                                    <!-- Strong Over 2.5 Goals Button -->
                                    <button @click="loadStrongOver25Goals"
                                        class="rounded bg-yellow-500 text-white px-3 py-1 text-sm hover:bg-yellow-600 transition">
                                        ⚡ Strong Over 2.5
                                    </button>

                                    <!-- Monster Over 3.5 Goals Button -->
                                    <button @click="loadMonsterOver35Goals"
                                        class="rounded bg-rose-500 text-white px-3 py-1 text-sm hover:bg-rose-600 transition">
                                        🧨 Monster Over 3.5
                                    </button>
                                    <!-- Buttons -->
                                    <!-- Strong GG Button (1 GG) -->



                                </div>
                            </div>

                            <!-- Actions -->
                            <div class="mt-8 flex justify-end gap-4">
                                <button @click="resetFilters"
                                    class="rounded-lg border border-gray-300 bg-white px-5 py-2.5 text-sm font-medium text-gray-700 shadow-sm transition-all duration-300 hover:bg-gray-50 hover:shadow-md focus:outline-none focus:ring-2 focus:ring-gray-300 focus:ring-offset-2">
                                    <div class="flex items-center gap-2">
                                        <svg class="h-4 w-4 text-gray-500" fill="none" viewBox="0 0 24 24"
                                            stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                                        </svg>
                                        Reset
                                    </div>
                                </button>
                                <button @click="applyFilters"
                                    class="rounded-lg bg-gradient-to-r from-indigo-600 to-indigo-700 px-5 py-2.5 text-sm font-medium text-white shadow-md transition-all duration-300 hover:from-indigo-700 hover:to-indigo-800 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
                                    <div class="flex items-center gap-2">
                                        <svg class="h-4 w-4 text-white" fill="none" viewBox="0 0 24 24"
                                            stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                                d="M5 13l4 4L19 7" />
                                        </svg>
                                        Apply Filters
                                    </div>
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Modern Stats Card -->
                    <!-- Modern Stats Card - Enhanced Version -->
                    <div
                        class="animate-fade-in-up rounded-2xl border border-gray-200 bg-white p-6 shadow-lg transition-all duration-300 hover:shadow-xl">
                        <h3 class="mb-6 flex items-center gap-3 text-xl font-bold text-gray-800">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-indigo-600" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                            </svg>
                            Analytics Dashboard
                        </h3>

                        <div class="grid grid-cols-1 gap-5 sm:grid-cols-2">
                            <!-- Total Matches -->
                            <div
                                class="group flex items-center justify-between rounded-xl bg-gradient-to-br from-gray-50 to-gray-100 p-4 transition-all duration-300 hover:from-gray-100 hover:to-gray-200">
                                <div class="flex flex-col">
                                    <span class="text-sm font-medium text-gray-500">Total Matches</span>
                                    <span class="text-2xl font-bold text-gray-800">{{ filteredMatches.length }}</span>
                                </div>
                                <div class="rounded-full bg-white p-3 shadow-md group-hover:shadow-lg">
                                    <svg class="h-5 w-5 text-indigo-600" fill="none" viewBox="0 0 24 24"
                                        stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M9 12h6m2 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                </div>
                            </div>

                            <!-- High Confidence -->
                            <div
                                class="group flex items-center justify-between rounded-xl bg-gradient-to-br from-green-50 to-green-100 p-4 transition-all duration-300 hover:from-green-100 hover:to-green-200">
                                <div class="flex flex-col">
                                    <span class="text-sm font-medium text-green-600">High Confidence</span>
                                    <span class="text-2xl font-bold text-green-800">
                                        {{ highConfidenceMatchesCount }}
                                        <span class="text-base font-medium">({{ highConfidencePercentage }}%)</span>
                                    </span>
                                </div>
                                <div class="rounded-full bg-white p-3 shadow-md group-hover:shadow-lg">
                                    <svg class="h-5 w-5 text-green-600" fill="none" viewBox="0 0 24 24"
                                        stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M5 13l4 4L19 7" />
                                    </svg>
                                </div>
                            </div>

                            <!-- Top Team Matches -->
                            <div
                                class="group flex items-center justify-between rounded-xl bg-gradient-to-br from-amber-50 to-amber-100 p-4 transition-all duration-300 hover:from-amber-100 hover:to-amber-200">
                                <div class="flex flex-col">
                                    <span class="text-sm font-medium text-amber-600">Top Team Matches</span>
                                    <span class="text-2xl font-bold text-amber-800">{{ topTeamMatchesCount }}</span>
                                </div>
                                <div class="rounded-full bg-white p-3 shadow-md group-hover:shadow-lg">
                                    <svg class="h-5 w-5 text-amber-600" fill="none" viewBox="0 0 24 24"
                                        stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
                                    </svg>
                                </div>
                            </div>

                            <!-- Avg Confidence -->
                            <div
                                class="group flex items-center justify-between rounded-xl bg-gradient-to-br from-indigo-50 to-indigo-100 p-4 transition-all duration-300 hover:from-indigo-100 hover:to-indigo-200">
                                <div class="flex flex-col">
                                    <span class="text-sm font-medium text-indigo-600">Avg. Confidence</span>
                                    <span class="text-2xl font-bold text-indigo-800">{{ averageConfidence }}%</span>
                                </div>
                                <div class="rounded-full bg-white p-3 shadow-md group-hover:shadow-lg">
                                    <svg class="h-5 w-5 text-indigo-600" fill="none" viewBox="0 0 24 24"
                                        stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>
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
                            <svg xmlns="http://www.w3.org/2000/svg" class="mr-2 h-6 w-6 text-red-500" fill="none"
                                viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <p class="font-medium text-red-700">{{ error }}</p>
                        </div>
                    </div>

                    <!-- Empty State -->
                    <div v-else-if="filteredMatches.length === 0" class="py-20 text-center">
                        <svg xmlns="http://www.w3.org/2000/svg" class="mx-auto h-16 w-16 text-gray-300" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <p class="mt-4 text-lg text-gray-500">
                            No matches found with current filters
                        </p>
                        <button @click="resetFilters"
                            class="mt-4 rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700">
                            Reset Filters
                        </button>
                    </div>

                    <!-- Regular Matches Section -->
                    <div class="mt-10">
                        <!-- Grid View -->
                        <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
                            <div v-for="match in paginatedMatchess" :key="match.id"
                                class="group relative overflow-hidden rounded-2xl bg-white shadow-md transition-all duration-300 hover:shadow-xl">
                                <!-- Card Header with Gradient Background -->
                                <div class="bg-gradient-to-r from-indigo-600 to-blue-500 p-4">
                                    <div class="flex items-center justify-between">
                                        <h3 class="text-lg font-bold text-white">
                                            {{ match.home_team }} vs {{ match.away_team }}
                                        </h3>
                                        <span class="rounded-full px-3 py-1 text-xs font-bold backdrop-blur-sm" :class="{
                                            'bg-green-100/90 text-green-800': match.prediction === '1',
                                            'bg-amber-100/90 text-amber-800': match.prediction === 'X',
                                            'bg-red-100/90 text-red-800': match.prediction === '2',
                                        }">
                                            🧠 <strong>{{ getPredictionType(match) }}</strong>
                                        </span>
                                    </div>
                                    <div class="mt-2 flex items-center text-white/90">
                                        <p class="text-sm">{{ match.time_str }}</p>
                                        <div v-if="match.league" class="ml-3 flex items-center">
                                            <span class="mr-1 text-xs">•</span>
                                            <a :href="match.match_url"
                                                class="text-xs font-medium text-white/90 hover:text-white hover:underline">
                                                🏆 {{ match.league }}
                                            </a>
                                        </div>
                                    </div>
                                </div>

                                <div class="p-5">
                                    <!-- Probabilities - Modern Design -->
                                    <div class="mb-6 mt-2 flex justify-between rounded-xl bg-gray-50 p-3">
                                        <div class="flex flex-1 flex-col items-center">
                                            <div
                                                class="mb-1 rounded-full bg-blue-100 px-3 py-1 text-xs font-semibold text-blue-700">
                                                1
                                            </div>
                                            <div class="text-lg font-bold text-gray-800">
                                                {{ match.prob_1 }}%
                                            </div>
                                        </div>
                                        <div class="flex flex-1 flex-col items-center">
                                            <div
                                                class="mb-1 rounded-full bg-amber-100 px-3 py-1 text-xs font-semibold text-amber-700">
                                                X
                                            </div>
                                            <div class="text-lg font-bold text-gray-800">
                                                {{ match.prob_x }}%
                                            </div>
                                        </div>
                                        <div class="flex flex-1 flex-col items-center">
                                            <div
                                                class="mb-1 rounded-full bg-red-100 px-3 py-1 text-xs font-semibold text-red-700">
                                                2
                                            </div>
                                            <div class="text-lg font-bold text-gray-800">
                                                {{ match.prob_2 }}%
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Ranks -->
                                    <div class="mb-5 flex justify-between text-sm">
                                        <div class="flex items-center">
                                            <span class="mr-2 rounded-full bg-green-100 p-1">🏠</span>
                                            <span class="font-medium text-gray-700">Rank: {{ match.home_rank || "-"
                                                }}</span>
                                        </div>
                                        <div class="flex items-center">
                                            <span class="mr-2 rounded-full bg-blue-100 p-1">🚗</span>
                                            <span class="font-medium text-gray-700">Rank: {{ match.away_rank || "-"
                                                }}</span>
                                        </div>
                                    </div>

                                    <!-- Home/Away Score -->
                                    <div class="mb-6 rounded-xl bg-gray-50 p-4">
                                        <div class="mb-3 flex justify-between items-center">
                                            <span class="text-base font-medium text-gray-700">Performance Score</span>
                                            <span :class="{
                                                'text-green-600': getHomeAwayPerformanceScore(match) >= 75,
                                                'text-amber-600':
                                                    getHomeAwayPerformanceScore(match) >= 60 &&
                                                    getHomeAwayPerformanceScore(match) < 75,
                                                'text-red-600': getHomeAwayPerformanceScore(match) < 60,
                                            }" class="text-xl font-bold">
                                                {{ getHomeAwayPerformanceScore(match) }}%
                                            </span>
                                        </div>

                                        <!-- Win/Loss Rates -->
                                        <div class="space-y-3 text-sm">
                                            <div class="flex justify-between items-center">
                                                <span class="flex items-center gap-2">
                                                    <span
                                                        class="flex h-6 w-6 items-center justify-center rounded-full bg-green-100 text-green-600">🏠</span>
                                                    <span class="text-gray-700">Home Win Rate</span>
                                                </span>
                                                <span class="font-semibold text-gray-800">{{ getHomeWinRate(match)
                                                    }}%</span>
                                            </div>

                                            <div class="flex justify-between items-center">
                                                <span class="flex items-center gap-2">
                                                    <span
                                                        class="flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-red-600">🏠</span>
                                                    <span class="text-gray-700">Home Loss Rate</span>
                                                </span>
                                                <span class="font-semibold text-gray-800">{{ getHomeLossRate(match)
                                                    }}%</span>
                                            </div>

                                            <div class="flex justify-between items-center">
                                                <span class="flex items-center gap-2">
                                                    <span
                                                        class="flex h-6 w-6 items-center justify-center rounded-full bg-blue-100 text-blue-600">🚗</span>
                                                    <span class="text-gray-700">Away Win Rate</span>
                                                </span>
                                                <span class="font-semibold text-gray-800">{{ getAwayWinRate(match)
                                                    }}%</span>
                                            </div>

                                            <div class="flex justify-between items-center">
                                                <span class="flex items-center gap-2">
                                                    <span
                                                        class="flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-red-600">🚗</span>
                                                    <span class="text-gray-700">Away Loss Rate</span>
                                                </span>
                                                <span class="font-semibold text-gray-800">{{ getAwayLossRate(match)
                                                    }}%</span>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Live Odds -->
                                    <div v-if="match.live_odds" class="mb-4">
                                        <span
                                            class="inline-flex items-center rounded-full bg-indigo-100 px-3 py-1 text-sm font-medium text-indigo-800">
                                            💸 {{ match.live_odds }}
                                        </span>
                                    </div>

                                    <!-- Extra Tags -->

                                    <!-- Team Stats - Modern Cards -->
                                    <div class="grid grid-cols-2 gap-3 mb-4">
                                        <!-- Home Stats -->
                                        <div class="rounded-lg bg-green-50 p-3">
                                            <div class="mb-2 flex items-center">
                                                <span
                                                    class="mr-2 flex h-5 w-5 items-center justify-center rounded-full bg-green-200 text-xs">🏠</span>
                                                <span class="font-medium text-green-800">Home</span>
                                            </div>
                                            <div class="grid grid-cols-2 gap-2 text-xs">
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">Games</span>
                                                    <span class="font-semibold text-gray-800">{{
                                                        match.home_gp
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">Win</span>
                                                    <span class="font-semibold text-green-700">{{
                                                        match.home_w
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">Draw</span>
                                                    <span class="font-semibold text-amber-700">{{
                                                        match.home_d
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">Loss</span>
                                                    <span class="font-semibold text-red-700">{{
                                                        match.home_l
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">GF</span>
                                                    <span class="font-semibold text-gray-800">{{
                                                        match.home_gf
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">GA</span>
                                                    <span class="font-semibold text-gray-800">{{
                                                        match.home_ga
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">GD</span>
                                                    <span :class="{
                                                        'text-green-700': match.home_gd > 0,
                                                        'text-red-700': match.home_gd < 0,
                                                    }" class="font-semibold">{{ match.home_gd }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">Points</span>
                                                    <span class="font-semibold text-gray-800">{{
                                                        match.home_pts
                                                        }}</span>
                                                </div>
                                            </div>
                                        </div>

                                        <!-- Away Stats -->
                                        <div class="rounded-lg bg-blue-50 p-3">
                                            <div class="mb-2 flex items-center">
                                                <span
                                                    class="mr-2 flex h-5 w-5 items-center justify-center rounded-full bg-blue-200 text-xs">🚗</span>
                                                <span class="font-medium text-blue-800">Away</span>
                                            </div>
                                            <div class="grid grid-cols-2 gap-2 text-xs">
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">Games</span>
                                                    <span class="font-semibold text-gray-800">{{
                                                        match.away_gp
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">Win</span>
                                                    <span class="font-semibold text-green-700">{{
                                                        match.away_w
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">Draw</span>
                                                    <span class="font-semibold text-amber-700">{{
                                                        match.away_d
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">Loss</span>
                                                    <span class="font-semibold text-red-700">{{
                                                        match.away_l
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">GF</span>
                                                    <span class="font-semibold text-gray-800">{{
                                                        match.away_gf
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">GA</span>
                                                    <span class="font-semibold text-gray-800">{{
                                                        match.away_ga
                                                        }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">GD</span>
                                                    <span :class="{
                                                        'text-green-700': match.away_gd > 0,
                                                        'text-red-700': match.away_gd < 0,
                                                    }" class="font-semibold">{{ match.away_gd }}</span>
                                                </div>
                                                <div class="flex items-center justify-between">
                                                    <span class="text-gray-600">Points</span>
                                                    <span class="font-semibold text-gray-800">{{
                                                        match.away_pts
                                                        }}</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Details Link - Modern Style -->
                                <a :href="match.match_url" target="_blank"
                                    class="flex items-center justify-center bg-gradient-to-r from-indigo-600 to-blue-600 py-3 text-sm font-medium text-white transition-all hover:from-indigo-700 hover:to-blue-700">
                                    View Match Details
                                    <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 h-4 w-4" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M14 5l7 7m0 0l-7 7m7-7H3" />
                                    </svg>
                                </a>
                            </div>

                            <!-- See More Button -->
                            <div v-if="hasMorePagess" class="col-span-full p-6 text-center">
                                <button @click="loadMores"
                                    class="group relative inline-flex items-center justify-center overflow-hidden rounded-lg bg-gradient-to-r from-indigo-500 to-blue-600 px-6 py-3 font-medium text-white transition-all hover:from-indigo-600 hover:to-blue-700">
                                    <span class="relative">See More Matches</span>
                                    <svg xmlns="http://www.w3.org/2000/svg" class="relative ml-2 h-5 w-5" fill="none"
                                        viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M19 9l-7 7-7-7" />
                                    </svg>
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
        class="animate-fade-in fixed bottom-4 right-4 flex items-center gap-2 rounded-full border border-gray-200 bg-white/80 px-4 py-1.5 text-sm font-medium text-gray-600 shadow-md backdrop-blur-sm">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-red-500" viewBox="0 0 24 24" fill="currentColor">
            <path
                d="M12 22c5.52 0 10-4.48 10-10S17.52 2 12 2 2 6.48 2 12s4.48 10 10 10zm0-1.5c-4.69 0-8.5-3.81-8.5-8.5S7.31 3.5 12 3.5 20.5 7.31 20.5 12 16.69 20.5 12 20.5z" />
            <path d="M10.25 15h1.5V9h-1.5v6zm0 2h1.5v-1.5h-1.5V17z" />
        </svg>
        Mahmoud Bouhlel © {{ new Date().getFullYear() }}
    </footer>
</template>

<script setup>
import axios from "axios";
import { computed, onMounted, ref } from "vue";

const haScoreFilter = ref("all"); // Options: all, 60+, 75+
const minGP = ref(0); // Default: Matches with both teams playing more than 10 games.
const maxNegativeGD = ref(0); // Default: Matches where either team has GD less than -30.
const minGF = ref(0); // Default: Matches where either team scores more than 50 goals.
const timeRangeStart = ref("");
const timeRangeEnd = ref("");
const minAvgGoals = ref(0); // Default: 0, means no filter
const minConfidence = ref(0); // Default: 0, means no filter
const minHomeGF = ref(0); // Minimum Home GF
const minAwayGF = ref(0); // Minimum Away GF
const showPerformanceStats = ref(false); // Controls visibility of stats section
const showAdvancedFilters = ref(false); // Controls visibility of stats section



const winGapMin = ref(0); // default value can be 0 (show all)
const isVIP = ref(false);
const vipCodeInput = ref("");
const vipError = ref("");
// State
const matches = ref([]);
const loading = ref(true);
const error = ref(null);
const showFilters = ref(false);
const showAllMustWatch = ref(false);
const mustWatchLimit = ref(10);
const minHomeGA = ref(0); // Minimum Home Goals Against
const minAwayGA = ref(0); // Minimum Away Goals Against

const tableView = ref(false);
const currentPage = ref(1);
const rowsPerPage = 50;
const page = ref(1);
const perPage = 50;
const tagFilter = ref("");
const onlyWithOdds = ref(false);
const onlyWithStats = ref(false);
const showComboModal = ref(false);
const comboStrategy = ref("best");
const comboStartDate = ref("");
const comboEndDate = ref("");
const comboMatchCount = ref(5);
const userSmartCombo = ref([]);
const isGenerating = ref(false);
const dateError = ref("");
const matchCountError = ref("");
const expandedMatches = ref({});

const minOdds = ref("");
const maxOdds = ref("");
const matchTimeFrom = ref("");
const matchTimeTo = ref("");
const HWR_WEIGHT = 0.4; // Weight of home win rate
const HGS_WEIGHT = 0.3; // Weight of home goals scored
const ALR_WEIGHT = 0.2; // Weight of away loss rate
const GD_WEIGHT = 0.1; // Weight of goal difference
const performanceScoreFilter = ref("all"); // Default to 'all'
const showNotStarted = ref(false); // to toggle between showing all or not started matches
const homeWinRateMin = ref(0);
const homeWinRateMax = ref(100);
const homeLossRateMin = ref(0);
const homeLossRateMax = ref(100);

const awayWinRateMin = ref(0);
const awayWinRateMax = ref(100);

const awayLossRateMin = ref(0);
const awayLossRateMax = ref(100);

const comboAvgGoals = computed(() => {
    if (!userSmartCombo.value.length) return 0;

    const total = userSmartCombo.value.reduce((sum, match) => sum + getAvgGoals(match), 0);
    return (total / userSmartCombo.value.length).toFixed(2);
});
const filteredCombo = computed(() => {
    if (!userSmartCombo.value.length) return [];

    return userSmartCombo.value.filter((match) => {
        const avgGoals = getAvgGoals(match);
        const confidence = getConfidence(match);

        // If minAvgGoals and minConfidence not set (still 0), allow all
        const goalsOk = minAvgGoals.value ? avgGoals >= minAvgGoals.value : true;
        const confidenceOk = minConfidence.value ? confidence >= minConfidence.value : true;

        return goalsOk && confidenceOk;
    });
});

const uniqueLeagues = computed(() => {
    const allLeagues = filteredMatches.value.map((m) => m.league).filter(Boolean);
    return [...new Set(allLeagues)].sort((a, b) => a.localeCompare(b));
});

const toggleMatchDetails = (matchId) => {
    expandedMatches.value = {
        ...expandedMatches.value,
        [matchId]: !expandedMatches.value[matchId],
    };
};

// Combo builder date validation
const validateDates = () => {
    if (!comboStartDate.value || !comboEndDate.value) {
        dateError.value = "";
        return;
    }

    const start = new Date(comboStartDate.value);
    const end = new Date(comboEndDate.value);

    if (end < start) {
        dateError.value = "End date must be after start date";
    } else {
        dateError.value = "";
    }
};

// Match count validation
const validateMatchCount = () => {
    const count = parseInt(comboMatchCount.value);
    if (isNaN(count) || count < 2) {
        matchCountError.value = "Please select at least 2 matches";
    } else if (count > 99999) {
        matchCountError.value = "Maximum 9999 matches allowed";
    } else {
        matchCountError.value = "";
    }
};

// Function to get confidence color
const getConfidenceColor = (match) => {
    const confidence = getConfidence(match);
    if (confidence >= 75) return "text-green-600";
    if (confidence >= 60) return "text-blue-600";
    return "text-gray-500";
};

// Function to get confidence percentage
const getConfidence = (match) => {
    const highestProb = getHighestProbability(match);
    return Math.round(highestProb);
};

// Copy combo to clipboard
const copyCombo = async () => {
    try {
        const comboText = userSmartCombo.value
            .map((match) => {
                return `${match.home_team} vs ${match.away_team} - ${match.tip} (${getConfidence(
                    match
                )}%)`;
            })
            .join("\n");

        await navigator.clipboard.writeText(comboText);
        alert("Combo copied to clipboard!");
    } catch (err) {
        console.error("Failed to copy combo:", err);
        alert("Failed to copy. Please try manually selecting and copying the text.");
    }
};
// Open the combo builder modal
const openComboBuilder = () => {
    // Pre-fill with current date range if empty
    if (!comboStartDate.value) {
        const today = new Date().toISOString().split("T")[0];
        comboStartDate.value = today;
        comboEndDate.value = today;
    }

    showComboModal.value = true;
};
// Function to calculate Home Win Rate
function getHomeWinRate(match) {
    if (!match.home_gp) return 0; // Prevent division by 0
    return ((match.home_w / match.home_gp) * 100).toFixed(1); // Return percentage with 1 decimal place
}
// Function to calculate Home Loss Rate (HLR)
function getHomeLossRate(match) {
    if (!match.home_gp) return 0; // Prevent division by 0
    return ((match.home_l / match.home_gp) * 100).toFixed(1); // Return percentage with 1 decimal place
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
        homeWinRate * HWR_WEIGHT +
        homeGoalsScored * HGS_WEIGHT -
        awayLossRate * ALR_WEIGHT -
        awayGoalsConceded * ALR_WEIGHT + // More goals conceded away = worse
        goalDifference * GD_WEIGHT; // Better goal difference = better performance

    return score;
}

const generateUserCombo = async () => {
    isGenerating.value = true;

    const start = comboStartDate.value ? new Date(comboStartDate.value) : null;
    const end = comboEndDate.value ? new Date(comboEndDate.value) : null;

    // Helper functions for metrics
    const hGF = (m) => m.home_gf || 0; // Home goals for
    const aGF = (m) => m.away_gf || 0; // Away goals for
    const hGA = (m) => m.home_ga || 0; // Home goals against
    const aGA = (m) => m.away_ga || 0; // Away goals against
    const rankGap = (m) => Math.abs((m.home_rank || 0) - (m.away_rank || 0));
    const prob = (m) => getHighestProbability(m); // Highest win/draw probability
    const prediction = (m) => getPredictionType(m); // 1/X/2 or other prediction
    const totalGF = (m) => hGF(m) + aGF(m); // Total goals scored
    const totalGA = (m) => hGA(m) + aGA(m); // Total goals conceded
    const avgGoalsPerGame = (m) => {
        const matches = m.matches_played || 1; // Avoid division by zero
        return ((hGF(m) + aGF(m) + hGA(m) + aGA(m)) / (2 * matches)).toFixed(2); // Avg goals per game
    };

    // Base filter by date range
    let filtered = [...filteredMatches.value].filter((m) => {
        const matchDate = new Date(m.iso_time);
        if (start && matchDate < start) return false;
        if (end && matchDate > end) return false;
        return true;
    });

    // Strategy-specific filtering
    switch (comboStrategy.value) {
        case "smart_over":
            filtered = filtered
                .filter(
                    (m) =>
                        avgGoalsPerGame(m) > 2.8 && (totalGF(m) > 50 || (hGF(m) > 30 && aGF(m) > 20))
                )
                .map((m) => {
                    let tip = "Over 2.5";
                    if (avgGoalsPerGame(m) > 3.5) tip = "Over 3.5";
                    else if (avgGoalsPerGame(m) > 3.0) tip = "Over 2.5";
                    else tip = "Over 1.5";
                    return { ...m, tip };
                })
                .sort((a, b) => avgGoalsPerGame(b) - avgGoalsPerGame(a)); // Sort by highest avg goals
            break;

        case "smart_under":
            filtered = filtered
                .filter(
                    (m) => avgGoalsPerGame(m) < 2.2 && totalGF(m) < 20 && hGF(m) < 15 && aGF(m) < 15
                )
                .map((m) => ({
                    ...m,
                    tip: avgGoalsPerGame(m) < 1.5 ? "Under 1.5" : "Under 2.5",
                }))
                .sort((a, b) => avgGoalsPerGame(a) - avgGoalsPerGame(b)); // Sort by lowest avg goals
            break;

        case "btts_focus":
            filtered = filtered
                .filter(
                    (m) =>
                        hGF(m) > 25 &&
                        aGF(m) > 25 &&
                        hGA(m) > 20 &&
                        aGA(m) > 20 &&
                        avgGoalsPerGame(m) > 2.5
                )
                .map((m) => ({ ...m, tip: "BTTS" }))
                .sort((a, b) => hGF(b) + aGF(b) - (hGF(a) + aGF(a))); // Sort by scoring potential
            break;

        case "draw_focus":
            filtered = filtered
                .filter(
                    (m) =>
                        rankGap(m) <= 2 &&
                        Math.abs(m.prob_1 - m.prob_2) <= 10 &&
                        avgGoalsPerGame(m) < 2.5
                )
                .map((m) => ({ ...m, tip: "Draw" }))
                .sort((a, b) => rankGap(a) - rankGap(b)); // Sort by closest rank gap
            break;

        case "safe_combo":
            filtered = filtered
                .filter((m) => prob(m) >= 75 && rankGap(m) >= 5 && avgGoalsPerGame(m) > 2.0)
                .map((m) => ({
                    ...m,
                    tip: prediction(m) === "Draw" ? "Double Chance" : `${prediction(m)} - Safe`,
                }))
                .sort((a, b) => prob(b) - prob(a)); // Sort by highest probability
            break;

        case "home_over":
            filtered = filtered
                .filter((m) => hGF(m) > 30 && aGA(m) > 25 && avgGoalsPerGame(m) > 2.8)
                .map((m) => ({ ...m, tip: "Home Over 2.5" }))
                .sort((a, b) => hGF(b) - hGF(a)); // Sort by home goals
            break;

        case "away_over":
            filtered = filtered
                .filter((m) => aGF(m) > 30 && hGA(m) > 25 && avgGoalsPerGame(m) > 2.8)
                .map((m) => ({ ...m, tip: "Away Over 2.5" }))
                .sort((a, b) => aGF(b) - aGF(a)); // Sort by away goals
            break;

        case "home_under":
            filtered = filtered
                .filter((m) => hGF(m) < 15 && aGA(m) < 15 && avgGoalsPerGame(m) < 2.2)
                .map((m) => ({ ...m, tip: "Home Under 2.5" }))
                .sort((a, b) => hGF(a) - hGF(b)); // Sort by lowest home goals
            break;

        case "away_under":
            filtered = filtered
                .filter((m) => aGF(m) < 15 && hGA(m) < 15 && avgGoalsPerGame(m) < 2.2)
                .map((m) => ({ ...m, tip: "Away Under 2.5" }))
                .sort((a, b) => aGF(a) - aGF(b)); // Sort by lowest away goals
            break;

        case "mixed":
            filtered = filtered
                .filter((m) => avgGoalsPerGame(m) > 2.0 || prob(m) > 60)
                .map((m, i) => {
                    const tags = getMatchTags(m);
                    let tip = prediction(m);
                    if (tags.includes("🎯 Over 2.5 Goals") || avgGoalsPerGame(m) > 3.0)
                        tip = "Over 2.5";
                    else if (tags.includes("🎯 Consistent Scorer") && avgGoalsPerGame(m) > 2.5)
                        tip = "BTTS";
                    else if (i % 3 === 0) tip = "Over 1.5";
                    else if (i % 4 === 0 && rankGap(m) < 3) tip = "Draw";
                    return { ...m, tip };
                })
                .sort((a, b) => prob(b) - prob(a)); // Sort by probability
            break;

        case "goals":
            filtered = filtered
                .filter((m) => totalGF(m) > 60 && avgGoalsPerGame(m) > 3.0)
                .map((m) => ({ ...m, tip: "Over 2.5 Goals" }))
                .sort((a, b) => avgGoalsPerGame(b) - avgGoalsPerGame(a)); // Sort by highest avg goals
            break;

        case "super_combo":
            filtered = filtered
                .filter((m) => prob(m) > 65 || totalGF(m) > 50 || avgGoalsPerGame(m) > 2.8)
                .map((m, i) => {
                    const p = prediction(m);
                    if (i % 2 === 0 && avgGoalsPerGame(m) > 3.0) return { ...m, tip: "Over 2.5" };
                    if (i % 3 === 0 && hGF(m) > 25 && aGF(m) > 25) return { ...m, tip: "BTTS" };
                    if (i % 4 === 0 && rankGap(m) < 3) return { ...m, tip: "Draw" };
                    if (prob(m) > 75 && rankGap(m) > 5) return { ...m, tip: `${p} - Safe` };
                    return { ...m, tip: p };
                })
                .sort((a, b) => prob(b) - prob(a)); // Sort by probability
            break;

        default:
            // Best: High-confidence predictions
            filtered = filtered
                .filter((m) => prob(m) > 65 && avgGoalsPerGame(m) > 2.0)
                .map((m) => ({ ...m, tip: prediction(m) }))
                .sort((a, b) => prob(b) - prob(a)); // Sort by highest probability
            break;
    }

    // Dynamic fallback: Relax constraints if too few results
    if (filtered.length < comboMatchCount.value) {
        filtered = [...filteredMatches.value]
            .filter((m) => {
                const matchDate = new Date(m.iso_time);
                if (start && matchDate < start) return false;
                if (end && matchDate > end) return false;
                return prob(m) > 55 || avgGoalsPerGame(m) > 2.5; // Relaxed thresholds
            })
            .sort((a, b) => prob(b) - prob(a))
            .map((m) => ({
                ...m,
                tip: prediction(m),
            }));
    }

    // Limit to requested number of matches
    userSmartCombo.value = filtered.slice(0, comboMatchCount.value);
    isGenerating.value = false;
};

function getTipReason(match, type = "best") {
    const highestProb = getHighestProbability(match);
    const goalSum = (match.home_gf || 0) + (match.away_gf || 0);
    const rankGap = Math.abs((match.home_rank || 0) - (match.away_rank || 0));

    if (type === "best") {
        if (highestProb >= 75) return "High confidence from model ";
        if (highestProb >= 65) return "Consistent team + strong form";
        return "Good value based on ranking and stats";
    }

    if (type === "goals") {
        if (goalSum >= 70) return "Both teams average high goals";
        if (match.home_gf >= 35 && match.away_gf >= 30) return "Strong attack on both sides";
        return "Scoring trend detected in last 5 games";
    }

    if (type === "mixed") {
        const tags = getMatchTags(match);
        if (tags.includes("🎯 Over 2.5 Goals"))
            return "Over trend supported by team GF stats";
        if (tags.includes("🎯 Consistent Scorer"))
            return "Scoring form: one side scores regularly";
        if (tags.includes("🛡️ Safe Pick")) return "Wide point gap: safe pick scenario";
        if (tags.includes("😮 Upset Alert")) return "Low-ranked team could surprise";
        return "Smart logic based on combined tags";
    }

    return "Based on model prediction and smart filters";
}

const selectedTags = ref([]);
const smartTagOptions = [
    { label: "📉 Home Negative GD", value: "📉 Home Negative GD" },
    { label: "📉 Away Negative GD", value: "📉 Away Negative GD" },
    /*   { label: '📉 Both Teams Negative GD', value: '📉 Both Teams Negative GD' },
    { label: '🎯 Consistent Scorer', value: '🎯 Consistent Scorer' },
    { label: '🔥 Streak Team', value: '🔥 Streak Team' },
    { label: '⚡ Attacking Momentum', value: '⚡ Attacking Momentum' },
    { label: '😮 Upset Alert', value: '😮 Upset Alert' },
    { label: '🎯 Over 2.5 Goals', value: '🎯 Over 2.5 Goals' },
    { label: '🛡️ Safe Pick', value: '🛡️ Safe Pick' },
    { label: '🌅 Morning Kickoff', value: '🌅 Morning Kickoff' },
  { label: '🌤️ Afternoon Match', value: '🌤️ Afternoon Match' },
  { label: '🌙 Evening Clash', value: '🌙 Evening Clash' }, */
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
const todayISODate = new Date().toISOString().split("T")[0];

const dateFilter = ref(todayISODate);
const startDateFilter = ref(todayISODate);
const endDateFilter = ref(todayISODate);
const minProbability = ref("0");
const leagueFilter = ref("");
const topTeamsFilter = ref("false");
const sortOption = ref("highest-prob");
const timeFilter = ref("");
const pickFilter = ref("");

// Sample data to ensure matches show up
const sampleMatches = [];
const mustWatchMatches = computed(() =>
    filteredMatches.value
        .filter((m) => {
            const home = Number(m.home_rank || 999);
            const away = Number(m.away_rank || 999);

            // 🎯 Match où une équipe du top 3 affronte une équipe classée après la 8e place
            return (home <= 3 && away > 8) || (away <= 3 && home > 8);
        })
        .sort((a, b) => {
            const aScore = getHighestProbability(a) - Math.abs(a.home_rank - a.away_rank);
            const bScore = getHighestProbability(b) - Math.abs(b.home_rank - b.away_rank);
            return bScore - aScore;
        })
        .slice(0, 9999)
);

const resetComboBuilder = () => {
    comboStartDate.value = "";
    comboEndDate.value = "";
    comboMatchCount.value = 5;
    comboStrategy.value = "best";
    userSmartCombo.value = [];

    // Optionally scroll back to top of modal or focus UI
    setTimeout(() => {
        const modal = document.querySelector(".smart-combo-modal");
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
    return filteredMatches.value.filter(
        (match) => match.prob_1 >= 70 || match.prob_x >= 70 || match.prob_2 >= 70
    ).length;
});

const highConfidencePercentage = computed(() => {
    if (filteredMatches.value.length === 0) return 0;
    return Math.round(
        (highConfidenceMatchesCount.value / filteredMatches.value.length) * 100
    );
});

const topTeamMatchesCount = computed(() => {
    return filteredMatches.value.filter(
        (match) => isTopRanked(match.home_rank) || isTopRanked(match.away_rank)
    ).length;
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

    if (leagueFilter.value) {
        result = result.filter((match) => match.league === leagueFilter.value);
    }
    // Filter by Minimum Home GF
    if (minHomeGF.value > 0) {
        result = result.filter((match) => {
            return parseInt(match.home_gf || 0) >= minHomeGF.value;
        });
    }

    // Filter by Minimum Away GF
    if (minAwayGF.value > 0) {
        result = result.filter((match) => {
            return parseInt(match.away_gf || 0) >= minAwayGF.value;
        });
    }

    // Filter by Minimum Home GA
    if (minHomeGA.value > 0) {
        result = result.filter((match) => {
            return parseInt(match.home_ga || 0) >= minHomeGA.value;
        });
    }

    // Filter by Minimum Away GA
    if (minAwayGA.value > 0) {
        result = result.filter((match) => {
            return parseInt(match.away_ga || 0) >= minAwayGA.value;
        });
    }

    if (timeRangeStart.value && timeRangeEnd.value) {
        const [startHour, startMinute] = timeRangeStart.value.split(":").map(Number);
        const [endHour, endMinute] = timeRangeEnd.value.split(":").map(Number);

        const startTotal = startHour * 60 + startMinute;
        const endTotal = endHour * 60 + endMinute;

        result = result.filter((match) => {
            const timePart = match.time_str?.split(" ")[1]; // extract "14:30" from "2025-04-12 14:30"
            if (!timePart) return false;

            const [matchHour, matchMinute] = timePart.split(":").map(Number);
            const matchTotal = matchHour * 60 + matchMinute;

            return matchTotal >= startTotal && matchTotal <= endTotal;
        });
    }

    // Filter by Home Win Rate, Away Win Rate, and Away Loss Rate
    result = result.filter((match) => {
        const homeWin = getHomeWinRate(match);
        const homeLoss = getHomeLossRate(match); // 🔥 ajoute cette ligne

        const awayWin = getAwayWinRate(match);
        const awayLoss = getAwayLossRate(match);

        return (
            homeWin >= homeWinRateMin.value &&
            homeWin <= homeWinRateMax.value &&
            homeLoss >= homeLossRateMin.value && // 🔥 ajoute cette condition
            homeLoss <= homeLossRateMax.value && // 🔥 ajoute cette condition
            awayWin >= awayWinRateMin.value &&
            awayWin <= awayWinRateMax.value &&
            awayLoss >= awayLossRateMin.value &&
            awayLoss <= awayLossRateMax.value
        );
    });

    // Filter by High Scoring Team: Only include matches where at least one team has scored more goals than the selected value.
    if (minGF.value) {
        result = result.filter((match) => {
            return (
                parseInt(match.home_gf || 0) > minGF.value ||
                parseInt(match.away_gf || 0) > minGF.value
            );
        });
    }
    if (minGP.value) {
        result = result.filter((match) => {
            return (
                parseInt(match.home_gp || 0) > minGP.value &&
                parseInt(match.away_gp || 0) > minGP.value
            );
        });
    }
    // Filter by Negative GD: Only include matches where at least one team has a goal difference below the selected maximum.
    if (maxNegativeGD.value < 0) {
        result = result.filter((match) => {
            return (
                parseInt(match.home_gd || 0) < maxNegativeGD.value ||
                parseInt(match.away_gd || 0) < maxNegativeGD.value
            );
        });
    }
    if (winGapMin.value > 0) {
        result = result.filter((match) => {
            const homeW = parseInt(match.home_w || 0);
            const awayW = parseInt(match.away_w || 0);
            return Math.abs(homeW - awayW) >= winGapMin.value;
        });
    }

    //h/a filter
    if (haScoreFilter.value !== "all") {
        result = result.filter((match) => {
            const haScore = getHomeAwayPerformanceScore(match); // Returns percentage

            switch (haScoreFilter.value) {
                case "0-30":
                    return haScore >= 0 && haScore < 30;
                case "30-60":
                    return haScore >= 30 && haScore < 60;
                case "60-70":
                    return haScore >= 60 && haScore < 70;
                case "70-80":
                    return haScore >= 70 && haScore < 80;
                case "80-100":
                    return haScore >= 80 && haScore <= 100;
                default:
                    return true;
            }
        });
    }

    // Filter by odds
    if (onlyWithOdds.value) {
        result = result.filter(
            (match) => !!match.live_odds && match.live_odds !== "-" && match.live_odds !== ""
        );
    }
    // Result Prediction (1/X/2) filter
    if (pickFilter.value) {
        result = result.filter((match) => match.prediction === pickFilter.value);
    }

    // Filter by stats (basic check: has GP + PTS for both sides)
    if (onlyWithStats.value) {
        result = result.filter(
            (match) => match.home_gp && match.away_gp && match.home_pts && match.away_pts
        );
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
        const [startHour, startMinute] = matchTimeFrom.value.split(":").map(Number);
        const [endHour, endMinute] = matchTimeTo.value.split(":").map(Number);

        result = result.filter((match) => {
            if (!match.time_str) return false;
            const [matchHour, matchMinute] = match.time_str.split(":").map(Number);

            const matchTime = matchHour * 60 + matchMinute;
            const startTime = startHour * 60 + startMinute;
            const endTime = endHour * 60 + endMinute;

            return matchTime >= startTime && matchTime <= endTime;
        });
    }

    if (performanceScoreFilter.value !== "all") {
        result = result.filter((match) => {
            const performanceScore = getHomeAwayPerformanceScore(match);

            // Filter based on selected score ranges
            if (performanceScoreFilter.value === "60-75") {
                return performanceScore >= 60 && performanceScore < 75;
            } else if (performanceScoreFilter.value === "75-100") {
                return performanceScore >= 75 && performanceScore <= 100;
            } else if (performanceScoreFilter.value === "below-60") {
                return performanceScore < 60;
            }
            return true; // If filter is "all", return all
        });
    }

    if (showNotStarted.value) {
        const now = new Date();

        // 1. Filter only future matches
        result = result.filter((match) => {
            if (!match.time_str) return false;

            const [day, month, rest] = match.time_str.split("/");
            if (!rest) return false;

            const [year, time] = rest.split(" ");
            if (!time) return false;

            const [hour, minute] = time.split(":");
            const matchDate = new Date(`${year}-${month}-${day}T${hour}:${minute}:00`);

            return matchDate > now;
        });

        // 2. Sort future matches by upcoming time
        result.sort((a, b) => {
            const toDate = (m) => {
                const [d, mo, r] = m.time_str.split("/");
                const [y, t] = r.split(" ");
                const [h, min] = t.split(":");
                return new Date(`${y}-${mo}-${d}T${h}:${min}:00`);
            };
            return toDate(a) - toDate(b); // Ascending order
        });
    }

    // Time of Day filter
    if (timeFilter.value) {
        result = result.filter((match) => {
            if (!match.time_str) return false;
            const [hours] = match.time_str.split(":").map(Number);
            if (timeFilter.value === "morning") return hours >= 0 && hours < 12;
            if (timeFilter.value === "afternoon") return hours >= 12 && hours < 18;
            if (timeFilter.value === "evening") return hours >= 18 && hours <= 23;
            return true;
        });
    }
    if (selectedTags.value.length > 0) {
        result = result.filter((match) => {
            const tags = getMatchTags(match);
            return selectedTags.value.every((tag) => tags.includes(tag));
        });
    }

    if (selectedTags.value.includes("negative_gd")) {
        result = result.filter((match) => {
            return match.home_gd < 0 || match.away_gd < 0;
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
        result = result.filter(
            (match) =>
                match.prob_1 >= minProb || match.prob_x >= minProb || match.prob_2 >= minProb
        );
    }

    // League filter
    if (leagueFilter.value) {
        result = result.filter((match) => match.league === leagueFilter.value);
    }

    // Top teams filter
    if (topTeamsFilter.value !== "false") {
        const maxRank = parseInt(topTeamsFilter.value); // Get the selected rank (1 to 5)

        result = result.filter((match) => {
            return (
                isTopRanked(match.home_rank, maxRank) || isTopRanked(match.away_rank, maxRank)
            );
        });
    }

    // Apply sorting
    if (sortOption.value === "highest-prob") {
        result.sort((a, b) => {
            const aMax = Math.max(a.prob_1, a.prob_x, a.prob_2);
            const bMax = Math.max(b.prob_1, b.prob_x, b.prob_2);
            return bMax - aMax;
        });
    } else if (sortOption.value === "time") {
        result.sort((a, b) => new Date(a.iso_time) - new Date(b.iso_time));
    } else if (sortOption.value === "league") {
        result.sort((a, b) => a.league.localeCompare(b.league));
    }

    return result;
});
const onlineUsers = ref(0);
function setToday() {
    const today = new Date().toISOString().split("T")[0];
    startDateFilter.value = today;
    endDateFilter.value = today;
}

function setTomorrow() {
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    const isoTomorrow = tomorrow.toISOString().split("T")[0];
    startDateFilter.value = isoTomorrow;
    endDateFilter.value = isoTomorrow;
}
function checkVIPCode() {
    if (vipCodeInput.value === "06store") {
        // Correct VIP Code
        localStorage.setItem("vipCode", "06store");
        isVIP.value = true;
        vipError.value = "";
    } else {
        // Wrong Code
        vipError.value = "Incorrect code, try again.";
        alert("🚫 Incorrect VIP Code");
    }
}

onMounted(() => {
    // 1. VIP Access Check
    if (localStorage.getItem("vipCode") === "06store") {
        isVIP.value = true;
    } else {
        isVIP.value = false;
    }

    // 2. Simulate random active users
    onlineUsers.value = Math.floor(20 + Math.random() * 100);

    setInterval(() => {
        onlineUsers.value = Math.floor(20 + Math.random() * 100);
    }, 30000);
});

// Computed: Best Bets
const bestBets = computed(() => {
    if (filteredMatches.value.length === 0) return [];

    const highProbMatches = filteredMatches.value.filter(
        (match) => match.prob_1 > 70 || match.prob_x > 70 || match.prob_2 > 70
    );

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
function getFormTrend(match, side = "home") {
    const w = parseInt(match[`${side}_w`] || 0);
    const d = parseInt(match[`${side}_d`] || 0);
    const l = parseInt(match[`${side}_l`] || 0);

    const trend = [];
    for (let i = 0; i < w; i++) trend.push("✅");
    for (let i = 0; i < d; i++) trend.push("➖");
    for (let i = 0; i < l; i++) trend.push("❌");

    return trend.slice(0, 5).join(" / ");
}

// Combo Builder State
// Combo Builder State
const comboRisk = ref("conservative");
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

    const sorted = eligible.sort(
        (a, b) => getHighestProbability(b) - getHighestProbability(a)
    );
    smartCombo.value = sorted.slice(0, comboSize.value);
};

// Combo stats
const comboConfidence = computed(() => {
    if (!smartCombo.value.length) return 0;
    const probs = smartCombo.value.map((m) => getHighestProbability(m) / 100);
    return Math.round(probs.reduce((acc, p) => acc * p, 1) * 100);
});
function getHomeAwayPerformanceScore(match) {
    const homeWinRate = match.home_w / match.home_gp || 0;
    const awayLossRate = match.away_l / match.away_gp || 0;
    const homeGF = match.home_gf / match.home_gp || 0;
    const awayGA = match.away_ga / match.away_gp || 0;

    const score =
        homeWinRate * 0.4 + (homeGF / 3) * 0.3 + awayLossRate * 0.2 + (awayGA / 2.5) * 0.1;

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
    const highest = getHighestProbability(match);

    const isClose = (a, b) => Math.abs(a - b) < 0.01;

    if (isClose(highest, match.prob_1)) return "1";
    if (isClose(highest, match.prob_x)) return "X";
    if (isClose(highest, match.prob_2)) return "2";

    return "?";
};

const formatDate = (dateString) => {
    const options = { weekday: "long", year: "numeric", month: "long", day: "numeric" };
    return new Date(dateString).toLocaleDateString("en-US", options);
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
    dateFilter.value = "";
    startDateFilter.value = todayISODate; // reset to today
    endDateFilter.value = todayISODate; // reset to today
    minProbability.value = "0";
    leagueFilter.value = "";
    topTeamsFilter.value = "false";
    sortOption.value = "highest-prob";
    timeFilter.value = "";
    minOdds.value = "";
    maxOdds.value = "";
    selectedTags.value = [];
    performanceScoreFilter.value = "all";
    matchTimeFrom.value = "";
    matchTimeTo.value = "";
    pickFilter.value = "";
    onlyWithOdds.value = false;
    onlyWithStats.value = false;
    minHomeGF.value = 0;
    minAwayGF.value = 0;
    minHomeGA.value = 0;
    minAwayGA.value = 0;

    // Range Sliders
    minGP.value = 0;
    maxNegativeGD.value = 0;
    minGF.value = 0;
    winGapMin.value = 0;

    // Time of Day Range
    timeRangeStart.value = "";
    timeRangeEnd.value = "";

    // Home/Away Win/Loss Rates
    homeWinRateMin.value = 0;
    homeWinRateMax.value = 100;
    homeLossRateMin.value = 0;
    homeLossRateMax.value = 100;
    awayWinRateMin.value = 0;
    awayWinRateMax.value = 100;
    awayLossRateMin.value = 0;
    awayLossRateMax.value = 100;

    // Special filters
    haScoreFilter.value = "all";
    showNotStarted.value = false;
};

function getMatchTags(match) {
    const tags = [];

    // 1. 📊 Extract data safely (parseInt + fallback to 0)
    const hGF = parseInt(match.home_gf || 0); // Home Goals For
    const hGA = parseInt(match.home_ga || 0); // Home Goals Against
    const aGF = parseInt(match.away_gf || 0); // Away Goals For
    const aGA = parseInt(match.away_ga || 0); // Away Goals Against

    const hW = parseInt(match.home_w || 0); // Home Wins
    const hL = parseInt(match.home_l || 0); // Home Losses
    const aW = parseInt(match.away_w || 0); // Away Wins
    const aL = parseInt(match.away_l || 0); // Away Losses

    const hPts = parseInt(match.home_pts || 0);
    const aPts = parseInt(match.away_pts || 0);

    const homeRank = parseInt(match.home_rank || 0);
    const awayRank = parseInt(match.away_rank || 0);

    const totalGF = hGF + aGF;
    const totalGA = hGA + aGA;
    const highestProb = getHighestProbability(match); // returns max(prob_1, prob_x, prob_2)

    // 11. 🕒 Time of Day Tags
    if (match.time_str) {
        const timePart = match.time_str.split(" ")[1]; // e.g., "14:30"
        if (timePart) {
            const hour = parseInt(timePart.split(":")[0]);
            if (!isNaN(hour)) {
                if (hour < 12) {
                    tags.push("🌅 Morning Kickoff");
                } else if (hour < 18) {
                    tags.push("🌤️ Afternoon Match");
                } else {
                    tags.push("🌙 Evening Clash");
                }
            }
        }
    }

    // 2. 💡 Confidence Level
    if (highestProb >= 75) {
        tags.push(`💡 Pick Confidence: High — ${highestProb}%`);
    } else if (highestProb >= 60) {
        tags.push("🧠 AI Confidence: Medium");
    }

    // 3. 📉 Negative Goal Difference
    if (match.home_gd < 0 && match.away_gd < 0) {
        tags.push("📉 Both Teams Negative GD");
    } else if (match.home_gd < 0) {
        tags.push("📉 Home Negative GD");
    } else if (match.away_gd < 0) {
        tags.push("📉 Away Negative GD");
    }

    // 4. ⚡ Attacking Momentum (if total GF much higher than GA)
    if (totalGF > totalGA + 10) {
        tags.push("⚡ Attacking Momentum");
    }

    // 5. 😮 Upset Alert (lower ranked home team with high win prob)
    if (homeRank > awayRank && match.prob_1 > 60) {
        tags.push("😮 Upset Alert");
    }

    // 6. 🎯 Consistent Scorer
    if (hGF > 40 || aGF > 40) {
        tags.push("🎯 Consistent Scorer");
    }

    // 7. 🔥 Streak Team (5+ wins)
    if (hW >= 5 || aW >= 5) {
        tags.push("🔥 Streak Team");
    }

    // 8. 📉 Poor Form
    if (match.home_gp >= 5 && hL > hW) {
        tags.push("📉 Home Poor Form");
    }
    if (match.away_gp >= 5 && aL > aW) {
        tags.push("📉 Away Poor Form");
    }

    // 9. 🎯 Over 2.5 Goals potential
    if (totalGF + totalGA > 70 || (hGF > 30 && aGF > 30)) {
        tags.push("🎯 Over 2.5 Goals");
    }

    // 10. 🛡️ Safe Pick (big point difference)
    if (Math.abs(hPts - aPts) > 20 && (hPts > 0 || aPts > 0)) {
        tags.push("🛡️ Safe Pick");
    }

    return tags;
}

// Fetch Matches
const fetchData = async () => {
    loading.value = true;
    error.value = null;
    try {
        // Try to fetch from API first
        const res = await axios.get("/forebet-data");
        matches.value = res.data.map((match) => ({
            ...match,
            league: match.league, // ✅ Use the value directly from backend
        }));
    } catch (e) {
        console.error("Error loading predictions", e);
        // If API fails, use sample data
        matches.value = sampleMatches.map((match) => ({
            ...match,
            league: match.game.split(" - ")[0] || match.league,
        }));
        error.value = "Using sample data - API unavailable";
    } finally {
        loading.value = false;
    }
};
const toggleTagFilter = (tag) => {
    const index = selectedTags.value.indexOf(tag);
    if (index === -1) selectedTags.value.push(tag);
    else selectedTags.value.splice(index, 1);
};

// Quick Load Combo Functions
function loadStrongHomeWin() {
    homeWinRateMin.value = 65;
    homeWinRateMax.value = 100;
    homeLossRateMin.value = 0;
    homeLossRateMax.value = 20;
    awayWinRateMin.value = 0;
    awayWinRateMax.value = 40;
    awayLossRateMin.value = 50;
    awayLossRateMax.value = 100;
    // minOdds.value = 1.3;
    // maxOdds.value = 3.0;
}

function loadStrongAwayWin() {
    homeWinRateMin.value = 0;
    homeWinRateMax.value = 50;
    homeLossRateMin.value = 40;
    homeLossRateMax.value = 100;
    awayWinRateMin.value = 50;
    awayWinRateMax.value = 100;
    awayLossRateMin.value = 0;
    awayLossRateMax.value = 40;
    // minOdds.value = 1.3;
    //maxOdds.value = 4.0;
}

function loadOverGoalsBomb() {
    homeWinRateMin.value = 30;
    homeWinRateMax.value = 70;
    homeLossRateMin.value = 30;
    homeLossRateMax.value = 70;
    awayWinRateMin.value = 30;
    awayWinRateMax.value = 70;
    awayLossRateMin.value = 30;
    awayLossRateMax.value = 70;
    minGF.value = 40;
    //minOdds.value = 1.3;
    //maxOdds.value = 3.5;
}

function loadUltraSafeLock() {
    homeWinRateMin.value = 65;
    homeWinRateMax.value = 100;
    homeLossRateMin.value = 0;
    homeLossRateMax.value = 20;
    awayLossRateMin.value = 50;
    awayLossRateMax.value = 100;
    winGapMin.value = 10;
    //minOdds.value = 1.2;
    //maxOdds.value = 2.5;
}

function loadHomeCollapse() {
    homeWinRateMin.value = 0;
    homeWinRateMax.value = 30;
    homeLossRateMin.value = 60;
    homeLossRateMax.value = 100;
    awayWinRateMin.value = 40;
    awayWinRateMax.value = 70;
    awayLossRateMin.value = 0;
    awayLossRateMax.value = 50;
    //minOdds.value = 1.4;
    //maxOdds.value = 4.0;
}
function autoCombo() {
    // Compter les matchs avec Home Win Rate > 70%
    const strongHome = filteredMatches.value.filter((m) => getHomeWinRate(m) > 70).length;
    // Compter les Away Wins > 55%
    const strongAway = filteredMatches.value.filter((m) => getAwayWinRate(m) > 55).length;
    // Compter les matchs Over 2.5 buts
    const highGoals = filteredMatches.value.filter((m) => getAvgGoals(m) > 2.8).length;

    // Décider du meilleur combo
    if (strongHome >= strongAway && strongHome >= highGoals) {
        loadStrongHomeWin(); // Appelle la fonction déjà faite
        alert("🏡 Strong Home Win Combo Chargé !");
    } else if (strongAway >= strongHome && strongAway >= highGoals) {
        loadStrongAwayWin();
        alert("🚗 Strong Away Win Combo Chargé !");
    } else {
        loadOverGoalsBomb();
        alert("🎯 Over Goals Bomb Combo Chargé !");
    }
}
function loadAwayCollapse() {
    homeWinRateMin.value = 40;
    homeWinRateMax.value = 100;
    homeLossRateMin.value = 0;
    homeLossRateMax.value = 50;
    awayWinRateMin.value = 0;
    awayWinRateMax.value = 30;
    awayLossRateMin.value = 60;
    awayLossRateMax.value = 100;
    // minOdds.value = 1.3;
    //maxOdds.value = 3.0;
}
// Draw Focus Combo - Matchs très équilibrés
function loadDrawFocus() {
    homeWinRateMin.value = 30;
    homeWinRateMax.value = 70;
    homeLossRateMin.value = 30;
    homeLossRateMax.value = 70;
    awayWinRateMin.value = 30;
    awayWinRateMax.value = 70;
    awayLossRateMin.value = 30;
    awayLossRateMax.value = 70;
    //minOdds.value = 2.5;
    // maxOdds.value = 4.0;
}
function loadCrazyGoalFest() {
    minGF.value = 40;
    minHomeGA.value = 30;
    minAwayGA.value = 30;
}
function loadStrongOver25Goals() {
    minGF.value = 50; // Total goals for must be high
    minHomeGA.value = 20; // Home team concedes some goals
    minAwayGA.value = 20; // Away team concedes some goals
    minAvgGoals.value = 2.7; // Minimum average goals per match: 2.7
}
function loadMonsterOver35Goals() {
    minGF.value = 60; // Super high scoring teams
    minHomeGA.value = 30; // Home concedes enough
    minAwayGA.value = 30; // Away concedes enough
    minAvgGoals.value = 3.5; // Minimum average goals per match: 3.5
}
// Strong GG Combo - Strong both teams scoring
function loadStrongGG() {
    homeWinRateMin.value = 40;
    homeWinRateMax.value = 80;
    homeLossRateMin.value = 20;
    homeLossRateMax.value = 60;
    awayWinRateMin.value = 40;
    awayWinRateMax.value = 80;
    awayLossRateMin.value = 20;
    awayLossRateMax.value = 60;
    minGF.value = 45; // More goals for both teams
    minHomeGA.value = 30;
    minAwayGA.value = 30;
}

// Monster GG Combo - Very aggressive both teams scoring
function loadMonsterGG() {
    homeWinRateMin.value = 30;
    homeWinRateMax.value = 90;
    homeLossRateMin.value = 20;
    homeLossRateMax.value = 70;
    awayWinRateMin.value = 30;
    awayWinRateMax.value = 90;
    awayLossRateMin.value = 20;
    awayLossRateMax.value = 70;
    minGF.value = 55; // Even higher goal scoring
    minHomeGA.value = 40;
    minAwayGA.value = 40;
    minAvgGoals.value = 3.0; // Minimum 3 goals per match
}

function loadDefenseWall() {
    minGF.value = 0;
    minHomeGA.value = 0;
    minAwayGA.value = 0;
    homeWinRateMin.value = 50;
    homeWinRateMax.value = 80;
    awayWinRateMin.value = 50;
    awayWinRateMax.value = 80;
}
function loadSafeFavorites() {
    winGapMin.value = 15; // Big difference in wins
    minProbability.value = 70; // High win probability
}

// BTTS Focus Combo - Les deux équipes marquent
function loadBTTSFocus() {
    homeWinRateMin.value = 30;
    homeWinRateMax.value = 80;
    homeLossRateMin.value = 20;
    homeLossRateMax.value = 70;
    awayWinRateMin.value = 30;
    awayWinRateMax.value = 80;
    awayLossRateMin.value = 20;
    awayLossRateMax.value = 70;
    minGF.value = 40; // Minimum goals for
    //minOdds.value = 1.30;
    //maxOdds.value = 3.0;
}
function loadCompBot() {
    const filtered = matches.value.filter((match) => {
        const homeWinRate =
            ((match.home_form?.wins || 0) /
                ((match.home_form?.wins || 0) +
                    (match.home_form?.draws || 0) +
                    (match.home_form?.losses || 0))) *
            100;
        const awayWinRate =
            ((match.away_form?.wins || 0) /
                ((match.away_form?.wins || 0) +
                    (match.away_form?.draws || 0) +
                    (match.away_form?.losses || 0))) *
            100;
        const maxWinRate = Math.max(homeWinRate, awayWinRate);

        const oddsHome = match.odds?.full_time_result?.home;
        const oddsAway = match.odds?.full_time_result?.away;

        return (
            maxWinRate >= 60 &&
            ((oddsHome && oddsHome >= 1.3 && oddsHome <= 2.0) ||
                (oddsAway && oddsAway >= 1.3 && oddsAway <= 2.0))
        );
    });

    const homeWinMatches = filtered
        .filter((match) => {
            const oddsHome = match.odds?.full_time_result?.home;
            return oddsHome && oddsHome >= 1.3 && oddsHome <= 2.0;
        })
        .slice(0, 1); // 1 Home Win

    const awayWinMatches = filtered
        .filter((match) => {
            const oddsAway = match.odds?.full_time_result?.away;
            return oddsAway && oddsAway >= 1.3 && oddsAway <= 2.0;
        })
        .slice(0, 1); // 1 Away Win

    const ggMatches = filtered
        .filter((match) => {
            const homeAvg = match.home_form?.avg_goals_scored || 0;
            const awayAvg = match.away_form?.avg_goals_scored || 0;
            return homeAvg >= 1.2 && awayAvg >= 1.2;
        })
        .slice(0, 1); // 1 GG Match

    const over25Matches = filtered
        .filter((match) => {
            return (match.avg_goals || 0) >= 2.5;
        })
        .slice(0, 1); // 1 Over 2.5 Match

    selectedMatches.value = [
        ...homeWinMatches,
        ...awayWinMatches,
        ...ggMatches,
        ...over25Matches,
    ];
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
        const script1 = document.createElement("script");
        script1.type = "text/javascript";
        script1.innerHTML = `
      atOptions = {
        'key': 'c68164d29f3923a1e7a7ff9be7d2e396',
        'format': 'iframe',
       'height' : 50,
		'width' : 320,
		'params' : {}
      };
    `;
        const script2 = document.createElement("script");
        script2.type = "text/javascript";
        script2.src =
            "//www.highperformanceformat.com/c68164d29f3923a1e7a7ff9be7d2e396/invoke.js";
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
