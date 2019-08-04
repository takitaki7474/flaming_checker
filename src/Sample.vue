<template>
  <img alt="Vue logo" :src="image_src">
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
