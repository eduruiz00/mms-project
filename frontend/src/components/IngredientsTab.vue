<template>
  <div class="flex justify-center mt-8">
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

    }
  },
  methods: {
    removeIngredient(ingredient) {
      this.$store.commit('removeIngredient', ingredient);
    },
    addIngredient(ingredient) {
      this.$emit('add-ingredient', ingredient);
    }
  }
}
</script>

<style lang="scss" scoped>

</style>