<template>
  <v-content>

    <v-container fluid fill-height justify-center style="height: 500px;">
      <v-layout wrap class="align-center justify-center row">
        <p class="home-text">炎上度をチェックします.<br>画像またはテキストをアップロードしてください.</p>
      </v-layout>
    </v-container>

    <v-container fluid fill-height justify-center style="height: 100px;">
      <v-layout wrap class="align-center justify-center row" style="height: 100px;">
        <UploadBtn></UploadBtn>
        <InputTextBtn></InputTextBtn>
      </v-layout>
    </v-container>

  </v-content>
</template>

<script>
import UploadBtn from './UploadBtn.vue';
import InputTextBtn from './InputTextBtn.vue';

export default {
  name: 'Home',
  components: {
    UploadBtn,
    InputTextBtn,
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
.home-text {
  font-size: 20px;
  color: #808080;
  text-align: center;
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
