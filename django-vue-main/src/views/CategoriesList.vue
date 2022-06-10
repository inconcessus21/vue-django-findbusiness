<template>
  <section class="portfolio-block projects-cards">
    <div class="container">
      <div class="heading">
        <h2>Kategorie</h2>
      </div>
      <div class="row">
        <div
          v-for="category in categories"
          v-bind:key="category.id"
          class="col-md-6 col-lg-4"
        >
          <div class="card border-0">
            <a href="#"
              ><img
                class="card-img-top scale-on-hover"
                :src="category.category_img"
                alt="Card Image"
            /></a>
            <div class="card-body">
              <h6>
                <router-link
                  :to="{
                    name: 'BusinessInCategory',
                    params: { propCategory: category.category_name },
                  }"
                  >{{ category.category_name }}</router-link
                >
              </h6>
              <p class="text-muted card-text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc
                quam urna.
              </p>
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
  name: "CategoriesList",

  data() {
    return {
      categories: [],
      errors: [],
    };
  },
  mounted() {
    this.getItemsProfiles();
  },

  methods: {
    async getItemsProfiles() {
      this.$store.commit("setIsLoading", true);

      axios
        .get("/api/v1/categories/")
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
