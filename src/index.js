import Vue from 'vue'
import Sample from "./Sample.vue"

Vue.config.productionTip = false

new Vue({
  render: h => h(Sample),
}).$mount('#app')
