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
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-4 h-4">
  <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" />
</svg>


            <p class="text-xs">{{ this.recipe.time_min }}</p>
          </div>
        </div>
      </div>
    </div>

    <div class="flex justify-end">
      <strong
          class="-mb-[2px] -me-[2px] inline-flex items-center gap-1 rounded-ee-xl rounded-ss-xl bg-green-600 px-3 py-1.5 text-white"
      >
<!--        <svg-->
<!--            xmlns="http://www.w3.org/2000/svg"-->
<!--            class="h-4 w-4"-->
<!--            fill="none"-->
<!--            viewBox="0 0 24 24"-->
<!--            stroke="currentColor"-->
<!--            stroke-width="2"-->
<!--        >-->
<!--          <path-->
<!--              stroke-linecap="round"-->
<!--              stroke-linejoin="round"-->
<!--              d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"-->
<!--          />-->
<!--        </svg>-->
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-4 h-4">
  <path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z" />
</svg>


        <span class="text-[10px] font-medium sm:text-xs">Starred</span>
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