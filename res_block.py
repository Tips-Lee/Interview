import tensorflow as tf


def residual_block(input, k=3, filters=64):
    x = tf.layers.conv2d(input, filters, k, 1, padding='same', activation=None)
    x = tf.nn.batch_normalization(x)
    x = tf.nn.relu(x)

    x = tf.layers.conv2d(x, filters, k, 1, padding='same', activation=tf.nn.relu)
    output = x + input
    return output


class ResNet:
    def __init__(self, input, batch_size):
        x = residual_block(input, k=3, filters=32)
        x = residual_block(input, k=3, filters=64)
        x = residual_block(input, k=3, filters=128)
        self.logits = tf.reshape(x, [batch_size, -1])

    def compute_loss(self, labels):
        loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=self.logits, labels=labels)
        return loss


def train():
    g = tf.Graph()
    with g.as_default():

        x_train = tf.placeholder(dtype=tf.float32, shape=[None, H, W, 3], name='x_train')
        y_train = tf.placeholder(dtype=tf.int64, shape=[None], name='x_train')
        net = ResNet(x_train, batch_size)
        loss = net.compute_loss(y_train)

        # accuracy
        opt = tf.train.AdamOptimizer(learning_rate=lr)
        train_op = opt.minimize(loss)

    with tf.Session(graph=g) as sess:
        for epoch in range(epochs):
            for step in range(steps):
                feed = {x_train:None, y_train:None}
                loss_ ... = sess.run([loss,....], feed_dict=feed)

                print('loss: %f' % loss)





