<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { columns } from '@/components/columns'

// Define a reactive property to hold your tasks
const athletes = ref([])

onMounted(async () => {
  try {
    // Fetch the tasks from your API endpoint
    const response = await fetch('http://127.0.0.1:8000/api/v1/athletes/', {
      method: 'GET',
      headers: {
        'Accept': 'application/json', // Essential for indicating the expected response format
      }
    })

    if (!response.ok) {
      throw new Error('Failed to fetch tasks')
    }

    // Parse the JSON response
    const data = await response.json()
    
    // Assign the fetched data to the tasks ref
    athletes.value = data
  } catch (error) {
    console.error('Error fetching tasks:', error)
  }
})
</script>

<template>
  <div class="hidden flex-1 flex-col space-y-8 p-8 md:flex">
    <DataTable :data="athletes" :columns="columns" />
  </div>
</template>
