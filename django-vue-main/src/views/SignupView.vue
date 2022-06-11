<template>
<div class="container">
    <div class="block-heading">
        <h2 class="text-info">Registration</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quam urna, dignissim nec auctor in, mattis vitae leo.</p>
    </div>
           
        <div class="alert alert-danger" role="alert" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{error}}</p>
        </div>
        

    

    <form @submit.prevent="submitForm">
        <div class="mb-3"><label class="form-label" for="email">Username</label><input id="username" class="form-control item" type="text" v-model="username" /></div>
        <div class="mb-3"><label class="form-label" for="email">Email</label><input id="email" class="form-control item" type="email" v-model="email" /></div>
        <div class="mb-3"><label class="form-label" for="password">Password</label><input id="password1" class="form-control item" type="password" v-model="password1" /></div>
        <div class="mb-3"><label class="form-label" for="password">Repeat-Password</label><input id="password2" class="form-control item" type="password" v-model="password2" /></div>

        
        
        <button class="btn btn-primary" type="submit">Signup</button>
 
    </form>
</div>
</template>

<script>
import axios from 'axios'
import { useToast } from "vue-toastification";

export default {
    
    name: 'Signup',
        setup() {
      // Get toast interface
      const toast = useToast();
      return { toast }
    },
    data() {
        return {
            username: '',
            email: '',
            password1: '',
            password2: '',
            errors: [],
        }
    },
  

    methods: {
        async submitForm() {


            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is missing!')
            }
            if (this.email === '') {
                this.errors.push('The email is missing!')
            }
            if (this.password1 === '') {
                this.errors.push('The password is missing!')
            } else {
            if (this.password1 !== this.password2) {
                this.errors.push('The passwords are not matching')
                }
            }

            if (!this.errors.length) {
                
                this.$store.commit('setIsLoading', true)

                const formData = {
                    username: this.username,
                    email: this.email,
                    password: this.password1,
                }
                await axios
                    .post('/api/v1/users/', formData)
                    .then(response => {
                            this.toast.success("Account created successfully", {
                                position: "bottom-right",
                                timeout: 4000,
                                });
                            this.$router.push('/login')
                    })

                    
                    .catch(error => {
                        if (error.response) {
                            for ( const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                            } 
                                } else if (error.message) {
                                    this.errors.push('Something went wrong. Please try again.')
                            }      
                        })

                    this.$store.commit('setIsLoading', false)


            }
        }
    }
}
</script>