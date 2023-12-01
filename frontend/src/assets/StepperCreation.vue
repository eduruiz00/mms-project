<template>
  <div>
    <h2 class="sr-only">Steps</h2>

    <div>
      <ol
        class="grid grid-cols-1 divide-x divide-gray-100 overflow-hidden rounded-lg border border-gray-100 text-sm text-gray-500 sm:grid-cols-3"
      >
        <li class="flex items-center justify-center gap-2 p-4"
            :class="customClasses(1)"
            @click="$emit('set-tab', 1)">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-7 w-7 shrink-0">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
          </svg>

          <p class="leading-none">
            <strong class="block font-medium"> Picture </strong>
            <small class="mt-1"> Picture of the ingredients. </small>
          </p>
        </li>

        <li
          class="relative flex items-center justify-center gap-2 p-4"

          :class="customClassesBox(2)"
          @click="$emit('set-tab', 2)"

        >
          <span
            class="absolute -left-2 top-1/2 h-4 w-4 -translate-y-1/2 rotate-45 border border-gray-100 ltr:border-b-0 ltr:border-s-0 ltr:bg-white rtl:border-e-0 rtl:border-t-0 rtl:bg-gray-50 sm:block"
            :class="customClassesBox(1)"
          >
          </span>

          <span
            class="absolute -right-2 top-1/2 h-4 w-4 -translate-y-1/2 rotate-45 border border-gray-100 border-b-0 border-s-0"
            :class="customClasses(2)"
          >
          </span>

          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-7 w-7 shrink-0">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 00-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 00-16.536-1.84M7.5 14.25L5.106 5.272M6 20.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm12.75 0a.75.75 0 11-1.5 0 .75.75 0 011.5 0z" />
          </svg>

          <p class="leading-none">
            <strong class="block font-medium"> Ingredients </strong>
            <small class="mt-1"> Edit the recognized ingredients. </small>
          </p>
        </li>

        <li class="flex items-center justify-center gap-2 p-4"
            :class="customClasses(3)"
            @click="$emit('set-tab', 3)"
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-7 w-7 shrink-0">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9.53 16.122a3 3 0 00-5.78 1.128 2.25 2.25 0 01-2.4 2.245 4.5 4.5 0 008.4-2.245c0-.399-.078-.78-.22-1.128zm0 0a15.998 15.998 0 003.388-1.62m-5.043-.025a15.994 15.994 0 011.622-3.395m3.42 3.42a15.995 15.995 0 004.764-4.648l3.876-5.814a1.151 1.151 0 00-1.597-1.597L14.146 6.32a15.996 15.996 0 00-4.649 4.763m3.42 3.42a6.776 6.776 0 00-3.42-3.42" />
          </svg>


          <p class="leading-none">
            <strong class="block font-medium"> Personalize </strong>
            <small class="mt-1"> Personalize your recipe. </small>
          </p>
        </li>
      </ol>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StepperCreation',
  props: {
    activeTab: {
      type: Number,
      required: true
    }
  },
  data() {
    return {

    }
  },
  methods: {
    customClasses(tabNum) {
      return {
        'bg-emerald-400 text-white cursor-pointer': this.activeTab >= tabNum,
        'bg-white text-gray-500 cursor-not-allowed': this.activeTab < tabNum,
      };
    },
    customClassesBox(tabNum) {
      return {
        'bg-emerald-400 text-white border-white border-b-0 border-s-0': this.activeTab >= tabNum,
        'bg-white text-gray-500': this.activeTab < tabNum,
      };
    },
  },
}
</script>

<style lang="scss" scoped>

</style>