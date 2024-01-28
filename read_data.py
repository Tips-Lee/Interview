import tensorflow as tf
from tensorflow.keras.datasets import mnist


def get_mnist_ds(batch_size=1000):
    global train_ds, test_ds
    (x_train, y_train), (x_test, y_test) = mnist.load_data(path=r"C:\Users\Tips\Desktop\aigc\Interview/data/mnist.npz")
    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).map(
        lambda x, y: ({"img": tf.cast(x, tf.float32) / 255.0 - 0.5}, {"label": tf.cast(y, tf.int32)}))
    test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).map(
        lambda x, y: ({"img": tf.cast(x, tf.float32) / 255.0 - 0.5}, {"label": tf.cast(y, tf.int32)}))
    train_ds = train_ds.shuffle(1024).batch(batch_size).prefetch(32)
    test_ds = test_ds.shuffle(1024).batch(batch_size).prefetch(32)

    return train_ds, test_ds