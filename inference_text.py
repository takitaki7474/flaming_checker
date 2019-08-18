# -*- coding:utf-8 -*-

import numpy as np
import cv2
import chainer
import chainer.links as L
import chainer.functions as F
from chainer import iterators, training, optimizers, serializers
from chainer.datasets import tuple_dataset, split_dataset_random
from chainer.training import extensions
import MeCab
import my_rnn
import re
import pickle
import argparse



infer_net = my_rnn.LSTM_SentenceClassifier(13443,200,100,2)
infer_net = L.Classifier(infer_net)
serializers.load_npz("./learned_model/lstm1.model", infer_net)



def sentence2words(sentence):
    stopwords = ["i", "a", "an", "the", "and", "or", "if", "is", "are", "am", "it", "this", "that", "of", "from", "in", "on"]
    sentence_words = []
    for word in sentence:
        if (re.compile(r"^.*[0-9]+.*$").fullmatch(word) is not None): # 数字が含まれるものは除外
            continue
        if word in stopwords: # ストップワードに含まれるものは除外
            continue
        sentence_words.append(word)
    return sentence_words[:-1]



def preprocessing(dx):

    m = MeCab.Tagger("-Owakati")
        #print(dx)
    dx = re.sub(re.compile(r"[!-、。「」\/:-@[-`{-~・]"), "", dx) # 記号を削除
    dx = dx.replace(" ", "") # 改行削除
    dx = dx.replace("\n","")
    #dx_result.append(m.parse(dx))
    dx = m.parse(dx)
        #print(dx_result)
    dx = dx.split(" ")


    #print(dx_result)
    f=open('./learned_model/word-jisho.pickle','rb')#辞書の読み込み
    words=pickle.load(f)

    for word in dx:
        if word not in words:
            words[word] = words["は"]




    data_x_vec = []
    sentence_words = sentence2words(dx)

    sentence_ids = []
    for word in sentence_words:
        sentence_ids.append(words[word])
    data_x_vec.append(sentence_ids)

    # 文章の長さを揃えるため、-1パディングする（系列を覚えておきやすくするため、前パディングする）
    max_sentence_size = 53
    '''for sentence_vec in data_x_vec:
        if max_sentence_size < len(sentence_vec):
            max_sentence_size = len(sentence_vec)'''
    for sentence_ids in data_x_vec:
        while len(sentence_ids) < max_sentence_size:
            sentence_ids.insert(0, -1) # 先頭に追加

    # データセット
    data_x_vec = np.array(data_x_vec, dtype="int32")
    #for x, t in zip(data_x_vec, data_t):
        #dataset.append((x, t))
    #print(data_x_vec)


    return data_x_vec

#def infer(text):
def infer(text):
    pre_data = preprocessing(text)
    result = F.softmax(infer_net.predictor(pre_data), axis=1)
    result = result.data[0][1]
    result = round(result * 100, 2)
    return result
