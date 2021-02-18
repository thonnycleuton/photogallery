<template>
  <div class="home">
    <div class="container mt-2">
      <div v-for="photo in photos" :key="photo.pk">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ photo.title }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="photo.photo"
          alt
        >
      </div>
      <div class="col-md-6">
        <div class="recipe-details">
          <h4>Social</h4>
          <h4>Preparation time ⏱</h4>
          <p>{{ photo.likes_count }}</p>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  props: ["photo"],
  name: "home",
  data() {
    return {
      photos: []
    };
  },
  methods: {
    getPhotos() {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = "/api/photos/";
      apiService(endpoint).then(data => {
        this.photos.push(...data.results);
      });
    }
  },
  created() {
    this.getPhotos();
  }
};
</script>

<style scoped>
.question-author {
  font-weight: bold;
  color: #DC3545;
}

.question-link {
  font-weight: bold;
  color: black;
}

.question-link:hover {
  color: #343A40;
  text-decoration: none;
}
</style>

