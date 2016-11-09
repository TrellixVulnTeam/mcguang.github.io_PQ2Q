import re
import tflearn
import tensorflow as tf
import tflearn.datasets.mnist as mnist

from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression

#--------------------------------------------------------------------

class Model1(object):
	"""convnet MNIST"""
	def __init__(self):
		network = tflearn.input_data(shape = [None, 784], name = "input")
		network = self.make_core_network(network)
		network = regression(network, optimizer = 'adam', learning_rate = 0.01,
							loss = 'categorical_crossentropy', name = 'target')

		model = tflearn.DNN(network, tensorboard_verbose = 0)
		self.model = model

	@staticmethod
	def make_core_network(network):
		network = tflearn.reshape(network, [-1, 28, 28, 1], name = "reshape")
		network = conv_2d(network, 32, 3, activation = 'relu', regularizer = "L2")
		network = max_pool_2d(network, 2)
		network = local_response_normalization(network)

