<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { columns } from '@/components/columns'
import athleteService from '~/services/athlete';
import Create from './[id].vue';

const athletes = ref([])

const fetchAthletes = async () => {
  try {
    athletes.value = await athleteService.getAll();
  } catch (err) {
    console.log(err);
  }
};

onMounted(fetchAthletes)

</script>

<template>
  <div class="hidden flex-1 flex-col space-y-8 p-8 md:flex">
    <DataTable
      :data="athletes"
      :columns="columns"
      :create="Create"
      :service="athleteService"
      @newAdded="fetchAthletes"
      @athleteDeleted="fetchAthletes"
    />
  </div>
</template>
