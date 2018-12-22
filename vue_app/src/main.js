
import { routes } from './components/Router.vue'

import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(VueRouter)


const router = new VueRouter({
  mode: 'history',
  base: '/latest/',
  routes
})

new Vue({
  el: '#latest657',
  router
});
