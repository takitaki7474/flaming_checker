<template>

<v-container fluid fill-height justify-center class="textarea-container" style="padding: 50px 0;">
  <v-layout wrap class="align-center justify-center row">
    <v-flex xs12 sm10 md8 lg6 xl4>
      <v-textarea v-model="message" color="teal" rows="20">
         <template v-slot:label class="text-input-area">
           <div>
             投稿前のテキストを入力してください
           </div>
         </template>
       </v-textarea>
    </v-flex>
    <TextCheckBtn v-on:changeScreen="changeTextCheckScreen"></TextCheckBtn>
  </v-layout>
</v-container>

</template>

<script>
import axios from 'axios';
import TextCheckBtn from "./TextCheckBtn.vue";

export default {
  name: 'TextInputScreen',
  components: {
    TextCheckBtn,
  },
  data: () => ({
    message: ""

  }),
  methods: {
    changeTextCheckScreen: function() {
      //this.postParam(this.message);
      //this.$emit("changeScreen", this.message);
      this.postParam(this.message, this.TransfarText);
    },
    TransfarText(text, word, ans) {
      this.$emit("changeScreen", text, word, ans);
    },
    postParam(textData, callback) {
      const text = textData
      const params = new URLSearchParams();
      params.append('input-text', text);

      axios.post(
        'http://localhost:5000/post_text',
        params,
        {
          headers: {
            'content-type': 'application/x-www-form-urlencoded',
          }
        }
      ).then(response => {
        callback(text, response.data.text, response.data.text_ans);
        }).catch(error => {
          console.log("uploading failure");
        });
    }

  }
};
</script>

<style>

</style>
