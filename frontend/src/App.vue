<template class="bg-gray-50 font-custom">
    <base-nav v-if="currentUser" :currentUser="currentUser" @logout="submitLogout" @update-form="updateFormToggle" />
    <div v-if="currentUser" class="center">
      <h2>You're logged in!</h2>
    </div>
    <div v-else class="center">
      <signup-view v-if="registrationToggle" @submit="submitRegistration" @to-login="registrationToggle = false"></signup-view>
      <login-tab v-else @submit="submitLogin" @to-signup="registrationToggle = true"></login-tab>
    </div>
  <router-view class="m-8" v-if="currentUser"/>
</template>

<script>
import BaseNav from "@/components/BaseNav.vue";
import axios from "axios";
import SignupView from "@/views/SignupView.vue";
import LoginTab from "@/components/LoginTab.vue";
export default {
  components: {LoginTab, SignupView, BaseNav},
  data() {
    return {
      currentUser: null,
      registrationToggle: false,
      email: '',
      username: '',
      password: '',
    };
  },
  methods: {
    updateFormToggle() {
      this.registrationToggle = !this.registrationToggle;
    },
    submitRegistration(data) {
      console.log('Registration data:', data);
      axios.post('register', {
        first_name: data.firstName,
        last_name: data.lastName,
        email: data.email,
        password: data.password,
      }).then(() => {
        axios.post('login', {
          email: data.email,
          password: data.password,
        }).then(() => {
          this.currentUser = true;
        });
      });
    },
    submitLogin(data) {
      axios.post('login', {
        email: data.email,
        password: data.password,
      }).then(() => {
        this.currentUser = true;
      });
    },
    submitLogout() {
      axios.post('logout', null, {withCredentials: true}).then(() => {
        this.currentUser = false;
      });
    },
  },
  created() {
    axios.get('user')
        .then(() => {
          this.currentUser = true;
        })
        .catch(() => {
          this.currentUser = false;
        });
  },
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
