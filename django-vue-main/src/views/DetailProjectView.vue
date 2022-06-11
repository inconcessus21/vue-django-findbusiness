<template>
<div>
  <p>Title: {{project.title}}</p>
  <p>Founder: {{project.who_create}}</p>
  <p>Describe: {{project.body}}</p>
  <p>Created: {{project.created_at}}</p>
  <div v-if="joined">
  <p>Members: {{ joined.length }}</p>
  <p v-for="user in project.joined" v-bind:key="user.id">  
    <p><img class="img-fluid" :src="user.avatarp" style="width: 50px;border-width: 1px;border-radius: 250px;" />  {{user.participant}}</p>

  </p>
</div>
</div>

</template>

<script>
import axios from 'axios'
import { useToast } from "vue-toastification";

export default {
    
    name: 'ProjectDetail',
        setup() {
      // Get toast interface
      const toast = useToast();
      return { toast }
    },
    data() {
        return {
            project: [],
            errors: [],
            joined: []
           
        }
    },
    mounted() {
        this.getItemsProjects()
    },

  props: {
    uuid: {
      type: String,
      required: true,
      
    },
  },
    methods: {
        async getItemsProjects() {

            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/v1/project/${this.uuid}`)
                .then(response => {
                     this.project = response.data
                     this.joined = response.data.joined
                     console.log(this.project)

                })

                
                .catch(error => {
                    console.log(error)
                  
                })

                this.$store.commit('setIsLoading', false)


            
        },
        
    }
}
</script>