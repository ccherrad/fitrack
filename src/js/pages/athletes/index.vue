<script setup lang="ts">
import { ref, onMounted } from "vue";
import athleteService from "~/services/athlete";
import Create from "./[id].vue";
import type { Athlete } from "~/schemas/athlete";
import { athleteTableColumns} from "~/schemas/athlete";

const athletes = ref<Athlete[]>([]);

const fetchAthletes = async () => {
  try {
    athletes.value = await athleteService.getAll();
  } catch (err) {
    console.log(err);
  }
};

onMounted(fetchAthletes);

</script>

<template>
  <div class="hidden flex-1 flex-col space-y-8 p-8 md:flex">
    <DataTable
      :data="athletes"
      :columns="athleteTableColumns"
      :create="Create"
      :service="athleteService"
      @new-added="fetchAthletes"
      @athlete-deleted="fetchAthletes"
    />
  </div>
</template>
