import { createRouter, createWebHistory } from 'vue-router'
import DiaryView from '../views/DiaryView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'diary',
      component: DiaryView,
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue'),
    },
    {
      path: '/addMeal/:typeOfMeal/:imageUrl/:id',
      name: 'addMeal',
      component: () => import('../views/AddMealView.vue'),
      meta: { hideHeaderFooter: true }
    },
    {
      path: '/seeDetails/:typeOfMeal',
      name: 'seeDetails',
      component: () => import('../views/SeeDetailsView.vue'),
      meta: { hideHeaderFooter: true }
    }
  ],
})

export default router
