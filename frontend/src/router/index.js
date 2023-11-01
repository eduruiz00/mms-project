import { createRouter, createWebHistory } from 'vue-router'
import RecipeCreation from "@/views/RecipeCreation.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: RecipeCreation
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
    path: '/signup',
    name: 'signup',
    component: function () {
        return import(/* webpackChunkName: "about" */ '../views/SignupView.vue')
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
