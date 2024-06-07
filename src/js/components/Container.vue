<script setup lang="ts">
import { cn } from "@/lib/utils";

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
