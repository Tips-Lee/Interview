import tensorflow as tf
import numpy as np
import tensorflow.keras.layers as layers
from tensorflow.keras.initializers import RandomNormal
from tensorflow.keras.preprocessing import image, text, sequence
from tensorflow.keras import Model, Input
from read_data import get_mnist_ds
from tensorflow.keras.initializers import lecun_normal
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MSE
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

inputs = {}
outputs ={}
inputs["img"] = Input(shape=(28, 28), name="img")
x = layers.Flatten()(inputs["img"])
x = layers.Dense(64, activation="relu")(x)
outputs["label"] = layers.Dense(10, activation=None, kernel_initializer="lecun_normal")(x)
model = Model(inputs=inputs, outputs=outputs)

model.compile(optimizer=Adam(learning_rate=0.001,),
              loss="sparse_categorical_crossentropy",
              metrics="acc",)

train_ds, valid_ds = get_mnist_ds(batch_size=4)

model.fit(x=train_ds,
          epochs=30,
          validation_data=valid_ds,
          validation_steps=10,
          validation_freq=1)

