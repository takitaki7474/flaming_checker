<template>

  <v-container fluid fill-height justify-center style="height: 500px;">
    <v-layout wrap class="align-center justify-center row">
      <img v-bind:src="imgUrl"/>
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
