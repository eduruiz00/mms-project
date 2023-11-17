<template class="bg-gray-50 font-custom">
  <base-nav v-if="isAuth"/>
  <router-view :class="classRouterView"/>
</template>

<script>
import BaseNav from "@/components/BaseNav.vue";
import VueJwtDecode from "vue-jwt-decode";

export default {
  components: {BaseNav},
  data() {
    return {};
  },
  methods: {},
  computed: {
    isAuth() {
      return this.$store.getters.isAuthenticated;
    },
    classRouterView() {
      return this.isAuth ? 'm-8' : '';
    }
  },
  created() {
    const storedAccessToken = localStorage.getItem('accessToken');
    if (storedAccessToken) {
      this.$store.commit('setAccessToken', storedAccessToken);
      const decodedJwt = VueJwtDecode.decode(storedAccessToken);
      this.$store.dispatch('setUser', decodedJwt["username"]);
    }
  }
};
</script>

<style lang="less">
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
