<template>
  <div class="flex justify-center">
    <div class="w-1/2 flex justify-center flex-col">
      <h1 class="font-bold text-4xl text-left">{{ recipe.title }}</h1>
      <div class="w-full flex justify-center mt-8">
        <img v-if="generatedImage" :src="'data:image/jpeg;base64,' + generatedImage" :alt="recipe.description"
             class="object-cover aspect-ratio-16/9 w-512 h-512 rounded-2xl">
        <!--        <img v-if="generatedImage" :src="generatedImage" :alt="recipe.Description" class="object-cover w-full h-96 rounded-2xl">-->
        <skeleton-loader v-else class="w-full h-96 rounded-2xl"></skeleton-loader>
      </div>
      <div class="mt-8 grid grid-cols-3">
        <div class="flex flex-col items-center justify-center text-center">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="#10b981"
               class="w-12 h-12">
            <path stroke-linecap="round" stroke-linejoin="round"
                  d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"/>
          </svg>

          <p class="text-sm text-gray-500 mt-2">{{ servings }}</p>
        </div>

        <div class="flex flex-col items-center justify-center text-center">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="#10b981"
               class="w-12 h-12">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <p class="text-sm text-gray-500 mt-2">{{ recipe.time_min }}</p>
        </div>

        <div class="flex flex-col items-center justify-center text-center">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
               stroke="#10b981" class="w-12 h-12" v-if="!recipe.bookmarked" @click="bookmarkRecipe">
            <path stroke-linecap="round" stroke-linejoin="round"
                  d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z"/>
          </svg>
          <svg xmlns="http://www.w3.org/2000/svg" fill="#10b981" viewBox="0 0 24 24" stroke-width="1.5"
               stroke="#10b981" class="w-12 h-12" v-else @click="bookmarkRecipe">
            <path stroke-linecap="round" stroke-linejoin="round"
                  d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z"/>
          </svg>


          <p class="text-sm text-gray-500 mt-2" v-if="!recipe.bookmarked">Add to bookmarks</p>
          <p class="text-sm text-gray-500 mt-2" v-else>Bookmarked!</p>
        </div>


      </div>
      <div class="mt-8">
        <h3 class="font-bold text-lg text-emerald-500 text-left">Ingredients:</h3>
        <ul class="grid grid-cols-2 gap-4 mt-4">
          <ingredient-item v-for="(quantity, ingredient) in recipe.ingredients"
                           :key="ingredient"
                           :ingredient="generateIngredientQuantities(ingredient, quantity)"
                           :removable="false"
          ></ingredient-item>
        </ul>
      </div>
      <div class="mt-8">
        <h3 class="font-bold text-lg text-emerald-500 text-left">Instructions:</h3>
        <!--        <vue-markdown :source="recipe.Instructions" class="text-left leading-8"/>-->
        <ol>
          <li v-for="(step, index) in steps" :key="index" class="text-left leading-8">{{ step }}</li>
        </ol>
      </div>
      <!--      <div class="flex justify-center mt-8 rounded-2xl border-2 border-emerald-500 py-1 px-2 align-middle cursor-pointer">-->
      <!--        <span><img src="../assets/bookmark-emerald.svg" class="h-8"></span>-->
      <!--        <span class="align-middle">Bookmark</span>-->
      <!--      </div>-->
    </div>
  </div>

</template>

<script>
import axios from "axios";
import SkeletonLoader from "@/components/SkeletonLoader.vue";
import IngredientItem from "@/components/IngredientItem.vue";
// import VueMarkdown from 'vue-markdown-render';

export default {
  name: 'ReciepeView',
  components: {IngredientItem, SkeletonLoader},
  mounted() {
    axios.post('http://127.0.0.1:8000/recipes/recipe/', {id: this.$route.params.id})
        .then(response => {
          console.log(response.data.recipe)
          this.recipe = response.data.recipe;
          if (response.data.image != "") {
            this.generatedImage = response.data.image;
          } else {
            const request = {
              id: this.$route.params.id,
            }
            axios.post('http://127.0.0.1:8000/recipes/image/', request)
                .then(response => {
                  console.log(response)
                  this.generatedImage = response.data.Image;
                })
                .catch(error => {
                  console.log(error)
                })
          }
        })
  },
  data() {
    return {
      // generatedImage: "https://i2.wp.com/www.downshiftology.com/wp-content/uploads/2018/12/Shakshuka-19.jpg",
      generatedImage: null,
      recipe: {
        title: '',
        description: '',
        ingredients: {},
        instructions: '',
      },
      bookmark: false,
    }
  },
  methods: {
    generateIngredientQuantities(ingredient, quantity) {
      return `${ingredient}: ${quantity}`;
    },
    bookmarkRecipe() {
      this.bookmark = !this.bookmark;
      axios.post('http://127.0.0.1:8000/recipes/bookmark/', {id: this.$route.params.id})
          .then(response => {
            this.recipe = response.data.recipe;
          })
          .catch(error => {
            console.log(error)
          })
    }
  },
  computed: {
    steps() {
      if (this.recipe.instructions) {
        return this.recipe.instructions.split('\n').filter(step => step.trim() !== '');
      }
      return [];
    },
    servings() {
      let people = this.recipe.servings
      if (people == 1) {
        return "1 serving"
      } else {
        return people + " servings"
      }
    },
  },
}
</script>

<style lang="scss" scoped>

</style>