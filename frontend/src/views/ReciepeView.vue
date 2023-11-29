<template>
  <div class="flex justify-center">
    <div class="w-1/2 flex justify-center flex-col">
      <h1 class="font-bold text-4xl text-left">{{ recipe.title }}</h1>
      <div class="w-full flex justify-center mt-8">
        <img v-if="generatedImage" :src="'data:image/jpeg;base64,' + generatedImage" :alt="recipe.description"
             class="object-cover w-full h-96 rounded-2xl">
        <!--        <img v-if="generatedImage" :src="generatedImage" :alt="recipe.Description" class="object-cover w-full h-96 rounded-2xl">-->
        <skeleton-loader v-else class="w-full h-96 rounded-2xl"></skeleton-loader>
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
    }
  },
  methods: {
    generateIngredientQuantities(ingredient, quantity) {
      return `${ingredient}: ${quantity}`;
    }
  },
  computed: {
    steps() {
      if (this.recipe.instructions) {
        return this.recipe.instructions.split('\n').filter(step => step.trim() !== '');
      }
      return [];
    }
  },
}
</script>

<style lang="scss" scoped>

</style>