<template>
<div>

    
            <div class="card" style="min-width: 350px;min-height: 400px;margin: 5px;border-radius: 15px;">
                
                    <div class="card-body text-center">
                        <img class="img-fluid" :src="profile.avatar" style="width: 150px;border-width: 1px;border-radius: 100px;" />
                        <h4 class="card-title">{{ profile.username }}
                        <fa v-if="profile.is_online" icon="circle" data-bs-toggle="tooltip" title="Online" style="color: rgb(0,197,67);font-size: 12px;padding: 0px;margin-top: 0px;" /></h4>
                        <h6 class="text-muted card-subtitle mb-2">{{ profile.last_online_at }}</h6>
                        <h6 class="text-muted card-subtitle mb-2">{{ profile.about }}</h6>
                        <div v-if="profile.tahs">
                        <div class="d-inline-block" >
                           
    <router-link v-for="item in profile.tahs.split(',')" v-bind:key="item" :to="{ name: 'tag', params: { tag: item} }" >
         <span class="badge rounded-pill bg-secondary" style="margin: 1px;">{{ item }}</span></router-link> 
                            
                        </div>
                        </div>
                       
                    <div v-if="myprojects.who_create == profile.username">Grupy stworzone przez : {{profile.username}}
                    </div>
                      <div v-for="my in myprojects" v-bind:key="my.id">
                      <div v-if="my.who_create == profile.username" >

                        <p> <router-link
                    :to="{ name: 'project', params: { uuid: my.uuid } }" >
                    {{ my.title }}
                    </router-link></p>
                      </div>
                     </div> 
                    </div> 

                    <div v-for="myjoi in myjoined" v-bind:key="myjoi.id">
                    {{ myjoi.joined}}
                    <div v-if="profile.id === myjoi.joined">Grupy w których jest zapisany : {{profile.username}}
                                         <p> <router-link
                    :to="{ name: 'project', params: { uuid: myjoi.uuid } }" >
                    {{ myjoi.title }}
                    </router-link></p>
                  
                    </div>  
                    </div>
                
            </div>

</div>
</template>

<script>
import axios from 'axios'
import { useToast } from "vue-toastification";

export default {
    
    name: 'Profile',
        setup() {
      // Get toast interface
      const toast = useToast();
      return { toast }
    },
    props: {
        username: {
        type: String,
        required: true, 
    },
    },
    data() {
        return {
            profile: [],
            errors: [],
            myprojects: [],
            myjoined: [],
        }
    },

    computed: {
        arrayFiltered() {
        return this.profile.filter(elem => elem === this.myjoined.id);
        }
    },
    // watch:{
    // $route (to, from){
    //     this.reloadPage()
        
    // }
    // },

    mounted() {
        this.getItemsProfile()
        this.getMyProjects()
        this.getJoined()
    },

    methods: {
        
            reloadPage() {
                 window.location.reload();
            },
        async getItemsProfile() {

            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/v1/profile/${this.username}`)
                .then(response => {
                     this.profile = response.data
                     console.log(this.profile)

                })

                
                .catch(error => {
                    console.log(error)
                    console.log(this.profile)
                })

                this.$store.commit('setIsLoading', false)


            
        },
        async getMyProjects() {

            this.$store.commit('setIsLoading', true)

            axios
                .get('/api/v1/myproject/')
                .then(response => {
                     this.myprojects = response.data
                     console.log(this.myprojects)
                     

                })

                
                .catch(error => {
                    console.log(error)
                  
                })

                this.$store.commit('setIsLoading', false)


            
        },
        async getJoined() {

            this.$store.commit('setIsLoading', true)

            axios
                .get('/api/v1/joined/')
                .then(response => {
                     this.myjoined = response.data
                     console.log('joined ',this.myjoined)
                     

                })

                
                .catch(error => {
                    console.log(error)
                  
                })

                this.$store.commit('setIsLoading', false)


            
        }
    }
}
</script>