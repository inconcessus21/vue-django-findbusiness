<template>
<div class="container">
    <div class="block-heading">
      <div>
        <form v-on:submit.prevent="submitBusiness()">
          <div class="card-body p-sm-5">
            <div class="mb-3">
              <input class="form-control" type="text" name="name" placeholder="Nazwa Firmy" v-model="business.businessName" />
            </div>
            <div class="mb-3">
              <textarea  class="form-control" name="message" rows="6" v-model="business.description" placeholder="Opis Firmy"></textarea>
            </div>
            <div class="mb-3">
              <input class="form-control" type="text" name="name" placeholder="Miasto" v-model="business.city" />
          </div>
          <div class="mb-3"> 
            <select  v-model="business.category" class="form-select" >
              <optgroup  label="Kategorie">
                <option v-for="category in categories" v-bind:key="category.id" :value="category.id">{{category.category_name}}</option>
              </optgroup>
            </select>
          </div>  
          <div class="mb-3">
            <label for="formFile" class="form-label">Zdjęcie/Logo</label>
              <input class="form-control" type="file" v-on:change="onFileSelected" />
                
          </div>
            <div class="mb-3">
              <input class="form-control" type="text" name="name" placeholder="Strona WWW" v-model="business.www" />
            </div>
            <div class="mb-3">
              <input class="form-control" type="text" name="name" placeholder="Telefon" v-model="business.phoneNumber" />
            </div>
            <div class="mb-3">
              <input class="form-control" type="text" name="name" placeholder="Email" v-model="business.email" />
            </div>
          <div><button class="btn btn-primary d-block w-100" type="submit">Dodaj Firmę </button></div>
    </div>
        </form>
{{business.image}}
    <router-link class="btn btn-danger" style="border-radius: 8px;" to='/' >Wstecz</router-link>
</div>
</div>
</div>
</template>

<script>
import axios from 'axios'
import { useToast } from "vue-toastification";

export default {
    
    name: 'AddBusiness',
        setup() {
      // Get toast interface
      const toast = useToast();
      return { toast }
    },
    data() {
        return {
            categories: [],
            errors: [],
            business: {
              businessName: '',
              description: '',
              city: '',
              www: '',
              phoneNumber: '',
              email: '',
              category: '',
              image: null,
            }
        }
    },
  

  mounted() {
      this.getCategories()   
    },

    methods: {
      onFileSelected(event) {
      this.business.image = event.target.files
    },
 
       async getCategories() {

            this.$store.commit('setIsLoading', true)

            axios
                .get('/api/v1/categories/')
                .then(response => {
                     this.categories = response.data

                })

                
                .catch(error => {
                    console.log(error)
                  
                })

                this.$store.commit('setIsLoading', false)


            
        },
        async submitBusiness() {

            this.$store.commit('setIsLoading', true)
            const fd = new FormData();
            fd.append('businessName', this.business.businessName)
            fd.append('description', this.business.description)
            fd.append('city', this.business.city)
            fd.append('www', this.business.www)
            fd.append('phoneNumber', this.business.phoneNumber)
            fd.append('email', this.business.email)
            fd.append('category', this.business.category)
            fd.append('image', this.business.image[0], this.business.image[0].name)

            axios
                .post(`/api/v1/addfirma/`, fd)
                .then(response => {
                    this.business = response.data
                    console.log(fd)

                    this.toast.success(`Pomyślnie utworzono firmę ${this.business.businessName }`, {
                    position: "bottom-right",
                    timeout: 4000,
                    });

                })

                
                .catch(error => {
                    console.log(error.response.data)
                })

                this.$store.commit('setIsLoading', false)


            
        }
    }
}
</script>
