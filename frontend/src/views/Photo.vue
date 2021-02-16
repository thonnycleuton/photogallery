<template>
  <div class="single-question mt-2">
    <div class="container">
      {{ photo.title }}
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service";

export default {
  name: "Photo",
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      photo: {}
    };
  },
  methods: {
    getPhotoData() {
      let endpoint = "/api/photos/" + this.id + "/";
      apiService(endpoint).then(data => {
        this.photo = data;
      });
    }
  },
  created() {
    this.getPhotoData();
    console.log(this.endpoint)
  }
}
</script>

<style scoped>

</style>