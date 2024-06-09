<script setup lang="ts" generic="T extends BaseModel">
import type {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
} from "@tanstack/vue-table";
import {
  FlexRender,
  getCoreRowModel,
  getFacetedRowModel,
  getFacetedUniqueValues,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useVueTable,
} from "@tanstack/vue-table";

import { ref } from "vue";
import DataTableToolbar from "./DataTableToolbar.vue";
import { valueUpdater } from "@/lib/utils";


export type BaseModel = {
  id: string;
};

interface DataTableProps {
  columns: ColumnDef<T>[];
  data: T[];
  create: any;
  service: any;
}
const props = defineProps<DataTableProps>();

const emit = defineEmits(["newAdded", "athleteDeleted"]);

const sorting = ref<SortingState>([]);
const columnFilters = ref<ColumnFiltersState>([]);
const columnVisibility = ref<VisibilityState>({});
const rowSelection = ref({});

const table = useVueTable<T>({
  get data() { return props.data; },
  get columns() { return props.columns; },
  state: {
    get sorting() { return sorting.value; },
    get columnFilters() { return columnFilters.value; },
    get columnVisibility() { return columnVisibility.value; },
    get rowSelection() { return rowSelection.value; },
  },
  enableRowSelection: true,
  onSortingChange: updaterOrValue => valueUpdater(updaterOrValue, sorting),
  onColumnFiltersChange: updaterOrValue => valueUpdater(updaterOrValue, columnFilters),
  onColumnVisibilityChange: updaterOrValue => valueUpdater(updaterOrValue, columnVisibility),
  onRowSelectionChange: updaterOrValue => valueUpdater(updaterOrValue, rowSelection),
  getCoreRowModel: getCoreRowModel(),
  getFilteredRowModel: getFilteredRowModel(),
  getPaginationRowModel: getPaginationRowModel(),
  getSortedRowModel: getSortedRowModel(),
  getFacetedRowModel: getFacetedRowModel(),
  getFacetedUniqueValues: getFacetedUniqueValues(),
});
</script>

<template>
  <div class="space-y-4">
    <DataTableToolbar :table="table" :create="create" @submitted="emit('newAdded')"/>
    <div class="rounded-md border">
      <Table>
        <TableHeader>
          <TableRow v-for="headerGroup in table.getHeaderGroups()" :key="headerGroup.id">
            <TableHead v-for="header in headerGroup.headers" :key="header.id">
              <FlexRender v-if="!header.isPlaceholder" :render="header.column.columnDef.header" :props="header.getContext()" />
            </TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <template v-if="table.getRowModel().rows?.length">
            <TableRow
              v-for="row in table.getRowModel().rows"
              :key="row.id"
              :data-state="row.getIsSelected() && 'selected'"
            >
              <TableCell v-for="cell in row.getVisibleCells()" :key="cell.id">
                <FlexRender :render="cell.column.columnDef.cell" :props="cell.getContext()" @athlete-deleted="emit('athleteDeleted')"/>
              </TableCell>
            </TableRow>
          </template>

          <TableRow v-else>
            <TableCell
              col-span="{columns.length}"
              class="h-24 text-center"
            >
              No results.
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>

    <DataTablePagination :table="table" />
  </div>
</template>
