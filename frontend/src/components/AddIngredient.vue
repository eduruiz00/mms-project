<template>
  <div class="relative">
    <label for="Search" class="sr-only"> Search </label>

    <input
        type="text"
        id="Search"
        placeholder="Add ingredient..."
        class="w-full rounded-2xl border-2 border-emerald-500 py-2.5 px-4 pe-10 shadow-sm focus:outline-none"
        v-model="ingredient"
        @keyup.enter="addIngredient"
    />

    <span class="absolute inset-y-0 end-0 grid w-10 place-content-center">
      <button type="button" class="text-gray-600 hover:text-gray-700" @click="addIngredient">
        <span class="sr-only">Search</span>

        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="#10b981"
             class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
      </button>
    </span>

  </div>
</template>

<script>
export default {
  name: 'AddIngredient',
  data() {
    return {
      ingredient: ''
    }
  },
  methods: {
    addIngredient() {
      this.$emit('add-ingredient', this.ingredient)
      this.ingredient = ''
    }
  }
}
</script>

<style lang="scss" scoped>

</style>