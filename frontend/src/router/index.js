import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home";
import Photo from "@/views/Photo";
import PhotoEditor from "@/views/PhotoEditor";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/photo/:id",
      name: "photo",
      component: Photo,
      props: true
    },
    {
      path: "post",
      name: "photo-editor",
      component: PhotoEditor,
      props: true
    }
  ]
});

