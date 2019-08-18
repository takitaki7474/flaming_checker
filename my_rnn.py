import chainer
import chainer.links as L
import chainer.functions as F

class LSTM_SentenceClassifier(chainer.Chain):
    def __init__(self, vocab_size, embed_size, hidden_size, out_size):
        # クラスの初期化
        # :param vocab_size: 単語数
        # :param embed_size: 埋め込みベクトルサイズ
        # :param hidden_size: 隠れ層サイズ
        # :param out_size: 出力層サイズ
        super(LSTM_SentenceClassifier, self).__init__(
            # encode用のLink関数
            xe = L.EmbedID(vocab_size, embed_size, ignore_label=-1),
            eh = L.LSTM(embed_size, hidden_size),
            hh = L.Linear(hidden_size, hidden_size),
            # classifierのLink関数
            hy = L.Linear(hidden_size, out_size)
        )

    def __call__(self, x):
        # 順伝播の計算を行う関数
        # :param x:　入力値
        # エンコード
        x = F.transpose_sequence(x)
        self.eh.reset_state()
        for word in x:
            e = self.xe(word)
            h = self.eh(e)
        # 分類
        y = self.hy(h)
        return y
