# 火の用心 (Flaming Checker)
## Overview
Flaming Checker is an app that quantify whether an image or text is likely to burn by deep learning.

## Description
You can upload one image or text. If you upload an image, Flaming Checker quantify whether the image is a flaming content. 
And display the degree of flame and advice on what the user should do. 
On the other hand, if you upload text, Flaming Checker quantify whether the text is a flaming content.
And also display the degree of flame. In addition, Flaming Checker detects words that are likely to burn and recommends words that are unlikely to burn. And flaming words are displayed in red and recommended words are displayed in blue.
  
Deep learning model was implemented using Chainer.
And we created three deep learning models for image analysis, text analysis and word recommendation.
We applied CNN for image analysis, LSTM for text analysis and Word2Vec for word recommendation.
The CNN and LSTM models trained more than 5,000 data each.
The back end is implemented using Flask and Chainer, and the front end is implemented using Vue.js.
  
In the word recommendation function, Flaming Checker performs emotion analysis of text.
It evaluates negative words as likely to burn by emotion analysis.
And recommends words that are similar in meaning and positive by Word2Vec and emotion analysis.

## Demo

![flamingCheckerDemo](https://github.com/takitaki7474/algorithm-research/blob/master/gifs_and_images/flaming_checker.gif)



