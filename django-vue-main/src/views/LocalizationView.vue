<template>
  <section class="portfolio-block projects-cards">
    <div class="container">
      <div class="heading">
        <h2>{{ firma.business_name }}</h2>
      </div>
      <div class="row">
        <p>{{ firma.opis }}</p>
        <p>{{ firma.strona_www }}</p>
        <p>{{ firma.miasto }}</p>
        <GoogleMap
          api-key=":-)"
          style="width: 100%; height: 500px"
          :center="center"
          :zoom="10"
        >
          {{ center }}
          <div v-for="point in markerOptions" v-bind:key="point">
            {{ point }}
            <Marker :options="{ position: { point } }" />
          </div>
        </GoogleMap>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import { GoogleMap, Marker } from "vue3-google-map";

export default {
  name: "LokalizacjeView",
  setup() {
    // Get toast interface
    // const toast = useToast();
    // return { toast }
  },
  data() {
    return {
      center: { lat: 51.093048, lng: 6.84212 },

      firma: [],
      errors: [],
      myArray: [],
      markerOptions: [],
    };
  },
  components: { GoogleMap, Marker },

  mounted() {
    this.getGeoLok();
  },

  methods: {
    async getGeoLok() {
      this.$store.commit("setIsLoading", true);

      axios
        .get(`/api/v1/lokalizacje/`)
        .then((response) => {
          this.firma = response.data;

          for (const property in Object.values(this.firma)) {
            this.myArray.push(this.firma[property].localization.split(","));
            console.log("log", this.myArray);
          }
          this.myArray.forEach((each) =>
            this.markerOptions.push(`lat: ${each[0]}, lng: ${each[1]}`)
          );
          // const [lat, lng] = this.myArray
          // this.markerOptions = this.markerOptions.concat({lat: parseFloat(lat), lng: parseFloat(lng)});

          console.log(this.markerOptions);
        })

        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
