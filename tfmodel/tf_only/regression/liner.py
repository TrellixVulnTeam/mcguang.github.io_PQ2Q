import tensorflow as tf
# prepare the data
X = [3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1]
Y = [1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3]
test_x = [3.2, 3.3, 3.4] 
# bulid the liner model

#input_data = tf.constant(X)
input_data = tf.placeholder(tf.float32 ,shape = (None))
a = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))

Y_ = a * input_data + b

# mean loss and gradient descent
loss = tf.reduce_mean(tf.square(Y_ - Y))
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# init all variables

init = tf.initialize_all_variables()

# run graph

sess = tf.Session()
sess.run(init)

# train

for step in xrange(0, 2001):
	_, a_, b_, loss_ = sess.run([train,a,b,loss],feed_dict = {input_data : X})
	if step % 100 == 0:
		print step, a_, b_, loss_

print sess.run([Y_],feed_dict = {input_data : test_x})

