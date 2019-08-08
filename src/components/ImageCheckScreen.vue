<template>

  <v-container fluid fill-height justify-center style="height: 500px;">
    <v-layout wrap class="align-center justify-center row">
      <img v-show="imgUrl" v-bind:src="imgUrl" class="display-img"/>
    </v-layout>
  </v-container>

</template>

<script>

export default {
  name: 'ImageCheckScreen',
  props: {
    imgUrl: String,
  },
  data: () => ({

  }),
};
</script>

<style>
.display-img {
  width: 300px;
  height: 300px;
}
</style>
