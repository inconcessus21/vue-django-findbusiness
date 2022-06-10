<template>
  <section class="portfolio-block projects-cards">
    <div class="container">
      <div class="heading">
        <h2>{{ propCategory }}</h2>
      </div>
      <div class="row">
        <div
          v-for="category in categories"
          v-bind:key="category.id"
          class="col-md-6 col-lg-4"
        >
          <div class="card border-1">
            <a href="#"
              ><img
                class="card-img-top scale-on-hover"
                :src="category.image"
                alt="Card Image"
            /></a>
            <div class="card-body">
              <h6>
                <router-link
                  :to="{
                    name: 'BusinessDetails',
                    params: { uuid: category.uuid },
                  }"
                  >{{ category.business_name }}</router-link
                >
              </h6>
              <p class="text-muted card-text">{{ category.description }}</p>

              <p></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "BusinessInCategory",
  setup() {
    // Get toast interface
    // const toast = useToast();
    // return { toast }
  },
  data() {
    return {
      categories: [],
      errors: [],
    };
  },
  mounted() {
    this.getCategories();
  },

  props: {
    propCategory: {
      type: String,
      required: true,
    },
  },

  methods: {
    async getCategories() {
      this.$store.commit("setIsLoading", true);

      axios
        .get(`/api/v1/category/${this.propCategory}/`)
        .then((response) => {
          this.categories = response.data;
        })

        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
