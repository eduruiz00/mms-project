<template>
  <div class="flex flex-col items-center justify-center my-8">
    <bookmark-card class="w-1/2 my-4"></bookmark-card>
    <bookmark-card class="w-1/2 my-4"></bookmark-card>
    <bookmark-card class="w-1/2 my-4"></bookmark-card>
  </div>
</template>

<script>
import BookmarkCard from "@/components/BookmarkCard.vue";

export default {
  name: 'BookmarkView',
  components: {BookmarkCard},
  data() {
    return {

    }
  },
  methods: {

  }
}
</script>

<style lang="scss" scoped>

</style>