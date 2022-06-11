<template>
<div class="container d-flex d-xl-flex justify-content-xl-center">
    <div class="d-flex d-sm-flex d-md-flex d-lg-flex d-xl-flex justify-content-center flex-wrap justify-content-sm-center justify-content-md-center justify-content-lg-center justify-content-xl-center">
        <p v-for="prof in profiles" v-bind:key="prof.id">
        <div class="card" style="width: 285px;height: 400px;margin: 5px;border-radius: 15px;">
              
                <div class="card-body text-center">
                    <img class="img-fluid" :src="prof.avatar" style="width: 150px;border-width: 1px;border-radius: 100px;" />
                    
                    <h4 class="card-title"><router-link :to="{ name: 'profile', params: { username: prof.username } }" >
                    {{ prof.username }}
                    </router-link>
                    <fa v-if="prof.is_online" icon="circle" data-bs-toggle="tooltip" title="Online" style="color: rgb(0,197,67);font-size: 12px;padding: 0px;margin-top: 0px;" /></h4>
                    <h6 class="text-muted card-subtitle mb-2">{{ prof.about }}</h6>
                    <h6 class="text-muted card-subtitle mb-2">{{ prof.last_online_at }}</h6>
                    <div v-if="prof.tahs">
                                          <div class="d-inline-block" >
                           
    <router-link v-for="item in prof.tahs.split(',')" v-bind:key="item" :to="{ name: 'tag', params: { tag: item} }" >
         <span class="badge rounded-pill bg-secondary" style="margin: 1px;">{{ item }}</span></router-link> 
                            
                        </div>
                        
                    </div>
                    <p class="card-text"></p><a class="card-link" href="#">Link</a><a class="card-link" href="#">Link</a>
                </div>
              
            </div>
        </p>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import { useToast } from "vue-toastification";

export default {
    
    name: 'Dash',
        setup() {
      // Get toast interface
      const toast = useToast();
      return { toast }
    },
    data() {
        return {
            profiles: [],
            errors: [],
        }
    },
    mounted() {
        this.getItemsProfiles()
    },

    methods: {
        async getItemsProfiles() {

            this.$store.commit('setIsLoading', true)

            axios
                .get('/api/v1/profiles/')
                .then(response => {
                     this.profiles = response.data
                     console.log(this.profiles)

                })

                
                .catch(error => {
                    console.log(error)
                  
                })

                this.$store.commit('setIsLoading', false)


            
        }
    }
}
</script>