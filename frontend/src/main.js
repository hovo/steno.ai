import Vue from 'vue'
import App from './App.vue'
import router from '@/router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import VuePlyr from 'vue-plyr'
import 'vue-plyr/dist/vue-plyr.css'
import Vuex from 'vuex'

Vue.config.productionTip = false
Vue.use(Buefy)
Vue.use(VuePlyr)
Vue.use(Vuex)

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
