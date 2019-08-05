import Vue from 'vue'
//import Vuetify from 'vuetify'
import Vuetify from './plugins/vuetify';
import Sample from "./Sample.vue"

Vue.config.productionTip = false


new Vue({
  Vuetify,
  render: h => h(Sample),
}).$mount('#app')

/*
new Vue({
  Vuetify,
  el: "#app",
  components: {Sample},
  template: "<Sample/>"
});
*/
