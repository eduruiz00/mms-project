<template class="bg-gray-50 font-custom">
  <nav>
    <div class="bg-emerald-500 p-4">
      <div class="container mx-auto flex items-center justify-between">
        <router-link class="flex items-center" :to="{name: 'home'}">
          <img src="./assets/chef.svg" class="h-10 fill-white mr-4">
          <h1 class="text-3xl font-extrabold text-white">Recipe Generator</h1>
        </router-link>

        <div class="flex items-center space-x-4">
          <router-link :to="{name: 'bookmarks'}">
            <img src="./assets/bookmark.svg" class="h-8 fill-white">
          </router-link>
          <button>
            <img src="./assets/user.svg" class="h-8 fill-white">
          </button>
        </div>
      </div>
    </div>
  </nav>
  <router-view class="m-8"/>
</template>

<style lang="less">
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
