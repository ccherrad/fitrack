<script setup lang="ts">
import * as z from "zod";
import { parseDate } from "@internationalized/date";
import { useForm } from "vee-validate";
import { toTypedSchema } from "@vee-validate/zod";
import { ref } from "vue";
import { Button } from "@/components/ui/button";
import { AutoForm } from "@/components/ui/auto-form";
import athleteService from "~/services/athlete";
import { athleteSchema } from "~/schemas/athlete";


const emit = defineEmits(["submitted"]);

const isEditMode = ref(false);
const athleteId = ref();

const athleteForm = useForm({
  validationSchema: toTypedSchema(athleteSchema),
});

onMounted(async () => {
  const route = useRoute();
  const id = route.params.id;
  if (id && !isNaN(Number(id))) {
    isEditMode.value = true;
    athleteId.value = Number(id);
    const athlete = await athleteService.get(Number(id));
    athleteForm.setFieldValue("first_name", athlete.first_name);
    athleteForm.setFieldValue("last_name", athlete.last_name);
    athleteForm.setFieldValue("birthday", parseDate(athlete.dob));
    athleteForm.setFieldValue("bio", athlete.bio);
  } else {
    isEditMode.value = false;
  }
});

async function onSubmit(values: Record<string, any>) {
  const transformedValues = { ...values };
  if (transformedValues.birthday) {
    transformedValues.dob = new Date(transformedValues.birthday).toISOString();
    delete transformedValues.birthday;
  }
  if (isEditMode.value) {
    await athleteService.update(athleteId.value, transformedValues);
  } else {
    await athleteService.create(transformedValues);
  }
  const router = useRouter();
  router.push("/athletes");
  emit("submitted");
}
</script>

<template>
  <AutoForm
    class="w-2/3 space-y-6"
    :schema="athleteSchema"
    :form="athleteForm"
    :field-config="{
      birthday: {
        label: 'Date of birth',
      },

      bio: {
        component: 'textarea',
      },
    }"
    @submit="onSubmit"
  >
    <Button type="submit">
      {{ isEditMode ? 'Update' : 'Submit' }}
    </Button>
  </AutoForm>
</template>
