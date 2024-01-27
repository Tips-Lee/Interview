# ! usr/bin/python
# File Name : tf_build.py
__author__ = 'Tips'

import numpy as np
import logging
import tensorflow as tf

print(tf.__version__)

import tensorflow.keras.layers as layers
from tensorflow.keras import Model, Input, Sequential
from tensorflow.keras.models import save_model, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.initializers import GlorotNormal, Zeros, TruncatedNormal
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam, RMSprop, SGD
from tensorflow.keras.losses import CategoricalCrossentropy, SparseCategoricalCrossentropy, MeanSquaredError
from tensorflow.keras.activations import sigmoid
from tensorflow.keras.metrics import AUC
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping, TensorBoard
from tensorflow.keras.datasets import mnist
from tensorflow.data import TFRecordDataset

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

model_dir = "./models/tf_build"

(x_train, y_train), (x_test, y_test) = mnist.load_data(path=r"C:\Users\Tips\Desktop\aigc\Interview/data/mnist.npz")
train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).map(
    lambda x, y: (tf.cast(x, tf.float32) / 255.0 - 0.5, tf.cast(y, tf.float32)))
test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).map(
    lambda x, y: (tf.cast(x, tf.float32) / 255.0 - 0.5, tf.cast(y, tf.float32)))

train_ds = train_ds.shuffle(1024).batch(1000).prefetch(32)
test_ds = test_ds.shuffle(1024).batch(1000).prefetch(32)

sample = x_test[:2].astype(np.float32) / 255.0 - 0.5
model = load_model(model_dir, compile=True)
# print(model)
# result = model.evaluate(x=test_ds,
#                         verbose=1,
#                         return_dict=True,
#                         steps=10
#                         )
# print(result)
#
# pred = model.predict(x=test_ds, steps=1)
# print(pred[0])
pred = model(tf.constant(sample))
print(pred)

# del model
# model = tf.saved_model.load("./models/tf_build1")
# print(model)

# f = model.signatures["serving_default"]
# result = f(input_1=sample)  # 模型预测
# print(result)
# # result = f(input_1=tf.constant(sample))  # 模型预测
# # print(result)
# #
# # result = f(input_1=sample.tolist())  # 模型预测
# # print(result)
# result = model(inputs=sample)  # 模型预测
# print(result)
# result = model(sample)  # 模型预测
# print(result)
# result = model(tf.constant(sample))  # 模型预测
# print(result)
