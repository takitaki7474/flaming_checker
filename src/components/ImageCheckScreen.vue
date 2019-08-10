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
                    <img v-show="imgUrl" v-bind:src="imgUrl" v-on:load="drawChart" class="display-img"/>
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
    randomNum: Number,
  },
  data: () => ({
    flamingBar: "",
  }),
  mounted() {
    var ctx = document.getElementById("flaming-bar");
    this.flamingBar = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['炎上度'],
        datasets: [
          {
            data: [this.randomNum],
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
  },
  methods: {
    drawChart: function() {
      console.log(this.randomNum);
      console.log(this.flamingBar.dataset);
      this.flamingBar.data.datasets[0].data[0] = this.randomNum
      console.log(this.flamingBar.data.datasets[0].data);
      this.flamingBar.update();
    }
  }
};
</script>

<style>
.display-img {
  width: 40vmin;
  height: 40vmin;
  border: 1px solid;
}

</style>
