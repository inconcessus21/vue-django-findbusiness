import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CategoriesList from '../views/CategoriesList.vue'
import BusinessInCategory from '../views/BusinessInCategory.vue'
import BusinessDetails from '../views/BusinessDetails.vue'
import LokalizacjeView from '../views/LokalizacjeView.vue'
import AddBusiness from '../views/AddBusiness.vue'
import LoginView from '../views/LoginView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/kategorie',
    name: 'kategorie',
    component: CategoriesList
  },
  {
    path: '/kategoria/:propCategory',
    name: 'kategoria',
    component: BusinessInCategory,
    props: true,
  },
  {
    path: '/firma/:uuid',
    name: 'BusinessDetails',
    component: BusinessDetails,
    props: true,
  },
  {
    path: '/lokalizacje',
    name: 'lokalizacjeview',
    component: LokalizacjeView,
  },
  {
    path: '/dodaj',
    name: 'AddBusiness',
    component: AddBusiness,
    meta: {
      requiredLogin: true
      
    }
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
