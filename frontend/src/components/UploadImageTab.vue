<template>
  <div class="flex justify-center my-8">
    <div class="flex items-center justify-center w-2/3">
      <label
          for="dropzone-file"
          class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100"
      >
        <div class="flex flex-col items-center justify-center pt-5 pb-6">
          <svg
              class="w-8 h-8 mb-4 text-gray-500"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 16"
          >
            <!-- Your SVG content here -->
          </svg>
          <p class="mb-2 text-sm text-gray-500">
            <span class="font-semibold">Click to upload</span> or drag and drop
          </p>
          <p class="text-xs text-gray-500">SVG, PNG, JPG or GIF</p>
        </div>
        <input id="dropzone-file" type="file" class="hidden" accept="image/*" @change="onFilesSelected" multiple/>
      </label>
    </div>
  </div>

  <div class="flex justify-center" v-if="selectedImages.length > 0">
    <div v-if="selectedImages.length > 0" class="flex w-2/3 justify-center gap-6">
      <div v-for="(file, index) in selectedImages" :key="index" class="justify-center relative">
        <img :src="file.imageData" :alt="file.name" class="w-16 h-16 flex border border-emerald-900">
        <button class="absolute -top-2 -right-2 p-0.5 bg-red-500 rounded-full" @click="removeImage(index)">
        <span>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
               stroke="white" class="w-4 h-4">
            <path stroke-linecap="round" stroke-linejoin="round"
                  d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </span>
        </button>
      </div>
    </div>
  </div>

  <div class="flex justify-center mt-8">
    <div class="w-2/3 flex justify-end">
      <button class="bg-emerald-500 rounded-xl px-4 py-2 text-white font-bold" @click="onUpload">
        Continue
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "UploadImageTab",
  data() {
    return {
      selectedFiles: [], // Store selected files
      selectedImages: [], // Store selected files and their data
    };
  },
  methods: {
    removeImage(index) {
      this.selectedFiles.splice(index, 1);
      this.selectedImages.splice(index, 1);
    },
    onFilesSelected(event) {
      const files = event.target.files;

      if (files && files.length > 0) {
        // Process each selected file
        for (let i = 0; i < files.length; i++) {
          const file = files[i];
          this.selectedFiles.push(file);
          const reader = new FileReader();

          reader.onload = (event) => {
            this.selectedImages.push({
              name: file.name,
              imageData: event.target.result,
            });
          };

          reader.readAsDataURL(file);
        }
      }
    },
    onUpload() {
      // You can now access this.selectedFiles to get the selected files and their data
      // Loop through this.selectedFiles and upload each file individually
      const fd = new FormData();

      this.selectedFiles.forEach((file) => {
        fd.append("images[]", file, file.name);
      });

      axios
          .post("http://127.0.0.1:8000/recipes/upload/", fd, {
            onUploadProgress: (uploadEvent) => {
              console.log(
                  "Upload Progress: " +
                  Math.round((uploadEvent.loaded / uploadEvent.total) * 100) +
                  "%"
              );
            },
          })
          .then((res) => {
            this.$store.commit("setIngredients", res.data.ingredients);
            this.$emit("advance-tab");
          });
    },
  },
};
</script>
