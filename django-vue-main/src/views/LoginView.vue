<template>
<div class="container">
    <div class="block-heading">
        <h2 class="text-info">Login</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quam urna, dignissim nec auctor in, mattis vitae leo.</p>
    </div>
           
        <div class="alert alert-danger" role="alert" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{error}}</p>
        </div>
        

    

    <form @submit.prevent="submitForm">
        <div class="mb-3"><label class="form-label" for="username">Username</label><input id="username" class="form-control item" type="text" v-model="username" /></div>
        <div class="mb-3"><label class="form-label" for="password">Password</label><input id="password" class="form-control item" type="password" v-model="password" /></div>

        
        
        <button class="btn btn-primary" type="submit">Login</button>
 
    </form>


       



</div>

</template>

<script>
import axios from 'axios'
import { useToast } from "vue-toastification";


export default {
   
    name: 'LoginView',
        setup() {
      // Get toast interface
      const toast = useToast();
      return { toast }
    },

    data() {
        return {
            username: '',
            password: '',
            errors: [],
         
        
        
        }
    },




    methods: {

        async submitForm() {
            
            this.$store.commit('setIsLoading', true)

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem['token']

            this.errors = []

            
            const formData = {
                username: this.username,
                password: this.password,
            }
            await axios
                .post('/api/v1/token/login/', formData)
                .then(response => {

                    const token = response.data.auth_token
                    
                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common['Authorization'] = 'Token ' + token

                    localStorage.setItem('token', token)

                    this.toast.success("Pomyślnie zalogowano", {
                            position: "bottom-right",
                            timeout: 4000,
                            });
                            
              

                    this.$router.push('/')
                })
                .catch(error => {
                    if (error.response) {
                        for ( const property in error.response.data) {
                            if (`${error.response.data[property]}` === 'Unable to log in with provided credentials.') {
                                 this.errors.push("Unable to log in with provided credentials.")
                            }
                       
                         } 
                            } else if (error.message) {
                                this.errors.push('Something went wrong. Please try again.')
                         }      
                    })

                this.$store.commit('setIsLoading', false)
                

                    
            
        }
    }
}
</script>
