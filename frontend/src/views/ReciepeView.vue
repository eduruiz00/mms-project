<template>
  <div>
    <h1>Generated recipe</h1>
    <h1>Title</h1>
    <p>Content</p>
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