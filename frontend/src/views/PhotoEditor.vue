<template>
  <div class="container mt-2">
    <h1 class="mb-3">Ask a Question</h1>
    <form @submit.prevent="onSubmit">
      <textarea
        v-model="question_body"
        class="form-control"
        placeholder="What do you want to ask?"
        rows="3"></textarea>
      <br>
      <button
        type="submit"
        class="btn btn-success"
        >Send
      </button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
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
      question_body: null,
      error: null
    };
  },
  methods: {
    onSubmit() {
      // Tell the REST API to create or update a Question Instance
      if (!this.question_body) {
        this.error = "You can't send an empty question!";
      } else if (this.question_body.length > 240) {
        this.error = "Ensure this field has no more than 240 characters!";
      } else {
        let endpoint = "/api/photos/";
        let method = "POST";
        if (this.id !== undefined) {
          endpoint += this.id + `/`;
          method = "PUT";
        }
        apiService(endpoint, method, { content: this.question_body })
          .then(photo_data => {
            this.$router.push({
              name: "photo",
              params: { id: photo_data.id }
            })
          })
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a question, then get the question's data from the REST API
    if (to.params.id !== undefined) {
      let endpoint = `/api/questions/${ to.params.id }/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.photo_body = data.title))
    } else {
      return next();
    }
  },
  created() {
    document.title = "Editor - QuestionTime";
  }
}
</script>
