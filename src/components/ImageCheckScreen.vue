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
                    <v-card raised>
                      <img v-show="imgUrl" v-bind:src="imgUrl" v-on:load="drawChart" class="display-img"/>
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
                    <v-card raised class="comment-card">
                      <p v-if="displayComment" v-model="flamingValue" v-bind="comment" style="text-align: center; margin: 0; font-size: 20px;">炎上度は<span style="color: red;">{{flamingValue}}%</span>です!<br>{{comment}}</p>
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
  name: 'ImageCheckScreen',
  props: {
    imgUrl: String,
    flamingValue: Number,
  },
  data: () => ({
    flamingBar: "",
    flamingHrizontalBar: "",
    fireSize: 0,
    displayComment: false,
    comment: ""
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
      const commentList = [
        "投稿者は多大なダメージを受けます。投稿を控えましょう。",
        "間違いなく燃え上がります。消化の準備を始めてください。",
        "投稿すれば、袋叩きに遭います。落ち着いて考えましょう。",
        "炎上の危険があります! お茶でも飲んで、一度考えましょう。",
        "火の粉を被るかもしれません! モザイク加工を施しましょう。",
        "危険な香りがします! 投稿には気をつけてください!",
        "問題なく投稿できます! 自信を持って伝えましょう!",
        "火の元はありません! 安心して投稿できます。",
        "あなたは炎上回避マスターです! どんどん投稿しましょう!"
      ]
      if (this.flamingValue > 66.0) {
        var min = 0 ;
        var max = 2 ;
        var commentValue = Math.floor( Math.random() * (max + 1 - min) ) + min ;
        this.comment = commentList[commentValue];
      } else if (this.flamingValue > 33.0) {
        var min = 3 ;
        var max = 5 ;
        var commentValue = Math.floor( Math.random() * (max + 1 - min) ) + min ;
        this.comment = commentList[commentValue];
      } else {
        var min = 6 ;
        var max = 8 ;
        var commentValue = Math.floor( Math.random() * (max + 1 - min) ) + min ;
        this.comment = commentList[commentValue];
      }

      this.displayComment = true;
    }
  }
};
</script>

<style>

</style>
