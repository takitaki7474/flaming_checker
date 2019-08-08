<template>
  <v-app>

    <v-app-bar app color="red accent-3" dark>
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-bold font-italic">炎上チェッカー</span>
      </v-toolbar-title>
    </v-app-bar>



    <v-content>
      <HomeScreen></HomeScreen/>
      <v-container fluid fill-height justify-center style="height: 100px;">
        <v-layout wrap class="align-center justify-center row" style="height: 100px;">
          <UploadBtn></UploadBtn>
          <InputTextBtn></InputTextBtn>
        </v-layout>
      </v-container>
    </v-content>

  </v-app>

</template>

<script>
import UploadBtn from './components/UploadBtn.vue';
import InputTextBtn from './components/InputTextBtn.vue';
import HomeScreen from './components/HomeScreen.vue';

export default {
  name: 'App',
  components: {
    UploadBtn,
    InputTextBtn,
    HomeScreen,
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
.form-select-btn {
  display: flex;
  justify-content: center;
}
.select-btn {
  width: 200px;
  font-weight: bold;
}
</style>
