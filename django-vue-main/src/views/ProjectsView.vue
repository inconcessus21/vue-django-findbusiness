<template>
<div>
<router-link class="btn btn-success" style="border-radius: 8px;" to='/grupymodlitewne/dodajgrupe' >Dodaj Grupę</router-link>
<div class="container d-flex d-xl-flex justify-content-xl-center">
    
    <div class="d-flex d-sm-flex d-md-flex d-lg-flex d-xl-flex justify-content-center flex-wrap justify-content-sm-center justify-content-md-center justify-content-lg-center justify-content-xl-center">
           

               

        
        <div v-for="prof in projects" v-bind:key="prof.id">
        <div class="card" style="width: 285px;height: 400px;margin: 5px;border-radius: 15px;">
              
                <div class="card-body text-center">
                    <h4 class="card-title">

                    <router-link
                    :to="{ name: 'project', params: { uuid: prof.uuid } }" >
                    {{ prof.title }}
                    </router-link>

                    </h4>
                    <h6 class="text-muted card-subtitle mb-2">{{ prof.short_body }}</h6>
                    <div v-if="prof.proj_tags">
                        <p>Project tags:</p>
                    <div class="d-inline-block" v-for="tag in prof.proj_tags.split(',')" v-bind:key="tag">
                        <span class="badge rounded-pill bg-secondary" style="margin: 1px;">{{tag}}</span>
                    </div>
                    </div>
                </div>
              
            </div>
        </div>
    </div>
</div>
</div>
</template>

<script>
import axios from 'axios'
import { useToast } from "vue-toastification";
import Project from '@/views/DetailProjectView.vue'

export default {
    
    name: 'Projects',
        setup() {
      // Get toast interface
      const toast = useToast();
      return { toast }
    },
    data() {
        return {
            projects: [],
            errors: [],
        }
    },
    mounted() {
        this.getItemsProjects()
    },

    components: {
    Project,
    
  },

    methods: {
        async getItemsProjects() {

            this.$store.commit('setIsLoading', true)

            axios
                .get('/api/v1/projects/')
                .then(response => {
                     this.projects = response.data
                     console.log(this.projects)

                })

                
                .catch(error => {
                    console.log(error)
                  
                })

                this.$store.commit('setIsLoading', false)


            
        },
        
    }
}
</script>