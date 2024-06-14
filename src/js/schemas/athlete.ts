import { z } from "zod";
import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";

import { labels } from "../data/data";
import DataTableColumnHeader from "@/components/DataTableColumnHeader.vue";
import DataTableRowActions from "@/components/DataTableRowActions.vue";
import { Checkbox } from "@/components/ui/checkbox";
import { Badge } from "@/components/ui/badge";

export const athleteSchema = z.object({
  id: z.string(),
  fullname: z.string(),
  dob: z.string(),
});

export type Athlete = z.infer<typeof athleteSchema>

export const athleteTableColumns: ColumnDef<Athlete>[] = [
  {
    id: "select",
    header: ({ table }) => h(Checkbox,
      { "checked": table.getIsAllPageRowsSelected(), "onUpdate:checked": value => table.toggleAllPageRowsSelected(!!value), "ariaLabel": "Select all", "class": "translate-y-0.5" }),
    cell: ({ row }) => h(Checkbox,
      { "checked": row.getIsSelected(), "onUpdate:checked": value => row.toggleSelected(!!value), "ariaLabel": "Select row", "class": "translate-y-0.5" }),
    enableSorting: false,
    enableHiding: false,
  },
  {
    accessorKey: "id",
    header: ({ column }) => h(DataTableColumnHeader, { column, title: "#" }),
    cell: ({ row }) => h("div", { class: "w-20" }, row.getValue("id")),
    enableSorting: false,
    enableHiding: false,
  },
  {
    accessorKey: "fullname",
    header: ({ column }) => h(DataTableColumnHeader, { column, title: "Fullname" }),

    cell: ({ row }) => {
      const label = labels.find(label => label.value === row.original.label);

      return h("div", { class: "flex space-x-2" }, [
        label && h(Badge, { variant: "outline" }, label.label),
        h("span", { class: "max-w-[500px] truncate font-medium" }, row.getValue("fullname")),
      ]);
    },
  },
  {
    accessorKey: "dob",
    header: ({ column }) => h(DataTableColumnHeader, { column, title: "Date of birth" }),

    cell: ({ row }) => {
      const label = labels.find(label => label.value === row.original.label);

      return h("div", { class: "flex space-x-2" }, [
        label && h(Badge, { variant: "outline" }, label.label),
        h("span", { class: "max-w-[500px] truncate font-medium" }, row.getValue("dob")),
      ]);
    },
  },
  {
    id: "actions",
    cell: ({ row }) => h(DataTableRowActions, { row }),
  },
];
