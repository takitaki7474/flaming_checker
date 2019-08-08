<template>

  <v-container fluid fill-height justify-center style="height: 500px;">
    <v-layout wrap class="align-center justify-center row">
      <p class="home-text">炎上度をチェックします.<br>画像またはテキストをアップロードしてください.</p>
    </v-layout>
  </v-container>

</template>

<script>

export default {
  name: 'Home',
  data: () => ({
    //
  }),
};
</script>

<style>
.home-text {
  font-size: 20px;
  color: #808080;
  text-align: center;
}
</style>
