# ! usr/bin/python
# File Name : tf_build.py
__author__ = 'Tips'
import tensorflow as tf
print(tf.__version__)
import tensorflow.keras.layers as layers
from tensorflow.keras import Model,Input,Sequential
from tensorflow.keras.models import save_model, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.initializers import GlorotNormal, Zeros, TruncatedNormal
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam, RMSprop, SGD
from tensorflow.keras.losses import CategoricalCrossentropy, SparseCategoricalCrossentropy, MeanSquaredError
from tensorflow.keras.activations import sigmoid
from tensorflow.keras.metrics import AUC


class DeepFM(Model):
    def __init__(self, ):
        super(DeepFM, self).__init__()
        self.flatten = layers.Flatten()
        self.fc1 = Dense(10, activation=None, kernel_initializer=GlorotNormal(), bias_initializer=Zeros(), kernel_regularizer=l2)

    def build(self, input_shape):
        self.w = self.add_weight(name="w", shape=(input_shape[-1], 64), initializer=GlorotNormal(seed=0), trainable=True)
        self.b = self.add_weight(name='b',shape=(64,), initializer=Zeros(),trainable=True)

    def call(self, inputs, training=False):
        x = self.flatten(inputs)
        x = tf.matmul(x,self.w) + self.b
        logits = self.fc1(x)
        return logits


model = DeepFM()

model.compile(optimizer=SGD(learning_rate=0.01, momentum=10),
              loss=SparseCategoricalCrossentropy(from_logits=True),
              metrics=AUC)



