<template>
  <div class="flex justify-center">
    <div class="w-1/2 flex justify-center flex-col">
      <h1 class="font-bold text-4xl text-left">{{ generatedRecipe.recipe.Title }}</h1>
      <div class="w-full flex justify-center mt-8">
        <img v-if="generatedImage" :src="'data:image/jpeg;base64,' + generatedImage" :alt="generatedRecipe.recipe.Description" class="object-cover w-full h-96 rounded-2xl">
<!--        <img v-if="generatedImage" :src="generatedImage" :alt="generatedRecipe.recipe.Description" class="object-cover w-full h-96 rounded-2xl">-->
        <skeleton-loader v-else class="w-full h-96 rounded-2xl"></skeleton-loader>
      </div>
      <div class="mt-8">
        <h3 class="font-bold text-lg text-emerald-500 text-left">Ingredients:</h3>
        <ul class="grid grid-cols-2 gap-4 mt-4">
          <ingredient-item v-for="(quantity, ingredient) in generatedRecipe.recipe.QuantitiesRequired"
                           :key="ingredient"
                           :ingredient="generateIngredientQuantities(ingredient, quantity)"
                           :removable="false"
          ></ingredient-item>
        </ul>
      </div>
      <div class="mt-8">
        <h3 class="font-bold text-lg text-emerald-500 text-left">Instructions:</h3>
<!--        <vue-markdown :source="generatedRecipe.recipe.Instructions" class="text-left leading-8"/>-->
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
  created() {
    if (this.generatedRecipe) {
      const request = {
        Title: this.generatedRecipe.recipe.Title,
        Description: this.generatedRecipe.recipe.Description,
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
  },
  data() {
    return {
      // generatedImage: "https://i2.wp.com/www.downshiftology.com/wp-content/uploads/2018/12/Shakshuka-19.jpg",
      generatedImage: null,
    }
  },
  methods: {
    generateIngredientQuantities(ingredient, quantity) {
      return `${ingredient}: ${quantity}`;
    }
  },
  computed: {
    generatedRecipe() {
      return this.$store.getters.generatedRecipe;
      // return {"recipe": {'Title': 'Quick and Healthy Quiche with a Fruit Twist', 'QuantitiesRequired': {'olive oil': ' 2 tablespoons', 'tomatoes': ' 1 small (diced)', 'eggs': ' 4 large', 'apples': ' 1 small (sliced)', 'broccoli': ' 1/2 cup (chopped)'}, 'Description': 'A colorful and nutritious quiche, filled with a blend of vegetables, fruits, and eggs, creating a delicious meal for one.', 'Instructions': '\n\n        1. Preheat your oven to 375°F (190°C).\n        2. In a large mixing bowl, whisk together the eggs, olive oil, diced tomatoes, and chopped broccoli. Season with salt and pepper.\n        3. Roll out your pie crust and place it into a 9-inch pie dish. Pour the egg mixture into the crust.\n        4. Arrange the sliced apples on top of the egg mixture.\n        5. Bake the quiche in the preheated oven for about 30-40 minutes or until the crust is golden brown and the eggs are set.\n        6. Remove from the oven and let cool for a few minutes before serving.\n\n        Enjoy your delicious and healthy Quick and Healthy Quiche with a Fruit Twist!\n'}}
    },
    steps() {
      return this.generatedRecipe.recipe.Instructions.split('\n').filter((step) => step.trim() !== '');
    }
  },
}
</script>

<style lang="scss" scoped>

</style>