<template>
  <v-app>
    <v-app-bar app>
      <Header />
    </v-app-bar>
    <v-content>
      {{name}}
    </v-content>
  </v-app>
</template>


<script>
import Header from "./components/Header.vue";
export default {
  components: {
    Header
  },
  data: () => ({
    name: "aaa"
  }),
}
</script>
