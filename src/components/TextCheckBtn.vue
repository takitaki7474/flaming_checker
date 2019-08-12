<template>
  <v-flex xs12 class="form-select-btn">
    <v-btn rounded small color="primary" class="select-btn" style="font-weight: bold;" v-on:click="checkBtnClick">炎上度を判定</v-btn>
  </v-flex>
</template>

<script>
export default {
  name: "TextCheckBtn",
  data: () => ({
    //
  }),
  methods: {
    checkBtnClick: function() {
      this.$emit("changeScreen");
    }
  }
};
</script>
