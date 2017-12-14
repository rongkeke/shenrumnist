# _*_ coding: utf-8 _*_
# !/usr/bin/env python
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('/home/rongtensorflow/MNIST_data/', one_hot= True)
sess = tf.InteractiveSession()
x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])