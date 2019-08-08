<template>
  <!--
  <v-flex xs12 class="form-select-btn">
    <v-btn rounded small color="warning" class="select-btn" style="font-weight: bold;">画像をアップロード</v-btn>
  </v-flex>
-->
  <v-flex xs12 class="upload-form">
    <v-btn v-on:click="inputClick" rounded small color="warning" class="select-btn" style="font-weight: bold;">画像をアップロード</v-btn>
    <input class="form-button" type="file" name="file-submit" id="upload-btn"/>
  </v-flex>
</template>

<script>
export default {
  name: "UploadBtn",
  data: () => ({
  }),
  methods: {
    inputClick: function() {
      document.getElementById("upload-btn").click();
    }
  }
};
</script>

<style>
.button-item:hover {
  box-shadow: none;
  background-color: #FFF;
  color: #0066FF;
  border: 1px solid #0066FF;
}

.upload-form {
  margin: 5px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 70px;
}

.form-button {
  display: none;
}
</style>
