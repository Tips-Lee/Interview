# ! usr/bin/python
# File Name : tf_build.py
__author__ = 'Tips'

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


class DeepFM(Model):
    def __init__(self, ):
        super(DeepFM, self).__init__()
        self.flatten = layers.Flatten()
        self.fc1 = Dense(10, activation=None, kernel_initializer=GlorotNormal(), bias_initializer=Zeros(),
                         kernel_regularizer=l2(0.01))

    def build(self, input_shape):
        self.w = self.add_weight(name="w", shape=(input_shape[-1] * input_shape[-2], 64),
                                 initializer=GlorotNormal(seed=0),
                                 trainable=True)
        self.b = self.add_weight(name='b', shape=(64,), initializer=Zeros(), trainable=True)

    def call(self, inputs, training=False):
        x = self.flatten(inputs)
        x = tf.matmul(x, self.w) + self.b
        logits = self.fc1(x)
        return logits


model = DeepFM()
model.compile(optimizer=SGD(learning_rate=0.001, momentum=0),
              loss=SparseCategoricalCrossentropy(from_logits=True),
              metrics=['acc'], )

ckpt_callback = ModelCheckpoint(filepath="./ckpt/tf_build/model.ckpt-{epoch:02d}",
                                monitor='val_acc',
                                save_best_only=True,
                                save_weights_only=True,
                                initial_value_threshold=0.35,
                                save_freq='epoch',
                                verbose=1)

tb_callback = TensorBoard(log_dir="./logs/tf_build",
                          histogram_freq=0,
                          write_steps_per_second=False,
                          update_freq=10)

es_callback = EarlyStopping(monitor="val_acc",
                            patience=5,
                            verbose=1,
                            restore_best_weights=True,
                            mode='max',
                            start_from_epoch=10
                            )
reduce_lr = ReduceLROnPlateau(monitor="val_acc",
                              factor=0.1,
                              patience=3,
                              verbose=0,
                              mode='max',
                              min_delta=0.0001,
                              cooldown=2,
                              min_lr=1e-6)
callbacks = [ckpt_callback, tb_callback, es_callback, reduce_lr]

ckpt_dir = "./ckpt/tf_build"
ckpt = tf.train.get_checkpoint_state(ckpt_dir)
if ckpt and ckpt.model_checkpoint_path:
    model.load_weights(ckpt.model_checkpoint_path)
    logging.info("Restored weights from {}".format(ckpt.model_checkpoint_path))
else:
    logging.info("training from scratch")

# model = load_model(model_dir, compile=True)
history = model.fit(x=train_ds,
                    epochs=20,
                    verbose=1,
                    validation_data=test_ds,
                    steps_per_epoch=None,
                    validation_steps=10,
                    validation_freq=1,
                    callbacks=callbacks)

# result = model.evaluate(x=test_ds,
#                         verbose=1,
#                         return_dict=True,
#                         steps=10
#                         )
# print(result)
#
# pred = model.predict(x=test_ds, steps=1)
# print(pred[0])


# print(model.summary())
# print(model == history.model)
#
model.save(model_dir, overwrite=True, save_format=None)
tf.saved_model.save(model, export_dir="./models/tf_build1")
