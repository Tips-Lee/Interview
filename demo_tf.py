import tensorflow as tf
import numpy as np
from tensorflow.keras.initializers import RandomNormal
from tensorflow.keras.preprocessing import image, text, sequence
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

rdm = RandomNormal(mean=0, stddev=1)

a = rdm((2,3))
tf.clip_by_global_norm()
print(a.numpy())