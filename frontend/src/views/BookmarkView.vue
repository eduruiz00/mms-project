<template>
  <div class="flex flex-col items-center justify-center my-8">
    <bookmark-card class="w-1/2 my-4" v-for="recipe in bookmarkedRecipes" :key="recipe.name" :recipe="recipe"></bookmark-card>
  </div>
</template>

<script>
import BookmarkCard from "@/components/BookmarkCard.vue";
import axios from "axios";

export default {
  name: 'BookmarkView',
  components: {BookmarkCard},
  created() {
    axios.get('http://127.0.0.1:8000/recipes/all/')
        .then(response => {
          console.log(response)
          this.recipes = response.data.recipes;
        })
  },
  data() {
    return {
      recipes: [],
    }
  },
  methods: {

  },
  computed: {
    bookmarkedRecipes() {
      return this.recipes.filter(recipe => recipe.bookmarked);
    }
  }
}
</script>

<style lang="scss" scoped>

</style>