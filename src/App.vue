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

    <v-content>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
  },
  data: () => ({
    //
  }),
};
</script>

<style>
.v-toolbar__content {
  justify-content: center;
}
.bar {
  display: flex;
  justify-content: center;
}
</style>
