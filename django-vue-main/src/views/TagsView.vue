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
     name: 'TagsView',

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
                
                .get(`/api/v1/tags/`)
                .then(response => {
                     this.results = response.data
                     console.log(this.results)

                })

                
                .catch(error => {
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)


            
        },
}
}
</script>