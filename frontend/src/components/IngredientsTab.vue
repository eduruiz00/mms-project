<template>
  <div class="flex-col justify-center">
    <div class="mt-8 text-end underline text-emerald-500 text-sm font-bold w-5/6">
      <button @click="viewDetected = true">View detected ingredients</button>
    </div>
    <div
        class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white p-8 shadow-lg z-50 w-3/4"
        v-if="viewDetected">
      <div class="flex justify-between text-end mb-4">
        <div class="font-bold text-xl">Detected images:</div>
        <div class="text-s">Image {{ currentImage+1 }} of {{ imagesDetected.length }}</div>
        <div class="flex">
          <button @click="goLeft">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
</svg>
          </button>
          <button @click="goRight">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
</svg>
          </button>

          <button @click="viewDetected = false">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
               stroke="currentColor" class="w-8 h-8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
        </div>

      </div>
      <!-- Your content goes here -->
      <img :src="'data:image/jpeg;base64,' + selectedImage" class="w-full">
    </div>
    <div class="flex justify-center mt-4">
      <div
          class="relative w-2/3 border px-4 py-8 sm:px-6 lg:px-8"
          aria-modal="true"
          role="dialog"
          tabindex="-1"
      >
        <div class="mt-4 space-y-6">
          <ul class="grid grid-cols-2 gap-4">
            <ingredient-item v-for="ingredient in ingredients"
                             :key="ingredient"
                             :ingredient="ingredient"
                             @remove-ingredient="removeIngredient"
                             :removable="true"
            ></ingredient-item>
          </ul>
        </div>
        <div class="flex justify-end mt-6">
          <add-ingredient class="w-1/3" @add-ingredient="addIngredient"></add-ingredient>
        </div>

      </div>
    </div>
  </div>

</template>

<script>
import IngredientItem from "@/components/IngredientItem.vue";
import AddIngredient from "@/components/AddIngredient.vue";

export default {
  name: 'IngredientsTab',
  components: {AddIngredient, IngredientItem},
  props: {
    ingredients: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      viewDetected: false,
      currentImage: 0,
    }
  },
  methods: {
    removeIngredient(ingredient) {
      this.$store.commit('removeIngredient', ingredient);
    },
    addIngredient(ingredient) {
      this.$emit('add-ingredient', ingredient);
    },
    goLeft() {
      if (this.currentImage > 0) {
        this.currentImage -= 1;
      }
    },
    goRight() {
      if (this.currentImage < this.imagesDetected.length - 1) {
        this.currentImage += 1;
      }
    }
  },
  computed: {
    imagesDetected() {
      return this.$store.getters.imagesDetected;
    },
    selectedImage(){
      return this.imagesDetected[this.currentImage];
    }
  }
}
</script>

<style lang="scss" scoped>

</style>