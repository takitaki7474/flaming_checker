<template>
  <v-flex xs12 class="form-select-btn">
    <v-btn rounded small color="warning" class="select-btn" style="font-weight: bold;" v-on:click="inputBtnClick">テキストを入力</v-btn>
  </v-flex>
</template>

<script>
export default {
  name: "TextInputBtn",
  data: () => ({
    //
  }),
  methods: {
    inputBtnClick: function() {
      this.$emit("changeScreen");
    }
  }
};
</script>
