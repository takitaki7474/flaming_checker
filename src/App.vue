<template>
  <v-app>

    <v-app-bar app color="red accent-3" dark>
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-bold font-italic">炎上チェッカー</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-content>

      <v-container fluid fill-height>
        <v-layout wrap>

          <v-flex xs12>
            <div v-if="screenType === 'home'">
              <HomeScreen></HomeScreen>
            </div>
            <div v-else-if="screenType === 'imageCheck'">
              <ImageCheckScreen v-bind:img-url="displayURL" v-bind:random-num="randomNum"></ImageCheckScreen>
            </div>
          </v-flex>

          <v-flex xs12>
            <v-container fluid fill-height justify-center>
              <v-layout wrap class="align-center justify-center row" style="height: 100px;">
                <UploadBtn v-on:changeScreen="changeImageCheckScreen" v-on:changeURL="changeDisplayURL"></UploadBtn>
                <InputTextBtn></InputTextBtn>
              </v-layout>
            </v-container>
          </v-flex>

        </v-layout>
      </v-container>


    </v-content>

  </v-app>

</template>

<script>
import UploadBtn from './components/UploadBtn.vue';
import InputTextBtn from './components/InputTextBtn.vue';
import HomeScreen from './components/HomeScreen.vue';
import ImageCheckScreen from './components/ImageCheckScreen.vue';

export default {
  name: 'App',
  components: {
    UploadBtn,
    InputTextBtn,
    HomeScreen,
    ImageCheckScreen,
  },
  data: () => ({
    screenType: "home",
    displayURL: "",
    randomNum: 70,
  }),
  methods: {
    changeImageCheckScreen() {
      this.screenType = "imageCheck";
    },
    changeDisplayURL(img_url) {
      this.displayURL = img_url;
      var min = 0 ;
      var max = 100 ;
      this.randomNum = Math.floor( Math.random() * (max + 1 - min) ) + min ;
    }
  }
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
