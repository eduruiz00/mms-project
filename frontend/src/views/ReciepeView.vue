<template>
  <div>
    <h1>Generated recipe</h1>
    <h1>{{ generatedRecipe.recipe.Title }}</h1>
    <img :src="'data:image/jpeg;base64,' + generatedRecipe.Image" alt="Image">
    <p>{{ generatedRecipe.recipe.QuantitiesRequired }}</p>
    <p>{{ generatedRecipe.recipe.Instructions }}</p>
  </div>
</template>

<script>
export default {
  name: 'ReciepeView',
  components: {},
  data() {
    return {

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