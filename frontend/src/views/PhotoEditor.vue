
<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase"> Titulo aqui</h2>
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitPhoto">
          <div class="form-group">
            <label for>Recipe Name</label>
            <input type="text" class="form-control" v-model="photo.title">
          </div>
          <div class="form-group">
            <label for>Food picture</label>
            <input type="file" name="file" @change="onFileChange">
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </main>
</template>

<script>
import axios from "axios";
import { CSRF_TOKEN } from "@/common/csrf_token";
export default {
  name: "PhotoEditor",
  props: {
    id: {
      type: Number,
      required: false
    }
  },
  data() {
    return {
      photo: {
        title: "",
        picture: null
      },
      preview: ""
    };
  },
  methods: {
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.photo.picture = files[0];
      this.createImage(files[0]);
    },
    createImage(file) {
      // let image = new Image();
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    submitPhoto() {
      const config = {
        headers: {
          "content-type": "multipart/form-data",
          "X-CSRFTOKEN": CSRF_TOKEN
        }
      };
      let formData = new FormData();
      let endpoint = "/api/photos/";
      for (let data in this.photo) {
        formData.append(data, this.photo[data]);
      }
      // const config2 = apiService(endpoint, method,formData)
      try {
        // eslint-disable-next-line no-unused-vars
        axios.post(endpoint, formData, config);
        this.$router.push("/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
