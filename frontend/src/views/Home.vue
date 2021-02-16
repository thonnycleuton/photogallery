<template>
  <div class="home">
    <div class="container mt-2">
      <div v-for="photo in photos"
           :key="photo.pk">
        <p class="mb-0">Posted by:
          <span class="question-author">{{ photo.author }}</span>
        </p>
        <h2>
          <router-link
            :to="{ name: 'photo', params: { id: photo.id } }"
            class="question-link"
            >{{ photo.title }}
          </router-link>
        </h2>
        <p>Answers: {{ photo.id }}</p>
        <p>Likes: {{ photo.likes_count }}</p>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
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
        this.photos.push(...data.results)
      })
    }
  },
  created() {
    this.getPhotos();
  }
};
</script>

<style>
.author-name {
  font-weight: bold;
  color: #DC3545;
}
</style>

