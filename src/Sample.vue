<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title>
        <span>aaa</span>
      </v-toolbar-title>
    </v-toolbar>
    <img alt="Vue logo" :src="image_src">
  </v-app>

</template>


<script>
export default {
  data () {
      return {
          image_src: require("./images/logo.png") // ←
      }
  }
}
</script>
