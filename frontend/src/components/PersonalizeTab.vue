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
        <div>
          <label for="Select" class="block text-sm font-medium text-gray-900">
            People
          </label>

          <div class="mt-1.5 w-full rounded-xl text-gray-700 p-2 border-gray-200 border shadow-md outline-0 pr-2">
            <select
                name="Select"
                id="Select"
                class="outline-0"
                v-model="selectedPeople"
            >
              <option value="" disabled>Please select</option>
              <option v-for="option in optionsPeople" :value="option" :key="option">{{ option }}</option>
            </select>
          </div>

        </div>
        <div>
          <label for="Select" class="block text-sm font-medium text-gray-900">
            Duration
          </label>

          <div class="mt-1.5 w-full rounded-xl text-gray-700 p-2 border-gray-200 border shadow-md outline-0 pr-2">
            <select
                name="Select"
                id="Select"
                class="outline-0"
                v-model="selectedDuration"
            >
              <option value="" disabled>Please select</option>
              <option v-for="option in optionsDuration" :value="option" :key="option">{{ option }}</option>
            </select>
          </div>

        </div>
        <div>
          <label for="Select" class="block text-sm font-medium text-gray-900">
            Food
          </label>

          <div class="mt-1.5 w-full rounded-xl text-gray-700 p-2 border-gray-200 border shadow-md outline-0 pr-2">
            <select
                name="Select"
                id="Select"
                class="outline-0"
                v-model="selectedFood"
            >
              <option value="" disabled>Please select</option>
              <option v-for="option in optionsFood" :value="option" :key="option">{{ option }}</option>
            </select>
          </div>

        </div>
      </div>
    </div>
  </div>
  <div class="flex justify-center mt-8">
    <div class="w-2/3 flex justify-end">
      <button class="bg-emerald-500 rounded-xl px-4 py-2 text-white font-bold" @click="getRecipe"
              :disabled="disabledButton" :class="buttonFormat">
        Generate
      </button>
    </div>
  </div>
  <div class="flex justify-center flex-col mt-16" v-if="loading">
    <radar-spinner
        :animation-duration="2000"
        :size="60"
        color="#10b981"
        class="mx-auto"
    />
    <p>Generating your recipe...</p>
  </div>
</template>

<script>
import IngredientItem from "@/components/IngredientItem.vue";
import {RadarSpinner} from 'epic-spinners';

import axios from "axios";

export default {
  name: 'PersonalizeTab',
  components: {IngredientItem, RadarSpinner},
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
      loading: false,
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
      axios.post('http://127.0.0.1:8000/recipes/write/', request, {
        onUploadProgress: () => {
          this.loading = true;
        }
      }).then(response => {
        console.log(response)
        this.loading = false;
        this.$store.commit('setGeneratedRecipe', response.data);
        this.$router.push({name: 'recipe'})
      })
          .catch(error => {
            console.log(error)
          })
    }
  },
  computed: {
    disabledButton() {
      return this.selectedPeople == "" || this.selectedDuration == "" || this.selectedFood == ""
    },
    buttonFormat() {
      if (this.disabledButton) {
        return "bg-gray-400 cursor-not-allowed"
      } else {
        return "bg-emerald-500"
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>