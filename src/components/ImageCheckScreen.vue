<template>

<v-container fluid fill-height justify-center>
  <v-layout wrap class="align-center justify-center row">
    <v-flex xs12 sm10 md8 lg6 xl4>


      <v-container fluid fill-height class="check-screen-container">
        <v-layout wrap>


          <v-flex xs12 class="container-el">
            <v-container fluid fill-height class="img-bar-container">
              <v-layout wrap>


                <v-flex xs12 sm8 class="container-el">
                  <v-container fluid fill-height class="img-container">
                    <img v-show="imgUrl" v-bind:src="imgUrl" class="display-img"/>
                  </v-container>
                </v-flex>


                <v-flex xs12 sm4 class="container-el">
                  <v-container fluid fill-height class="bar-container">
                    <canvas id="flaming-bar" width="400" height="1000"></canvas>
                  </v-container>
                </v-flex>


              </v-layout>
            </v-container>
          </v-flex>


          <v-flex xs12 class="container-el">
            <v-container fluid fill-height class="mark-text-container">
              <v-layout wrap>


                <v-flex xs2 class="container-el">
                  <v-container fluid fill-height class="mark-container">
                    <p>mark</p>
                  </v-container>
                </v-flex>


                <v-flex xs8 class="container-el">
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
import Chart from 'chart.js';

export default {
  name: 'ImageCheckScreen',
  props: {
    imgUrl: String,
  },
  data: () => ({

  }),
  mounted: function() {
     var ctx = document.getElementById("flaming-bar");
     var flamingBar = new Chart(ctx, {
       type: 'bar',
       data: {
         labels: ['炎上度'],
         datasets: [
           {
             data: [60],
             backgroundColor: "rgba(219,39,91,0.5)",
           }
         ]
       },
       options: {
         animation: {
           easing: 'easeInOutQuart',
           duration: 3000,
           onComplete: function(animation) {
             console.log("stop")
           }

         },
         legend: {
           display: false
         },
         scales: {
           yAxes: [{
              ticks: {
                suggestedMax: 100,
                suggestedMin: 0,
                stepSize: 10,
                fontSize: 20,
              }
            }],
            xAxes: [{
              ticks: {
                fontSize: 20
              }
            }]
         }
       }
     });
  }
};
</script>

<style>
.display-img {
  width: 80%;
  height: 80%;
  border: 1px solid;
}

</style>
