<template>
  <div>
    <label for="Select" class="block text-sm font-medium text-gray-900">
      {{ label }}
    </label>

    <div class="mt-1.5 w-full rounded-xl text-gray-700 p-2 border-gray-200 border shadow-md outline-0 pr-2">
      <select
      name="Select"
      id="Select"
      class="outline-0"
    >
      <option value="" disabled>Please select</option>
      <option v-for="option in options" :value="option" :key="option">{{ option }}</option>
    </select>
    </div>

  </div>
</template>

<script>
export default {
  name: 'BaseSelect',
  props: {
    label: {
      type: String,
      required: true
    },
    options: {
      type: Array,
      required: true
    }
  },
  data() {
    return {}
  },
  methods: {}

}
</script>

<style lang="scss" scoped>

</style>