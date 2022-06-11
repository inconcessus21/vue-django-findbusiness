<template>
  <section class="portfolio-block projects-cards">
    <div class="container">
      <div class="heading">
        <a href="#">
          <img
            style="width: 200px; height: 200px"
            class="card-img-top scale-on-hover"
            :src="business.image"
            alt="Card Image"
          />
        </a>
        <h2>{{ business.business_name }}</h2>
      </div>
      <div class="row">
        <p>{{ business.description }}</p>
        <p>{{ business.website }}</p>
        <p>{{ business.city }}</p>
        <GoogleMap
          api-key=":-)"
          style="width: 100%; height: 500px"
          :center="center"
          :zoom="15"
        >
          <Marker :options="{ position: center }" />
        </GoogleMap>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import { GoogleMap, Marker } from "vue3-google-map";

export default {
  name: "BusinessDetails",
  setup() {
    // Get toast interface
    // const toast = useToast();
    // return { toast }
  },
  data() {
    return {
      business: [],
      errors: [],
      center: "",
      lok: "",
    };
  },
  components: { GoogleMap, Marker },

  props: {
    uuid: {
      type: String,
      required: true,
    },
  },

  mounted() {
    this.getItemsProfiles();
  },

  methods: {
    async getItemsProfiles() {
      this.$store.commit("setIsLoading", true);

      axios
        .get(`/api/v1/businessdetail/${this.uuid}/`)
        .then((response) => {
          this.business = response.data;
          this.lok = response.data.localization;
          const [lat, lng] = this.lok.split(",");
          console.log(lat, lng);
          this.center = { lat: parseFloat(lat), lng: parseFloat(lng) };
        })

        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
