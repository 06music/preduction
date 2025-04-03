<template>
  <div class="min-h-screen bg-gray-50 px-3 py-4 sm:px-6">
    <!-- Header -->
    <header class="mb-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Tunisia.svg"
            alt="Tunisia Flag"
            class="h-10 w-10 rounded-full border border-gray-300"
          />
          <div>
            <h1 class="text-2xl sm:text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-red-600 to-rose-500">
              🇹🇳 DimaRaba7
            </h1>
            <p class="text-sm text-gray-600 italic">توقعات كروية... عالطريقة التونسية ✨</p>
          </div>
        </div>

        <div class="hidden sm:flex gap-3">
          <button
            @click="fetchData"
            class="px-4 py-2 bg-white border border-gray-200 hover:border-red-300 rounded-lg text-sm font-medium shadow-sm"
          >
            🔄 Refresh
          </button>
          <button
            @click="showFilters = !showFilters"
            class="px-4 py-2 bg-white border border-gray-200 hover:border-red-300 rounded-lg text-sm font-medium shadow-sm"
          >
            ⚙️ {{ showFilters ? 'Hide Filters' : 'Show Filters' }}
          </button>
        </div>
      </div>
    </header>

    <!-- Floating Filter Button (Mobile) -->
    <div class="fixed bottom-4 right-4 z-50 sm:hidden">
      <button
        @click="showFilters = !showFilters"
        class="bg-red-600 text-white px-4 py-2 rounded-full shadow-lg hover:bg-red-700 transition"
      >
        {{ showFilters ? 'Hide Filters' : 'Filters' }}
      </button>
    </div>

    <!-- Filters -->
    <div v-if="showFilters" class="bg-white p-4 rounded-xl shadow-md mb-6 border border-gray-100">
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div>
          <label class="block text-sm font-medium mb-1">📅 Date</label>
          <input type="date" v-model="dateFilter" class="w-full rounded-md border-gray-200 shadow-sm text-sm" />
        </div>
        <div>
          <label class="block text-sm font-medium mb-1">📈 Min Probability</label>
          <select v-model="minProbability" class="w-full rounded-md border-gray-200 shadow-sm text-sm">
            <option value="0">Any %</option>
            <option value="50">50%+</option>
            <option value="60">60%+</option>
            <option value="70">70%+</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium mb-1">🏆 Top Teams Only</label>
          <select v-model="topTeamsFilter" class="w-full rounded-md border-gray-200 shadow-sm text-sm">
            <option value="false">All Teams</option>
            <option value="true">Top 3 Ranked Only</option>
          </select>
        </div>
      </div>
      <div class="mt-4 flex justify-end gap-2">
        <button @click="resetFilters" class="px-4 py-2 border rounded-lg text-sm">Reset</button>
        <button @click="applyFilters" class="px-4 py-2 bg-red-600 text-white rounded-lg text-sm">Apply</button>
      </div>
    </div>

    <!-- Match Cards -->
    <div v-if="filteredMatches.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div
        v-for="match in filteredMatches"
        :key="match.id"
        class="bg-white rounded-xl shadow hover:shadow-md transition border border-gray-200 p-4"
      >
        <div class="flex justify-between items-center mb-2">
          <div>
            <h3 class="font-semibold">{{ match.game }}</h3>
            <p class="text-xs text-gray-500">{{ match.league }}</p>
          </div>
          <span class="text-sm text-red-600">{{ match.time_str }}</span>
        </div>
        <div class="flex justify-between text-sm items-center">
          <div>
            <div class="font-bold">{{ match.home_team }}</div>
            <div class="text-xs text-gray-400">#{{ match.home_rank }}</div>
          </div>
          <div class="bg-red-100 text-red-800 px-2 py-1 rounded-full text-xs font-semibold">
            {{ match.prediction === '1' ? 'Home Win' : match.prediction === 'X' ? 'Draw' : 'Away Win' }}
          </div>
          <div class="text-right">
            <div class="font-bold">{{ match.away_team }}</div>
            <div class="text-xs text-gray-400">#{{ match.away_rank }}</div>
          </div>
        </div>

        <!-- Probabilities -->
        <div class="mt-4 space-y-2 text-xs">
          <div class="flex items-center gap-2">
            <span class="w-4">1</span>
            <div class="flex-1 bg-gray-200 rounded-full overflow-hidden h-2">
              <div class="h-full bg-green-500" :style="{ width: match.prob_1 + '%' }"></div>
            </div>
            <span>{{ match.prob_1 }}%</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-4">X</span>
            <div class="flex-1 bg-gray-200 rounded-full overflow-hidden h-2">
              <div class="h-full bg-yellow-400" :style="{ width: match.prob_x + '%' }"></div>
            </div>
            <span>{{ match.prob_x }}%</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-4">2</span>
            <div class="flex-1 bg-gray-200 rounded-full overflow-hidden h-2">
              <div class="h-full bg-red-500" :style="{ width: match.prob_2 + '%' }"></div>
            </div>
            <span>{{ match.prob_2 }}%</span>
          </div>
        </div>

        <a
          :href="match.match_url"
          target="_blank"
          class="block mt-4 text-center text-sm text-blue-600 hover:underline"
        >
          View Match →
        </a>
      </div>
    </div>

    <div v-else class="text-center text-gray-500 mt-20">
      No matches found. Try different filters.
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// State
const showFilters = ref(false)
const matches = ref([])
const dateFilter = ref('')
const minProbability = ref('0')
const topTeamsFilter = ref('false')

// Sample Data
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
  }
]

// Utils
const isTopRanked = (rank) => rank && [1, 2, 3].includes(Number(rank))
const getHighestProbability = (m) => Math.max(m.prob_1, m.prob_x, m.prob_2)
const isSameDay = (a, b) =>
  a.getFullYear() === b.getFullYear() &&
  a.getMonth() === b.getMonth() &&
  a.getDate() === b.getDate()

// Filtered Matches
const filteredMatches = computed(() => {
  let result = [...matches.value]
  if (dateFilter.value) {
    const selected = new Date(dateFilter.value)
    result = result.filter((m) => isSameDay(new Date(m.iso_time), selected))
  }
  if (minProbability.value > 0) {
    const min = Number(minProbability.value)
    result = result.filter((m) =>
      m.prob_1 >= min || m.prob_x >= min || m.prob_2 >= min
    )
  }
  if (topTeamsFilter.value === 'true') {
    result = result.filter((m) => isTopRanked(m.home_rank) || isTopRanked(m.away_rank))
  }
  return result
})

// Actions
const applyFilters = () => {
  showFilters.value = false
}
const resetFilters = () => {
  dateFilter.value = ''
  minProbability.value = '0'
  topTeamsFilter.value = 'false'
}
const fetchData = () => {
  matches.value = sampleMatches
}

onMounted(() => {
  fetchData()
})
</script>

<style scoped>
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
