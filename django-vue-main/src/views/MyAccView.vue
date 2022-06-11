<template>

<div class="container text-center">
    <div v-for="it in myaccount" v-bind:key="it.id">
   
        <div class="avatar"><img :src="it.avatar" style="width: 210px;height: 210px; border-radius: 20px;"></div>
            <div class="about-me">
         <h1>{{ it.username }}</h1>
         <h4>{{ it.about }}</h4>
            </div>
        
    </div>
</div>






</template>

<script>
import axios from 'axios'
export default {
    name: 'Myacc',

    data() {
        return {
            myaccount: [],
            
        }
    },
    mounted() {
        this.getItemsProjects()
    },
    methods: {
        async getItemsProjects() {

            this.$store.commit('setIsLoading', true)

            axios
                .get('/api/v1/myaccount/')
                .then(response => {
                     this.myaccount = response.data
                     console.log(this.myaccount)

                })

                
                .catch(error => {
                    console.log(error)
                  
                })

                this.$store.commit('setIsLoading', false)


            
        },
        
    }
}
</script>