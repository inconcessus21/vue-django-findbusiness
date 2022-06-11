<template>
<div>
    <form v-on:submit.prevent="submitGroup()">
      <div class="col-md-8 col-lg-6 col-xl-5 col-xxl-4">
    <div class="card mb-5">
        

      <div class="card-body p-sm-5">
        <div class="mb-3">
          <input class="form-control" type="text" name="name" placeholder="Nazwa Grupy" v-model="passprojects.title" />
        </div>
        <div class="mb-3"><textarea  class="form-control" name="message" rows="6" v-model="passprojects.body" placeholder="Opis Grupy"></textarea></div>
      </div>
      <div><button class="btn btn-primary d-block w-100" type="submit">Dodaj Grupę </button></div>
          </div>
</div>
    </form>
    <router-link class="btn btn-danger" style="border-radius: 8px;" to='/grupymodlitewne' >Wstecz</router-link>
</div>
</template>


<script>
import axios from 'axios'
import { useToast } from "vue-toastification";

export default {
     name: 'addproject',
      setup() {
      // Get toast interface
      const toast = useToast();
      return { toast }
    },
    data() {
        return {
            results: [],
            errors: [],
            passprojects: {
              title: '',
              body: '',
            }
        }
    },





        methods: {

        
        submitGroup() {
          console.log("submitGroup")
                 this.$store.commit('setIsLoading', true)

            axios
                
                .post(`/api/v1/addproject/`, this.passprojects)
                .then(response => {
                     this.passprojects.title = ''
                     this.passprojects.body = ''
                    this.toast.success("Utworzono Grupę", {
                            position: "bottom-right",
                            timeout: 4000,
                            });
                })

                
                .catch(error => {
                    console.log(error.response.data)
                })

                this.$store.commit('setIsLoading', false)

                this.$router.push('/grupymodlitewne')
        },
        
          
      
}
}
</script>