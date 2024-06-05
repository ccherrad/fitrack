<script setup lang="ts">
import type { Table } from '@tanstack/vue-table'
import { computed, ref} from 'vue'
import { PlusIcon } from '@radix-icons/vue'

interface DataTableCreateRowProps {
  create: Object
}

const props = defineProps<DataTableCreateRowProps>()
const open = ref(false)
const emit = defineEmits(['submitted']);

const handleSubmitted = () => {
  open.value = false;
  emit('submitted');
};
</script>

<template>
  <Dialog v-model:open="open">
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
      <component :is="create" @submitted="handleSubmitted"/>
    </DialogContent>
  </Dialog>
</template>
