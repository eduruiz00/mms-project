<template>
  <div>
    <h1>Generated recipe</h1>
    <h1 v-if="generatedRecipe">{{ generatedRecipe.recipe.Title }}</h1>
    <div class="w-full flex justify-center">
      <img v-if="generatedImage" :src="'data:image/jpeg;base64,' + generatedImage" alt="Image">
      <div class="h-56 w-96 bg-gray-200" v-else></div>
    </div>
    <p v-if="generatedRecipe">{{ generatedRecipe.recipe.QuantitiesRequired }}</p>
    <p v-if="generatedRecipe">{{ generatedRecipe.recipe.Instructions }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'ReciepeView',
  components: {},
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
      generatedImage: null,
    }
  },
  methods: {

  },
  computed: {
    generatedRecipe() {
      return this.$store.getters.generatedRecipe;
    }
  }
}
</script>

<style lang="scss" scoped>

</style>