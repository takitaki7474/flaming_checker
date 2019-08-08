<template>
  <v-app>
    <v-app-bar app color="red accent-3" dark>
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-bold font-italic">炎上チェッカー</span>
      </v-toolbar-title>
      <!--
      <v-spacer></v-spacer>
      <v-btn
        text
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn>
    -->
    </v-app-bar>

    <HomeScreen></HomeScreen/>
      
  </v-app>
</template>

<script>
import HomeScreen from './components/HomeScreen.vue';

export default {
  name: 'App',
  components: {
    HomeScreen,
  },
  data: () => ({
    //
  }),
};
</script>

<style>

</style>
