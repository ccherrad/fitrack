
<template>
  <div class="bg-white bg-light-pattern h-full grid grid grid-cols-12 grid-rows-12 m-4">
    <div class="col-span-12 h-16 flex">
      <MainLogo class="items-center"/>
      <div class="ml-auto flex items-center space-x-2 justify-end">
        <MainMenu />
        <MainMenu />
      </div>
    </div>
    <div class="col-start-1 row-start-2 col-span-2 row-span-9">
      <MainSidebar />
    </div>
    <div class="col-start-1 row-start-12 col-span-12"/>
    <div class="col-start-3 row-start-2 col-span-10 row-span-10">
      <NuxtPage />
    </div>
  </div>
</template>

