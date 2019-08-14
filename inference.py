# -*- coding:utf-8 -*-

import numpy as np
import cv2
import chainer
import chainer.links as L
import chainer.functions as F
from chainer import iterators, training, optimizers, serializers
from chainer.datasets import tuple_dataset, split_dataset_random
from chainer.training import extensions
import cnn_mynet


gpu_id = -1

infer_net = cnn_mynet.MyNet_6(2)
infer_net = L.Classifier(infer_net)
serializers.load_npz("./learned_model/" + "hayakawa_special.model", infer_net)

def preprocessing(img):
    img = cv2.resize(img,(28,28))
    img = img.astype(np.float32)
    img = img[None,...]
    return img

def infer(img_path):

    ans_list = []
    prob_list = []

    img = cv2.imread(img_path)
    img = preprocessing(img)
    y = infer_net.predictor(img)
    y = y.data
    print(F.softmax(y)[0].data)
    prob_list.append([round(i*100,2) for i in F.softmax(y)[0].data])

    return prob_list
