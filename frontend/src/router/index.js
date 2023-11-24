import {createRouter, createWebHistory} from 'vue-router'
import RecipeCreationView from "@/views/RecipeCreationView.vue";
import store from '../store/index.js';

const routes = [
    {
        path: '/',
        name: 'home',
        component: RecipeCreationView,
        beforeEnter: checkAuth,
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: function () {
            return import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
        }
    },
    {
        path: '/bookmarks',
        name: 'bookmarks',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: function () {
            return import(/* webpackChunkName: "about" */ '../views/BookmarkView.vue')
        }
    },
    {
        path: '/recipe',
        name: 'recipe',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: function () {
            return import(/* webpackChunkName: "about" */ '../views/ReciepeView.vue')
        }
    },
    {
        path: '/login',
        name: 'login',
        component: function () {
            return import(/* webpackChunkName: "about" */ '../views/LoginView.vue')
        },
        beforeEnter: (to, from, next) => {
            if (store.getters.isAuthenticated) {
                return next({
                    name: 'home'
                });
            }
            return next();
        }
    },
    {
        path: '/signup',
        name: 'signup',
        component: function () {
            return import(/* webpackChunkName: "about" */ '../views/SignupView.vue')
        },
    },
    {
        path: '/logout',
        name: 'logout',
        component: RecipeCreationView,
        // User MUST BE authenticated
        beforeEnter: (to, from, next) => {
            store.dispatch('logout');
            return next({
                name: 'login'
            });
        }
    },

]

function checkAuth(to, from, next) {
    const isAuthenticated = store.getters.isAuthenticated;
    if (isAuthenticated) {
        return next();
    } else {
        //Cleans all the vuex stored variables
        store.dispatch('logout');
    }
}

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
