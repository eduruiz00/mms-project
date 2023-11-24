<template>
  <div class="flex flex-col">
    <div class="flex justify-center mt-8">
      <div
          class="relative w-2/3 border px-4 py-8 sm:px-6 lg:px-8"
          aria-modal="true"
          role="dialog"
          tabindex="-1"
      >
        <h3 class="font-bold text-xl text-left mb-4">Ingredients</h3>
        <div class="mt-4 space-y-6">
          <ul class="grid grid-cols-2 gap-4">
            <ingredient-item v-for="ingredient in ingredients"
                             :key="ingredient"
                             :ingredient="ingredient"
                             :removable="false"
            ></ingredient-item>
          </ul>
        </div>

      </div>
    </div>
    <div class="flex justify-center w-full">
      <div class="flex justify-around gap-4 w-2/3 mt-8">
        <base-select :options="optionsPeople" label="People" v-model="selectedPeople"></base-select>
        <base-select :options="optionsDuration" label="Duration" v-model="selectedDuration"></base-select>
        <base-select :options="optionsFood" label="Include" v-model="selectedFood"></base-select>
      </div>
    </div>
  </div>
  <div class="flex justify-center mt-8">
    <div class="w-2/3 flex justify-end">
      <button class="bg-emerald-500 rounded-xl px-4 py-2 text-white font-bold" @click="getRecipe">
        Generate
      </button>
    </div>
  </div>
</template>

<script>

import BaseSelect from "@/components/BaseSelect.vue";
import IngredientItem from "@/components/IngredientItem.vue";

import axios from "axios";

export default {
  name: 'PersonalizeTab',
  components: {IngredientItem, BaseSelect},
  props: {
    ingredients: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      selectedPeople: '',
      selectedDuration: '',
      selectedFood: '',
      optionsPeople: ['1', '2', '3', '4+'],
      optionsDuration: ['< 15 min', '15 - 30 min', '30 - 45 min', '45 - 60 min', '> 60 min'],
      optionsFood: ['Include all', 'Include some'],
    }
  },
  methods: {
    getRecipe() {
      console.log("Hola, get recipe")
      const request = {
        ingredients: this.ingredients,
        people: this.selectedPeople,
        duration: this.selectedDuration,
        food: this.selectedFood,
      }
      axios.post('http://127.0.0.1:8000/recipes/write/', request)
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>

<style lang="scss" scoped>

</style>