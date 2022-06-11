<template>

</template>

<script>
import axios from 'axios'
import { useToast } from "vue-toastification";
import store from '@/store/index.js';



const timeoutInMS = 3000; // 3 minutes -> 3 * 60 * 1000
let timeoutId;
export default {
    name: 'Online',


    setup() {
      // Get toast interface
      const toast = useToast();
      
      return { toast }
    },
    data() {
        return {
            is_online: '',
            id: [],
            timeoutId: '',
            
        }
    },

watch: {
  '$store.state.isAuthenticated': {
    deep: true,
    handler(newVal) {
        console.log(store.state.isAuthenticated)
        if (store.state.isAuthenticated){
            this.getId()
        }
    }
  },
   is_online: {
    deep: true,
    handler(newVal) {
        if (!this.is_online){
            this.Activate()
        }
    }
  }
},

  mounted() {
    this.mnt()
    
},





    methods: {

            mnt() {
        if (!this.is_online) {
            this.getId()
            this.Activate()
        }
    },

        async getId(id) {
            await axios

                .get('/api/v1/profile/')
                .then(response => {
                     this.id = response.data[0].id
                     this.is_online = response.data[0].is_online
                     console.log(this.id)
                     console.log('Funkcja is online', this.is_online)

                })

                .catch(error => {
                    console.log(JSON.stringify(error))
                })

        },

        async offline(id) {
            await axios

                .put(`/api/v1/online/${this.id}/`, { is_online: 'false' } )

                .then(response => {
                    this.is_online = false
                    console.log('Offline')
                    
                })
                // .catch(error => {
                //     console.log(JSON.stringify(error))
                // })

        },
        async online(id) {
            await axios

                .put(`/api/v1/online/${this.id}/`, { is_online: 'true' } )

                .then(response => {
                    this.is_online = true
                    console.log('Online')
                    
                })
                // .catch(error => {
                //     console.log(JSON.stringify(error))
                // })

        },
        
  
    handleInactive() {
        
        this.is_online = false
        console.log('Online', this.is_online)
        this.offline()
  
        },

    startTimer() { 
    // setTimeout returns an ID (can be used to start or clear a timer)
    timeoutId = setTimeout(this.handleInactive, timeoutInMS);

},

    resetTimer() { 
    
    if (!this.is_online) {
        this.is_online = true
        this.online()
        console.log('Online',this.is_online)
        clearTimeout(timeoutId);
        this.startTimer() 
    }

},
 

    setupTimers() {
    
     document.addEventListener("keypress", this.resetTimer, false);
     document.addEventListener("mousemove", this.resetTimer, false);
     document.addEventListener("mousedown", this.resetTimer, false);
     document.addEventListener("touchmove", this.resetTimer, false);
     
    this.startTimer();
},

    Activate() {
    
     document.addEventListener("keypress", this.resetTimer, false);
     document.addEventListener("mousemove", this.resetTimer, false);
     document.addEventListener("mousedown", this.resetTimer, false);
     document.addEventListener("touchmove", this.resetTimer, false);
     
},

}
}
</script>

