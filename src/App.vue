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

      <v-container fluid fill-height justify-center style="height: 500px;">
        <v-layout wrap class="align-center justify-center row">
          <p class="home-text">炎上度をチェックします.<br>画像またはテキストをアップロードしてください.</p>
        </v-layout>
      </v-container>

      <v-container fluid fill-height justify-center style="height: 100px;">
        <v-layout wrap class="align-center justify-center row">
          <v-flex xs12 sm6 class="form-select-btn">
            <v-btn small color="primary">Primary</v-btn>
          </v-flex>
          <v-flex xs12 sm6 class="form-select-btn">
            <v-btn small color="primary">Primary</v-btn>
          </v-flex>
        </v-layout>
      </v-container>

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
.home-text {
  font-size: 20px;
  color: #808080;
  text-align: center;
}
.form-select-btn {
  display: flex;
  justify-content: center;
}

</style>
