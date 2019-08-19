import re
from statistics import mean
import sys
import csv
import codecs
import MeCab
from sys import argv
#import better_exceptions
import glob
import logging
import os
import pickle
from gensim.models.word2vec import Word2Vec
#from tqdm import tqdm


## ファイル読み込み関数
def read_file_into_lines(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.readlines()


## 体言ファイル読み込み関数
def read_dict_of_declinable_words(wago_file):
    wago_string = read_file_into_lines(wago_file)

    for l in wago_string:
        line_list = l.split("\t")
        polar_words_list = line_list[1].split(" ")[0].strip()

        if line_list[0].split("（")[0] == "ネガ":
            polar_dict[polar_words_list] = -1
        elif line_list[0].split("（")[0] == "ポジ":
            polar_dict[polar_words_list] = 1
        else:
            polar_dict[polar_words_list] = 0


## 用言ファイル読み込み関数
def read_dict_of_substantive_words(trim_file):
    trim_string = read_file_into_lines(trim_file)

    for l in trim_string:
        line_list = l.split("\t")
        if line_list[1] == "p":
            polar_dict[line_list[0]] = 1
        elif line_list[1] == "n":
            polar_dict[line_list[0]] = -1
        else:
            polar_dict[line_list[0]] = 0


## 分かち書き
def create_mecab_list(text):
    mecab_list = []
    mecab = MeCab.Tagger("-Owakati")
    # mecab = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    mecab.parse("")
    pos_name_list = ["形容詞", "動詞", "形容動詞", "助動詞"]
    # encoding = text.encode('utf-8')
    node = mecab.parseToNode(text)
    while node:
        feature = node.feature.split(",")
        ## [品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音]
        ## 忙しく  形容詞,自立,*,*,形容詞・イ段,連用テ接続,忙しい,イソガシク,イソガシク
        if feature[0] in pos_name_list:
            mecab_list.append({feature[6]:feature[0]})
        else:
            mecab_list.append({node.surface:feature[0]})
        node = node.next
    return mecab_list


## ネガポジ判別（ネガティブをpolar_negative_wordsリストに格納）
def polar_negative_score(mecab_list, polar_dict):
    morphemes_list = [k for mecab_dict in mecab_list for k, v in mecab_dict.items()]

    polar_score_list = []
    polar_score_words = []
    polar_negative_words = []

    for mecab_dict in morphemes_list:
        if mecab_dict in polar_words_list:
            polar_score_words.append(mecab_dict) ## 入力テキストのうち辞書にある単語を格納
            polar_score_list.append(polar_dict[mecab_dict]) ## 上記の単語のスコアを格納

            if polar_dict[mecab_dict] == -1:
                polar_negative_words.append(mecab_dict) ## ネガティブを格納

    if len(polar_score_list) == 0:
        score = 0
        print("no polar words.")
    else:
        score = mean(polar_score_list)
    return polar_negative_words# polar_score_words, polar_score_list, [score]


## ポジティブ判別（ポジティブをpolar_positive_wordsリストに格納）
def polar_positive_store(similar_words_list, polar_dict):

    polar_positive_words = []

    for similar_word in similar_words_list:
        if similar_word in polar_words_list:
            if polar_dict[similar_word] == 1:
                polar_positive_words.append(similar_word) ## ポシティブを格納

    return polar_positive_words


## 類義語の単語辞書の定義，及び参照ディレクトリ明記
word2sid = {"<unk>": "0"}
files = glob.glob("contents/wiki*")

## Word2vecクラス定義
class Wiki2Vec:
    def __init__(self, dic_path, model_path):
        with open(dic_path, mode="rb") as f:
            self.word2sid = pickle.load(f)
        self.sid2word = {v:k for k, v in self.word2sid.items()}
        self.model = Word2Vec.load(model_path)

    def get_vector(self, token):
        ## 単語のベクトルを見る
        sid = self.word2sid[token]
        word_vector = self.model.wv[sid]
        print('-- {} --'.format(token))
        print(word_vector)

    def get_similar_tokens(self, token, topn=10):
        ## 与えられる単語と似ている単語を見る
        ## tokenは与えられる文字
        ## topnは類似単語の個数
        similar_words_list = []
        similarity_list = []
        sid = self.word2sid[token]
        similar_tokens = self.model.wv.most_similar(positive=[sid], topn=topn)
        # print('-- {} --'.format(token))
        for sid, similarity in similar_tokens:
            # tokenを類似語に更新
            token = self.sid2word[sid]
            similar_words_list.append(token)
            similarity_list.append(similarity)
            # print("{}: {:.2f}".format(token, similarity))

        # print(similar_words_list)
        # print(similarity_list)

        return similar_words_list, similarity_list


## ネガポジ判別辞書
polar_dict = {}
## 体言・用言読み込み
read_dict_of_declinable_words("./read_file/wago.121808.pn")
read_dict_of_substantive_words("./read_file/pn.csv.m3.120408.trim")

### Tune up the polar dictionary.
del polar_dict[""]
del polar_dict["だ"]
polar_dict["ある"] = 1
polar_dict["ない"] = -1
polar_dict["www"] = -1
### End of tune-up.

## 辞書内に定義されている単語のリスト
polar_words_list = [d for d in polar_dict]

## パラメータ設定
"""
size = 200
min_count = 20
window = 10
sg = 1
dirname = "size{}-min_count{}-window{}-sg{}".format(size, min_count, window, sg)
dic_path = "read_file/dictionary.pickle"
model_path = "learned_model/"+dirname+"/wikipedia.model"
"""

def recommend_words(text, wiki2vec):
    posi_list = []
    ans_list = []
    morphemes_dict_list = create_mecab_list(text)
    negative_words_list = polar_negative_score(morphemes_dict_list, polar_dict)
    #wiki2vec = Wiki2Vec(dic_path, model_path)

    for negative_word in negative_words_list:
        similar_words_list, similarity_list = wiki2vec.get_similar_tokens(negative_word, 50)
        positive_words_list = polar_positive_store(similar_words_list, polar_dict)

        if len(positive_words_list) == 0:
            positive_words_list.append("※使用注意")

        posi_list.append(positive_words_list[0])

        #print('-- {} --'.format(negative_word))
        #print(similar_words_list)
        #print(positive_words_list)

    #result = zip(negative_words_list, posi_list)
    for ng, po in zip(negative_words_list, posi_list):
        ans_list.append((ng, po))

    return ans_list

    #for val in result:
        #print(val)

    #return result


#with open("input.txt","r", encoding="utf-8") as f:
    #text = f.read()

#recommend_words(text)
