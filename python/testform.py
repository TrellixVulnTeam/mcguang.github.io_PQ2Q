from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from scipy import misc
import tensorflow as tf
import numpy as np
import sys
import argparse
import facenet
import align_dlib
from PIL import Image
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import os
import json

def loadArg():
	path1 = './shape_predictor_68_face_landmarks.dat'
	path2 = './20160514-234418/model.ckpt-500000'
	align = align_dlib.AlignDlib(os.path.expanduser(path1))
	landmarkIndices = align_dlib.AlignDlib.OUTER_EYES_AND_NOSE
	# Load the model
	print("load model")
	facenet.load_model(path2)
	return align,landmarkIndices
def a(image_paths,align,landmarkIndices ):
	image_size = 96
	images = load_and_align_data(image_paths, image_size, align, landmarkIndices)
	# Get input and output tensors
	images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
	phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
	embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
	#image_size = int(images_placeholder.get_shape()[1])
	feed_dict = { images_placeholder: images, phase_train_placeholder: False }
	emb = sess.run(embeddings, feed_dict=feed_dict)
	#dist = np.sqrt(np.mean(np.square(np.subtract(emb[0,:], emb[1,:]))))
	dist=np.dot(emb[0,:],emb[1,:])
	return dist

def load_and_align_data(image_paths, image_size, align, landmarkIndices):
    nrof_samples = len(image_paths)
    img_list = [None] * nrof_samples
    for i in xrange(nrof_samples):
        img = misc.imread(image_paths[i])
        aligned = align.align(image_size, img, landmarkIndices=landmarkIndices, skipMulti=True)
        prewhitened = facenet.prewhiten(aligned)
        img_list[i] = prewhitened
    images = np.stack(img_list)
    return images

def computerRS(align,landmarkIndices ):
	register_openers()
	ph = "imageset"
	imagenamelist = os.listdir(ph)
	res = {}
	f = open("log","w")
	for i in range(100):
		rs1 = os.path.join(ph,imagenamelist[i])
		for j in range(len(imagenamelist)):
			rs2 = os.path.join(ph,imagenamelist[j])		

			datagen, headers = multipart_encode({"image1": open(rs1, "rb"),"image2":open(rs2,"rb")})
			request = urllib2.Request("http://192.168.0.13:31415/compare", datagen, headers)
			image_paths=[]
			image_paths.append(rs1)
			image_paths.append(rs2)
			try:
				data = eval(urllib2.urlopen(request).read())
				res["image1"] = imagenamelist[i]
				res["image2"] = imagenamelist[j]
				res["score1"]  = data["score"]
				dt = a(image_paths,align,landmarkIndices )
				res["score2"] = str(dt*100)
				print (res)
				restostr=json.JSONEncoder().encode(res)
				f.write(restostr+"\n")
			except Exception as e:
				print("is error : %s,%s"%(imagenamelist[i],imagenamelist[j]),e)
				continue
if __name__ == '__main__':
	with tf.Graph().as_default(),tf.device("/cpu:0"):
		with tf.Session() as sess:
			align,landmarkIndices = loadArg()
			computerRS(align,landmarkIndices )
