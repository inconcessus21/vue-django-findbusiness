<template>
<div>
    <nav class="navbar navbar-dark navbar-expand-lg fixed-top bg-white portfolio-navbar gradient" style="background: linear-gradient(90deg, black, #a80000);">
        <div class="container"><router-link class="navbar-brand logo" to="/"><strong>PASS</strong><fa icon="handshake" /><strong>JON</strong></router-link><button data-bs-toggle="collapse" class="navbar-toggler" data-bs-target="#navbarNav"><span class="visually-hidden">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <template v-if="!$store.state.isAuthenticated">
                       
                    <li class="nav-item"><router-link class="nav-link d-lg-flex" to="/signup">Utwórz Konto</router-link></li>
                    <li class="nav-item"><router-link class="nav-link d-lg-flex" to="/login">Zaloguj</router-link></li>
                    
                    </template>
                    <template v-else>
                      
                        <li class="nav-item dropdown">
                        <a class="dropdown-toggle nav-link" aria-expanded="false" data-bs-toggle="dropdown" href="#">
                        <img  v-for="item in avatar" v-bind:key="item.id" :src="item.avatar" style="width: 32px;height: 32px; border-radius: 20px;">
                         </a>
                         
                        <div class="dropdown-menu">
                         <router-link class="dropdown-item" to='/mojekonto' >Moje Konto</router-link>



                            <router-link class="dropdown-item" to='/dash' >Bracia i Siostry</router-link>
                            <router-link class="dropdown-item" to='/grupymodlitewne' >Grupy Modlitewne</router-link>
                            <a class="dropdown-item" @click="logout()">Wyloguj</a>
                        </div>
                    </li>
                    </template>
                </ul>
            </div>
        </div>
    </nav>
    <div style="height:100px;"></div>
</div>
  

</template>

<script>
import store from '@/store/index.js';
import axios from 'axios'
import { useToast } from "vue-toastification";


export default {
    name: 'Navbar',
    
    

    setup() {
      // Get toast interface
      const toast = useToast();
      return { toast }
    },

  props:{
    name:Boolean,
  },

    data() {
        return {
            avatar: [],
            errors: [],
            
        }
    },

watch: {
  '$store.state.isAuthenticated': {
    deep: true,
    handler(newVal) {
        console.log(store.state.isAuthenticated)
        if (store.state.isAuthenticated){
            this.getAvatar()
        }
    }
  }
},

mounted() {
        if (store.state.isAuthenticated){
            this.getAvatar()
        }
    
},


    methods: {
        async logout() {

            await axios
                .post('/api/v1/token/logout/')
                .then(response => {
                    console.log('Logged out')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            this.$store.commit('removeToken')

            this.$router.push('/')

            this.toast.success("Successfully logged out", {
            position: "bottom-right",
            timeout: 4000,
            });

        },
        async getAvatar() {

            this.$store.commit('setIsLoading', true)

            axios
                .get('/api/v1/navbar/')
                .then(response => {
                     this.avatar = response.data
                     console.log(this.avatar)

                })

                
                .catch(error => {
                    console.log(error)
                    console.log(this.avatar)
                })

                this.$store.commit('setIsLoading', false)

        }
            
        }
    
}
</script>

