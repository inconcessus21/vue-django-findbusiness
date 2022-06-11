import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import HomeView from '../views/HomeView.vue'
import Signup from '../views/SignupView.vue'
import Login from '../views/LoginView.vue'
import Dash from '../views/DashView.vue'
import Myacc from '../views/MyAccView.vue'
import Profile from '../views/ProfileView.vue'
import Projects from '../views/ProjectsView.vue'
import ProjectDetail from '../views/DetailProjectView.vue'
import AddProject from '../views/AddProject.vue'
import Tags from '../views/TagsView.vue'
import Tag from '../views/TagView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/dash',
    name: 'dash',
    component: Dash,
    meta: {
      requiredLogin: true
    }
  },
  {
    path: '/mojekonto',
    name: 'myacc',
    component: Myacc,
    meta: {
      requiredLogin: true
    }
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: Profile,
    props: true,
    meta: {
      requiredLogin: true
      
    }
  },

  {
    path: '/grupymodlitewne',
    name: 'projects',
    component: Projects,
    meta: {
      requiredLogin: true
    }
  },
  {
    path: '/grupa/:uuid',
    name: 'project',
    component: ProjectDetail,
    props: true,
    meta: {
      requiredLogin: true,
      
    }
  },
  {
    path: '/grupymodlitewne/dodajgrupe',
    name: 'dodajgrupe',
    component: AddProject,
    meta: {
      requiredLogin: true,
      
    }
  },
  {
    path: '/tags',
    name: 'tags',
    component: Tags,
    props: true,
    meta: {
      requiredLogin: true,
      
    }
  },
  {
    path: '/tag/:tag',
    name: 'tag',
    component: Tag,
    props: true,
    meta: {
      requiredLogin: true,
      
    }
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiredLogin) && !store.state.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
