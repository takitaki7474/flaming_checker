<template>

<v-container fluid fill-height justify-center>
  <v-layout wrap class="align-center justify-center row">
    <v-flex xs12 sm10 md8 lg6 xl4>
      <v-textarea color="teal">
         <template v-slot:label>
           <div>
             Bio <small>(optional)</small>
           </div>
         </template>
       </v-textarea>
    </v-flex>
  </v-layout>
</v-container>

</template>

<script>
export default {
  name: 'inputTextScreen',
  data: () => ({

  }),
};
</script>

<style>

</style>
