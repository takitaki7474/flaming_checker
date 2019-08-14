import chainer
import chainer.links as L
import chainer.functions as F

class MyNet_6(chainer.Chain):

    def __init__(self, n_out):
        super(MyNet_6, self).__init__()
        with self.init_scope():
            self.conv1 = L.Convolution2D(None, 32, 3, 3, 1)
            self.conv2 = L.Convolution2D(32, 32, 3, 3, 1)
            self.conv3 = L.Convolution2D(32, 32, 3, 3, 1)
            self.conv4 = L.Convolution2D(32, 32, 3, 3, 1)
            self.conv5 = L.Convolution2D(32, 32, 3, 3, 1)
            self.conv6 = L.Convolution2D(32, 32, 3, 3, 1)
            self.fc4 = L.Linear(None, 512)
            self.fc5 = L.Linear(512, n_out)

    def __call__(self, x):
        h = F.relu(self.conv1(x))
        h = F.max_pooling_2d(F.relu(self.conv2(h)), 2)
        h = F.relu(self.conv3(h))
        h = F.max_pooling_2d(F.relu(self.conv4(h)), 2)
        h = F.relu(self.conv5(h))
        h = F.max_pooling_2d(F.relu(self.conv6(h)), 2)
        h = F.dropout(F.relu(self.fc4(h)))
        h = self.fc5(h)
        return h
