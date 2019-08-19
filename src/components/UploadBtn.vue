<template>
  <v-flex xs12 class="upload-form">
    <v-btn v-on:click="inputClick" rounded small color="warning" class="select-btn">画像をアップロード</v-btn>
    <input class="form-button" type="file" name="file-submit" id="upload-btn" v-on:change="uploadImageFile"/>
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
      this.postParam(files[0], this.createImage);
      this.img_name = files[0].name;
      this.$emit('changeScreen');
    },
    createImage(file, ans) {
      const reader = new FileReader();
      reader.onload = e => {
        this.uploadedImage = e.target.result;
        this.$emit('changeURL',this.uploadedImage, ans);
      };
      reader.readAsDataURL(file);
    },
    postParam(file, callback) {
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
        callback(file, result.data.img_ans);
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
