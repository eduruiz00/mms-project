<template>
  <div>
    <h1 class="text-2xl font-bold text-left mb-8">Recipe Creation</h1>
    <div>
      <stepper-creation @set-tab="setTab" :active-tab="currentTab"></stepper-creation>
      <upload-image-tab v-if="currentTab === 1" @advance-tab="currentTab += 1" @detected-ingredients="changeIngredients"></upload-image-tab>
      <ingredients-tab v-if="currentTab === 2"
                       :ingredients="ingredients"
                        @remove-ingredient="removeIngredient"
                        @add-ingredient="addIngredient"
      ></ingredients-tab>
      <personalize-tab v-if="currentTab === 3" :ingredients="ingredients"></personalize-tab>
      <div class="flex justify-center mt-8" v-if="currentTab === 2">
        <div class="w-2/3 flex justify-end">
          <button class="bg-emerald-500 rounded-xl px-4 py-2 text-white font-bold" @click="currentTab += 1">{{ buttonName}}</button>
        </div>
      </div>

    </div>

  </div>
</template>

<script>
import StepperCreation from "@/assets/StepperCreation.vue";
import UploadImageTab from "@/components/UploadImageTab.vue";
import IngredientsTab from "@/components/IngredientsTab.vue";
import PersonalizeTab from "@/components/PersonalizeTab.vue";

export default {
  name: 'RecipeCreationView',
  components: {PersonalizeTab, IngredientsTab, UploadImageTab, StepperCreation},
  data() {
    return {
      currentTab: 1,
    }
  },
  methods: {
    setTab(tab) {
      if (tab <= this.currentTab) {
        this.currentTab = tab;
      }
    },
    removeIngredient(ingredient) {
      this.ingredients = this.ingredients.filter(item => item !== ingredient);
    },
    addIngredient(ingredient) {
      this.ingredients.push(ingredient);
    },
    changeIngredients(ingredients) {
      this.ingredients = ingredients;
    }
  },
  computed: {
    buttonName() {
      return this.currentTab === 3 ? 'Generate' : 'Continue';
    },
    ingredients() {
      return this.$store.getters.ingredients;
    }
  }
}
</script>

<style lang="scss" scoped>

</style>