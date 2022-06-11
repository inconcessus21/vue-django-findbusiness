import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import 'bootstrap'; 
import 'bootstrap/dist/css/bootstrap.min.css';

import Toast from "vue-toastification";
// Import the CSS or use your own!
import "vue-toastification/dist/index.css";



import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';

library.add(fas);



axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).component('fa', FontAwesomeIcon).use(Toast).use(store).use(router, axios).mount('#app')
