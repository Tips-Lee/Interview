# ! usr/bin/python
# File Name : demo_cross_entropy.py
__author__ = 'Tips'

import jiagu
import tensorflow as tf


def build_graph():
    g = tf.Graph()
    with g.as_default():
        w = tf.get_variable('w', [3,], initializer=tf.random_uniform_initializer())
        c = tf.constant(1.0, tf.float32, None, 'c')
        y = tf.multiply(w, c, name='y')
        tf.summary.histogram('c', c)
    print(w, c, y)
    return g


def train(graph):
    with tf.Session(graph=graph) as sess:
        fw = tf.summary.FileWriter(logdir='./logs', session=sess)
        summary = tf.summary.merge_all()
        sess.run(tf.global_variables_initializer())
        w = tf.get_default_graph().get_tensor_by_name('w:0')
        c = tf.get_default_graph().get_tensor_by_name('c:0')
        y = tf.get_default_graph().get_tensor_by_name('y:0')
        for i in range(20):
            summary_, w_, c_, y_ = sess.run([summary, w, c, y])
            fw.add_summary(summary_, global_step=i)
        print(w_, c_, y_, summary_)
        fw.close()


if __name__ == '__main__':
    g = build_graph()
    train(g)