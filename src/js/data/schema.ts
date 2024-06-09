import { z } from "zod";

// We're keeping a simple non-relational schema here.
// IRL, you will have a schema for your data models.
export const athleteSchema = z.object({
  id: z.string(),
  fullname: z.string(),
  dob: z.string(),
  label: z.string(),
});

export type Athlete = z.infer<typeof athleteSchema>
