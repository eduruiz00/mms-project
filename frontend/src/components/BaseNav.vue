<template>
  <div>
    <nav>
      <div class="bg-emerald-500 p-4">
        <div class="container mx-auto flex items-center justify-between">
          <router-link class="flex items-center" :to="{name: 'home'}">
            <img src="../assets/chef.svg" class="h-10 fill-white mr-4">
            <h1 class="text-3xl font-extrabold text-white">Recipe Generator</h1>
          </router-link>

          <div class="flex items-center space-x-4">
            <router-link :to="{name: 'bookmarks'}">
              <img src="../assets/bookmark.svg" class="h-8 fill-white">
            </router-link>
            <button>
              <img src="../assets/user.svg" class="h-8 fill-white">
            </button>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'BaseNav',
  props: {
    currentUser: {
      type: Object,
      default: null,
    },
  },
}
</script>

<style lang="scss" scoped>

</style>