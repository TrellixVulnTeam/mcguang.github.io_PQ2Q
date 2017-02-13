import tensorflow as tf


with tf.Session():
	c = tf.constant([[1.,2.,3.,4.],[-1.,-2.,-3.,-5.],[5.,6.,7.,8.]])
	print tf.sparse_segment_sum(c, tf.constant([0, 1]), tf.constant([0, 0])).eval()
