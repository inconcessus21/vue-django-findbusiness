<template>
  <div class="about">
    <h1>You looking: {{tag}}</h1>
    <div v-for="result in results" :key="result.id">
      <div>{{result.username}}</div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
export default {
     name: 'TagView',

    data() {
        return {
            results: [],
            errors: [],
            
        }
    },

      props: {
        tag: {
        type: String,
        required: true, 
    },
    },

    mounted() {
      this.getTagsResults()
    },

        methods: {
        async getTagsResults() {

            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/v1/tag/?tahs=${this.tag}`)
                .then(response => {
                     this.results = response.data
                     console.log('from ', this.results)

                })

                
                .catch(error => {
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)


            
        },
}
}
</script>