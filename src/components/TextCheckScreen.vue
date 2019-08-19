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
                      <v-card color="orange lighten-5" style="min-width:100%; min-height: 80%; display: flex; align-items: center;">
                        <v-row justify="center" style="padding: 20px;">
                          <div class="headline mb-2" v-on:load="drawChart">{{message}}</div>
                        </v-row>
                      </v-card>
                    </v-container>
                  </v-flex>


                  <v-flex xs12 sm4 class="container-el">
                    <v-container fluid fill-height class="bar-container">
                      <canvas id="flaming-bar" width="400" height="1000"></canvas>
                      <canvas id="flaming-horizontal-bar" width="1000" height="40"></canvas>
                    </v-container>
                  </v-flex>


                </v-layout>
              </v-container>
            </v-flex>


            <v-flex xs12 class="container-el">
              <v-container fluid fill-height class="mark-text-container">
                <v-layout wrap class="mark-text-layout">


                  <v-flex xs2 class="mark-flex container-el">
                    <v-container fluid fill-height justify-center align-center class="mark-container">
                      <v-icon :size="fireSize" color="orange darken-2">whatshot</v-icon>
                    </v-container>
                  </v-flex>


                  <v-flex xs10 class="container-el">
                    <v-container fluid fill-height justify-center align-center class="text-container">
                      <v-card class="comment-card">
                        <v-card-text v-if="displayComment">
                          <p v-model="flamingValue" style="text-align: center; margin: 0; font-size: 20px;">炎上度は<span style="color: red;">{{flamingValue}}%</span>です!</p><br>
                          <v-chip-group column>
                            <v-chip v-if="comment.length > 0" label color="grey lighten-4" v-for="item in comment" :key="index" style="height: 50px;">
                              <v-chip color="pink lighten-4" style="margin: 0 5px;">{{item[0]}}</v-chip>
                              <v-chip color="blue lighten-4" style="margin: 0 5px;">{{item[1]}}</v-chip>
                            </v-chip>
                            <v-chip column v-if="comment.length==0">
                              炎上しそうな単語は存在しません
                            </v-chip>
                          </v-chip-group>
                        </v-card-text>
                      </v-card>
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
  name: 'TextCheckScreen',
  props: {
    flamingValue: Number,
    message: String,
    comment: Object,
  },
  data: () => ({
    flamingBar: "",
    flamingHrizontalBar: "",
    fireSize: 0,
    displayComment: false,
  }),
  mounted() {
    var me = this;
    var ctx = document.getElementById("flaming-bar");
    this.flamingBar = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['炎上度'],
        datasets: [
          {
            data: [this.flamingValue],
            backgroundColor: "rgba(219,39,91,0.5)",
          }
        ]
      },
      options: {
        animation: {
          easing: 'easeInOutQuart',
          duration: 2000,
          onComplete: function(animation) {
            me.drawFire(me.drawComment);
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

    var ctx2 = document.getElementById("flaming-horizontal-bar");
    this.flamingHorizontalBar = new Chart(ctx2, {
      type: 'horizontalBar',
      data: {
        labels: ['炎上度'],
        datasets: [
          {
            data: [this.flamingValue],
            backgroundColor: "rgba(219,39,91,0.5)",
          }
        ]
      },
      options: {
        animation: {
          easing: 'easeInOutQuart',
          duration: 2000,
          onComplete: function(animation) {
            me.drawFire(me.drawComment);
          }
        },
        legend: {
          display: false
        },
        scales: {
          xAxes: [{
             display: false,
             ticks: {
               suggestedMax: 100,
               suggestedMin: 0,
               stepSize: 10,
               fontSize: 10,
             }
           }],
           yAxes: [{
             display: false,
             ticks: {
               fontSize: 10
             }
           }]
        }
      }
    });
  },
  methods: {
    drawChart: function() {
      this.displayComment = false;
      this.fireSize = 0;
      this.flamingBar.data.datasets[0].data[0] = this.flamingValue
      this.flamingBar.update();
      this.flamingHorizontalBar.data.datasets[0].data[0] = this.flamingValue
      this.flamingHorizontalBar.update();
    },
    drawFire: function(callback) {
      var fire_size;
      if (this.flamingValue < 40) {
        fire_size = 40;
      } else {
        fire_size = this.flamingValue;
      }
      this.fireSize = fire_size;
      callback();
    },
    drawComment: function() {
      this.displayComment = true;
    }
  }
};
</script>

<style>

</style>
