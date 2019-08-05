

<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title>
        <span>aaa</span>
      </v-toolbar-title>
    </v-toolbar>
    <img alt="Vue logo" :src="image_src">
    <Header />
  </v-app>
</template>


<script>
import Header from "./Header.vue";
export default {
  components: {
    Header
  },
  data () {
      return {
          image_src: require("./images/logo.png") // ←
      }
  }
}
</script>
