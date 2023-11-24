import {createStore} from 'vuex'
import axios from 'axios';
import VueJwtDecode from 'vue-jwt-decode'
import router from "@/router";

export default createStore({
    state: {
        accessToken: null,
        user: null,
        ingredients: ['Tomatoes', 'Onions', 'Garlic', 'Bread', 'Pepper', 'Chicken'],
        generatedRecipe: null,
    },
    getters: {
        isAuthenticated: state => {
            return state.accessToken !== null;
        },
        accessToken: state => {
            return state.accessToken;
        },
        user: state => {
            return state.user;
        },
        ingredients: state => {
            return state.ingredients;
        },
        generatedRecipe: state => {
            return state.generatedRecipe;
        }
    },
    mutations: {
        setAccessToken: (state, value) => {
            state.accessToken = value;
        },
        logoutAuth: state => {
            state.accessToken = null;
        },
        setUser: (state, value) => {
            state.user = value;
            return value;
        },
        setIngredients: (state, value) => {
            state.ingredients = value;
        },
        removeIngredient: (state, ingredient) => {
            state.ingredients = state.ingredients.filter(item => item !== ingredient);
        },
        setGeneratedRecipe(state, value) {
            state.generatedRecipe = value;
        }
    },
    actions: {
        login({commit}, credentials) {
            return axios.post('token/', credentials)
                .then(response => {
                    // retrieve access token
                    const accessToken = response.data.access;
                    commit('setAccessToken', accessToken);
                    localStorage.setItem('accessToken', accessToken);

                    //Redirects to logged User homepage
                    const decodedJwt = VueJwtDecode.decode(accessToken);
                    commit('setUser', decodedJwt["username"]);
                    router.push({name: 'home'});
                })
        },
        setUser({commit}, user) {
            commit('setUser', user);
        },
        setAccessToken({commit}, token) {
            commit('setAccessToken', token);
        },
        logout({commit}) {
            commit('logoutAuth');
            localStorage.removeItem('accessToken');
            router.push({name: 'login'});
        },
    },
    modules: {}
})
