import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.optimizers import Adam
import  scipy
opt = Adam(learning_rate=1)

with tf.GradientTape() as tape:
    # x = tf.Variable(tf.constant(4), trainable=True, name='x')
    x = tf.Variable(4,trainable=True    )
    y = tf.pow(x, 2)

print(isinstance(x, tf.Variable))
print(isinstance(y, tf.Variable))

# x_grad = tape.gradient(y, [x])
grads_and_vars = opt.compute_gradients(y, [x], tape)
# opt.apply_gradients(grads_and_vars)
print(x, y)
print(grads_and_vars)

print(scipy.stats.sqrt(4))