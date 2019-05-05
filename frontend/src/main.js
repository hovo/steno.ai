import Vue from 'vue'
import App from './App.vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.config.productionTip = false
Vue.use(Buefy)
Vue.use(VueRouter)

new Vue({
  render: h => h(App),
}).$mount('#app')
