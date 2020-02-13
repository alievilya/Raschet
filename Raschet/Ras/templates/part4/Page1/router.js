import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: '/index'
    },
    {
      path: "/count",
      name: "count",
      component: () => import("./components/Count.vue")
    },
    // {
    //   path: "/edit/:id",
    //   name: "edit",
    //   component: () => import("./components/Edit.vue")
    // },
    // {
    //   path: "/index",
    //   name: "index",
    //   component: () => import("./components/Index.vue")
    // },
  ]
});
