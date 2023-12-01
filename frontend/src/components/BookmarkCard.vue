<template>
  <article class="rounded-xl border-2 border-gray-100 bg-white">
    <div class="flex items-start gap-4 p-4 sm:p-6 lg:p-8">
      <router-link :to="'/recipe/' + recipe.id" class="block shrink-0">

        <img
            v-if="recipe.image"
            :alt="recipe.description"
            :src="'data:image/jpeg;base64,' + recipe.image"
            class="h-14 w-14 rounded-lg object-cover"
        />
        <div
            v-else
            class="h-14 w-14 rounded-lg object-cover bg-gray-300"
        />

      </router-link>

      <div class="text-left">
        <h3 class="font-medium sm:text-lg">
          <router-link :to="'/recipe/' + recipe.id" class="hover:underline">
            {{ recipe.title }}
          </router-link>
        </h3>

        <p class="line-clamp-2 text-sm text-gray-700">
          {{ recipe.description }}
        </p>

        <div class="mt-2 sm:flex sm:items-center sm:gap-2">
          <div class="flex items-center gap-1 text-gray-500">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                 stroke="currentColor" class="w-4 h-4">
              <path stroke-linecap="round" stroke-linejoin="round"
                    d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"/>
            </svg>

            <p class="text-xs">{{ servings }}</p>
          </div>

          <span class="hidden sm:block" aria-hidden="true">&middot;</span>

          <div class="flex items-center gap-1 text-gray-500">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                 stroke="currentColor" class="w-4 h-4">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>


            <p class="text-xs">{{ this.recipe.time_min }}</p>
          </div>
        </div>
      </div>
    </div>

    <div class="flex justify-end" v-if="recipe.bookmarked">
      <strong
          class="-mb-[2px] -me-[2px] inline-flex items-center gap-1 rounded-ee-xl rounded-ss-xl bg-green-600 px-3 py-1.5 text-white"
      >
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
             class="w-4 h-4">
          <path stroke-linecap="round" stroke-linejoin="round"
                d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z"/>
        </svg>


        <span class="text-[10px] font-medium sm:text-xs">Bookmark</span>
      </strong>
    </div>
  </article>
</template>

<script>
export default {
  name: 'BookmarkCard',
  props: {
    recipe: {
      type: Object,
      required: true
    }
  },
  data() {
    return {}
  },
  methods: {},
  computed: {
    servings() {
      let people = this.recipe.servings
      if (people == 1) {
        return "1 serving"
      } else {
        return people + " servings"
      }
    }
  }

}
</script>

<style lang="scss" scoped>

</style>