import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import './assets/bootstrap/css/bootstrap.min.css'
import './assets/fonts/fontawesome-all.min.css'
import './assets/css/pikaday.min.css'
import './assets/fonts/ionicons.min.css'


import Toast from "vue-toastification";
// Import the CSS or use your own!
import "vue-toastification/dist/index.css";


axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).use(Toast).use(store).use(router, axios).mount('#app')
