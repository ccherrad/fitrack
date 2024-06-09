<script setup lang="ts">
import { cn } from "@/lib/utils";
import {
    PersonIcon,
    MagicWandIcon,
    DesktopIcon,
    TokensIcon,
} from "@radix-icons/vue";
</script>


<template>
  <div :class="cn('pb-12', $attrs.class ?? '')">
    <div class="space-y-4 py-4">
      <div class="px-3 py-2">
        <h2 class="mb-2 px-4 text-lg font-semibold tracking-tight">
          Workspace
        </h2>
        <div class="space-y-1">
        <Button variant="ghost" class="w-full justify-start">
            <TokensIcon class="mr-2 h-4 w-4" />
            Workouts
          </Button>
          <NuxtLink to="/athletes">
            <Button variant="secondary" class="w-full justify-start">
              <PersonIcon class="mr-2 h-4 w-4" />
              Athletes
            </Button>
          </NuxtLink>
          <Button variant="ghost" class="w-full justify-start">
            <TokensIcon class="mr-2 h-4 w-4" />
            Teams
          </Button>
          <Button variant="ghost" class="w-full justify-start">
            <DesktopIcon class="mr-2 h-4 w-4" />
            Monitoring
          </Button>
        </div>
      </div>
      <div class="px-3 py-2">
        <h2 class="mb-2 px-4 text-lg font-semibold tracking-tight">
          Library
        </h2>
        <div class="space-y-1">
          <Button variant="ghost" class="w-full justify-start">
            <MagicWandIcon class="mr-2 h-4 w-4" />
            Questionnaires
          </Button>
          <Button variant="ghost" class="w-full justify-start">
            <MagicWandIcon class="mr-2 h-4 w-4" />
            Exercises
          </Button>
        </div>
      </div>
    </div>
  </div>
</template>
