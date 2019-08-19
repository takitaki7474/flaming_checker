<template>
  <v-app>

    <v-app-bar app color="red accent-3" dark>
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-bold font-italic">火の用心</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-content>

      <v-container fluid>
        <v-layout wrap>

          <v-flex xs12>
            <div v-if="screenType === 'home'">
              <HomeScreen></HomeScreen>
            </div>
            <div v-else-if="screenType === 'imageCheck'">
              <ImageCheckScreen v-bind:img-url="displayURL" v-bind:flaming-value="flamingValue"></ImageCheckScreen>
            </div>
            <div v-else-if="screenType === 'inputText'">
              <TextInputScreen v-on:changeScreen="changeTextCheckScreen"></TextInputScreen>
            </div>
            <div v-else-if="screenType === 'textCheck'">
              <TextCheckScreen v-bind:message="displayMessage" v-bind:flaming-value="flamingValue" v-bind:comment="displayComment"></TextCheckScreen>
            </div>
          </v-flex>

          <v-flex xs12>
            <v-container fluid justify-center class="btn-container">
              <v-layout wrap class="align-center justify-center row" style="height: 100px;">
                <UploadBtn v-on:changeScreen="changeImageCheckScreen" v-on:changeURL="changeDisplayURL"></UploadBtn>
                <TextInputBtn v-on:changeScreen="changeTextInputScreen"></TextInputBtn>
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
import TextInputBtn from './components/TextInputBtn.vue';
import HomeScreen from './components/HomeScreen.vue';
import ImageCheckScreen from './components/ImageCheckScreen.vue';
import TextInputScreen from './components/TextInputScreen.vue';
import TextCheckScreen from './components/TextCheckScreen.vue';


export default {
  name: 'App',
  components: {
    UploadBtn,
    TextInputBtn,
    HomeScreen,
    ImageCheckScreen,
    TextInputScreen,
    TextCheckScreen,
  },
  data: () => ({
    screenType: "home",
    displayURL: "",
    displayMessage: "",
    displayComment: "",
    flamingValue: 70,
  }),
  methods: {
    changeImageCheckScreen() {
      this.screenType = "imageCheck";
    },
    changeTextInputScreen() {
      this.screenType = "inputText";
    },
    changeTextCheckScreen(message, comment, text_ans) {
      this.screenType = "textCheck";
      this.displayMessage = message;
      this.displayComment = comment;
      this.flamingValue = text_ans;
    },

    changeDisplayURL(img_url, img_ans) {
      this.displayURL = img_url;
      var min = 0 ;
      var max = 100 ;
      this.flamingValue = img_ans
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
/*600以上*/
@media screen and (min-width:600px){
  .display-text {
    width: 40vmin;
    height: 40vmin;
  }
  .display-img{
    width: 40vmin;
    height: 40vmin;
  }
  .comment-card{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    min-height: 100px;
  }
  #flaming-horizontal-bar {
    display: none !important;
  }
  .select-btn {
    font-weight: bold;
  }
  .home-text {
    font-size: 20px;
    color: #808080;
    text-align: center;
  }
}
/*600以下*/
@media screen and (max-width:600px){
  .display-text {
    width: 80vmin;
    height: 60vmin;
  }
  .display-img {
    width: 60vmin;
    height: 60vmin;
  }
  .container {
    padding: 0;
  }
  .img-container {
    display: flex;
    justify-content: center;
    padding: 50px 0;
  }
  .mark-flex {
    display: none !important;
  }
  .mark-text-layout {
    display: flex !important;
    justify-content: center !important;
    padding: 50px 0;
  }
  .bar-container {
    display: flex;
    justify-content: center;
    width: 80vmin !important;
    height: 10vmin !important;
  }
  #flaming-bar {
    display: none !important;
  }
  #flaming-horizontal-bar {
    border: 1px solid #000;
  }
  .comment-card {
    min-width: 80vmin;
    min-height: 30vmin;
  }
  .select-btn {
    font-size: 14px;
    width: 80vmin;
  }
  .btn-container {
    height: 200px;
  }
  .textarea-container {
    width: 80vmin;
  }
  .home-text {
    font-size: 16px;
    color: #808080;
    text-align: center;
  }
  .home-text-layout {
    padding: 0 15px;
  }
}
</style>
