<template>
<!--
  <v-container fluid fill-height justify-center style="height: 500px;">
    <v-layout wrap class="align-center justify-center row">
      <v-flex xs12 sm10 class="check-screen-container">


        <v-container fluid fill-height>
          <v-layout wrap>
            <v-flex xs12 sm10 class="img-bar-container">


              <v-container fluid fill-height>
                <v-layout wrap>
                  <v-flex xs12 sm8 class="img-container">
                    <img v-show="imgUrl" v-bind:src="imgUrl" class="display-img"/>
                  </v-flex>
                </v-layout>
              </v-container>


              <v-container fluid fill-height>
                <v-layout wrap>
                  <v-flex xs12 sm2 class="bar-container">
                    <p>bar</p>
                  </v-flex>
                </v-layout>
              </v-container>


            </v-flex>
          <v-flex xs12 sm10 class="mark-text-container">
            <v-layout wrap>
              <v-flex xs2 sm2 class="mark-container">
                <p>mark</p>
              </v-flex>
            </v-layout>
            <v-layout wrap>
              <v-flex xs8 sm8 class="text-container">
                <p>text</p>
              </v-flex>
            </v-layout>


          </v-flex>
        </v-layout>
      </v-container>


      </v-flex>
    </v-layout>
  </v-container>
-->
<v-container fluid fill-height justify-center style="height: 500px;">
  <v-layout wrap class="align-center justify-center row">
    <v-flex xs12 sm10>


      <v-container fluid fill-height class="check-screen-container">
        <v-layout wrap>


          <v-flex xs12>
            <v-container fluid fill-height class="img-bar-container">
              <v-layout wrap>


                <v-flex xs12 sm8>
                  <v-container fluid fill-height class="img-container">
                    <img v-show="imgUrl" v-bind:src="imgUrl" class="display-img"/>
                  </v-container>
                </v-flex>


                <v-flex xs12 sm2>
                  <v-container fluid fill-height class="bar-container">
                    <p>bar</p>
                  </v-container>
                </v-flex>


              </v-layout>
            </v-container>
          </v-flex>


          <v-flex xs12>
            <v-container fluid fill-height class="mark-text-container">
              <v-layout wrap>


                <v-flex xs2>
                  <v-container fluid fill-height class="mark-container">
                    <p>mark</p>
                  </v-container>
                </v-flex>


                <v-flex xs8>
                  <v-container fluid fill-height class="text-container">
                    <p>text</p>
                  </v-container>
                </v-flex>


              </v-layout>
            </v-container>
          </v-flex>
          

        </v-layout>
      </v-container>


    </v-flex>
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
  width: 100%;
  height: 100%;
}
/*
.check-screen-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.img-bar-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.mark-text-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
*/
</style>
