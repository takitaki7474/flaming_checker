<template>

<v-container fluid fill-height justify-center>
  <v-layout wrap class="align-center justify-center row">
    <v-flex xs12 sm10 md8 lg6 xl4>
      <v-textarea color="teal" rows="20">
         <template v-slot:label>
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
import TextCheckBtn from "./TextCheckBtn.vue";

export default {
  name: 'inputTextScreen',
  components: {
    TextCheckBtn,
  },
  data: () => ({

  }),
  methods: {
    changeTextCheckScreen: function() {
      console.log("change to TextCheckScreen")
    }

  }
};
</script>

<style>

</style>
