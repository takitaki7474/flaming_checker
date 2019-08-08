<template>
  <!--
  <v-flex xs12 class="form-select-btn">
    <v-btn rounded small color="warning" class="select-btn" style="font-weight: bold;">画像をアップロード</v-btn>
  </v-flex>
-->
  <v-flex xs12 class="upload-form">
    <v-btn v-on:click="inputClick" rounded small color="warning" class="select-btn" style="font-weight: bold;">画像をアップロード</v-btn>
    <input class="form-button" type="file" name="file-submit" id="upload-btn" v-on:change="uploadImageFile"/>
    <img v-show="uploadedImage" class="preview-item-file" :src="uploadedImage" alt="" />
  </v-flex>
</template>

<script>
import axios from 'axios';

export default {
  name: "UploadBtn",
  data: () => ({
    uploadedImage: '',
    img_name: '',
  }),
  methods: {
    inputClick: function() {
      document.getElementById("upload-btn").click();
    },
    uploadImageFile(e) {
      const files = e.target.files;
      this.createImage(files[0]);
      this.postParam(files[0]);
      this.img_name = files[0].name;
      this.$emit('changeScreen');
    },
    createImage(file) {
      const reader = new FileReader();
      reader.onload = e => {
        this.uploadedImage = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    postParam(file) {
      const params = new FormData();
      params.append("file-submit", file);

      axios.post(
        'http://localhost:5000/post',
        params,
        {
          headers: {
            'content-type': 'multipart/form-data',
          },
        }
      ).then(result => {
        console.log(result.data.img_url);
      }).catch(error => {
        console.log("uploading failure");
      });

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
