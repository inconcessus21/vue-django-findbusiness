<template>
  <div class="hello">
       <nav class="navbar navbar-dark navbar-expand-lg fixed-top bg-white portfolio-navbar gradient">
        <div class="container"><router-link  class="navbar-brand logo" to="/"><i class="fas fa-search-location"></i>&nbsp;Znajdź Firmę&nbsp;</router-link><button data-bs-toggle="collapse" class="navbar-toggler" data-bs-target="#navbarNav"><span class="visually-hidden">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"> <router-link class="nav-link active" to="/">Strona Główna</router-link></li>
                    <li class="nav-item"> <router-link class="nav-link" to="/kategorie">Lista Firm</router-link></li>
                    <li class="nav-item"> <router-link class="nav-link" to="/lokalizacje">Lokalizacje</router-link></li>
                    


                    <template v-if="!$store.state.isAuthenticated">
                      <li class="nav-item"> <router-link class="nav-link" to="/login">Zaloguj</router-link></li>
                      <li class="nav-item"> <router-link class="nav-link" to="/rejestracja">Utwórz Konto</router-link></li>                    
                    </template>
                    <template v-else>                    
                      <li class="nav-item"> <router-link class="nav-link" style="background: var(--bs-indigo);border-radius: 12px;" to="/dodaj">DODAJ FIRMĘ</router-link></li>
                      <li class="nav-item"> <a class="nav-link" @click="logout()">Wyloguj</a></li>
                    </template>
                </ul>
            </div>
        </div>
    </nav>
    <div style="height: 100px;"></div>
  </div>
</template>

<script>

import axios from 'axios'
import { useToast } from "vue-toastification";

export default {
  name: 'NavBar',
      setup() {
      // Get toast interface
      const toast = useToast();
      return { toast }
    },
  methods: {

    async logout() {

            await axios
                .post('/api/v1/token/logout/')

                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            this.$store.commit('removeToken')

            this.$router.push('/')

            this.toast.success("Poprawnie wylogowano", {
            position: "bottom-right",
            timeout: 4000,
            });

        },
  }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
