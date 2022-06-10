import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CategoriesList from '../views/CategoriesList.vue'
import BusinessInCategory from '../views/BusinessInCategory.vue'
import BusinessDetails from '../views/BusinessDetails.vue'
import LocalizationView from '../views/LocalizationView.vue'
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
    name: 'BusinessInCategory',
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
    name: 'LocalizationView',
    component: LocalizationView,
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
