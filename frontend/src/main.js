import Vue from 'vue'
import App from './App.vue'
import router from '@/router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

Vue.config.productionTip = false
Vue.use(Buefy)

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
