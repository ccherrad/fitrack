<script setup lang="ts" generic="T extends BaseModel">
import type { Row } from "@tanstack/vue-table";
import { DotsHorizontalIcon } from "@radix-icons/vue";
import AthleteService from "@/services/athlete";
import type { BaseModel } from "./DataTable.vue";

interface DataTableRowActionsProps<T> {
  row: Row<T>;
}


const props = defineProps<DataTableRowActionsProps<T>>();

const emit = defineEmits(["athleteDeleted"]);

async function handleDelete() {
  const athleteId = props.row.getValue<number>("id");
  await AthleteService.delete(athleteId);
  emit("athleteDeleted");
}

</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger as-child>
      <Button
        variant="ghost"
        class="flex h-8 w-8 p-0 data-[state=open]:bg-muted"
      >
        <DotsHorizontalIcon class="h-4 w-4" />
        <span class="sr-only">Open menu</span>
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="end" class="w-[160px]">
      <DropdownMenuItem>Edit</DropdownMenuItem>
      <DropdownMenuItem @click="handleDelete">
        Delete
        <DropdownMenuShortcut>⌘⌫</DropdownMenuShortcut>
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
