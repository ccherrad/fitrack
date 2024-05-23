<script setup lang="ts">
import * as z from 'zod'
import { h } from 'vue'
import { Button } from '@/components/ui/button'
import { toast } from '@/components/ui/toast'
import { AutoForm, AutoFormField } from '@/components/ui/auto-form'
import athleteService from '~/services/athlete';


const schema = z.object({
  fullname: z
    .string({
      required_error: 'Fullname is required.',
    })
    .min(2, {
      message: 'Username must be at least 2 characters.',
    }),

  birthday: z.coerce.date().optional(),

  bio: z
    .string()
    .min(10, {
      message: 'Bio must be at least 10 characters.',
    })
    .max(160, {
      message: 'Bio must not be longer than 30 characters.',
    })
    .optional(),
})

function onSubmit(values: Record<string, any>) {
  const transformedValues = { ...values };
  if (transformedValues.birthday) {
    transformedValues.dob = new Date(transformedValues.birthday).toISOString();
    delete transformedValues.birthday;
  }
  athleteService.create(transformedValues);
}
</script>

<template>
  <AutoForm
    class="w-2/3 space-y-6"
    :schema="schema"
    :field-config="{
      birthday: {
        description: 'We need your birthday to send you a gift.',
      },

      bio: {
        component: 'textarea',
      },
    }"
    @submit="onSubmit"
  >
    <Button type="submit">
      Submit
    </Button>
  </AutoForm>
</template>
