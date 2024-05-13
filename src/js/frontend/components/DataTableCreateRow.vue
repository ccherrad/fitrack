<script setup lang="ts">
import type { Table } from '@tanstack/vue-table'
import { computed } from 'vue'
import { type Task } from '@/data/schema'
import { PlusIcon } from '@radix-icons/vue'

interface DataTableCreateRowProps {
  table: Table<Task>
}

const props = defineProps<DataTableCreateRowProps>()

const columns = computed(() => props.table.getAllColumns()
  .filter(
    column =>
      typeof column.accessorFn !== 'undefined' && column.getCanHide(),
  ))
</script>

<template>
  <Dialog>
    <DialogTrigger as-child>
      <Button
        variant="outline"
        size="sm"
        class="ml-auto hidden h-8 lg:flex"
      >
        <PlusIcon class="mr-2 h-4 w-4" />
        Add
      </Button>
    </DialogTrigger>
    <DialogContent class="sm:max-w-[425px]">
      <DialogHeader>
        <DialogTitle>Add athlete</DialogTitle>
      </DialogHeader>
      <form class="w-2/3 space-y-6" @submit="onSubmit">
        <FormField v-slot="{ componentField }" name="fullname">
          <FormItem>
            <FormLabel>Fullname</FormLabel>
            <FormControl>
              <Input type="text" placeholder="John Doe" v-bind="componentField" />
            </FormControl>
          </FormItem>
        </FormField>
        <DialogFooter>
          <Button type="submit">
            Save changes
          </Button>
        </DialogFooter>
      </form>
    </DialogContent>
  </Dialog>
</template>
