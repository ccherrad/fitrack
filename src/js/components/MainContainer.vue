<script setup lang="ts">
interface ContainerProps {
  message: string;
}

defineProps<ContainerProps>();
</script>


<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>
