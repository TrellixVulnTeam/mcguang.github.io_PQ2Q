"""Performs face alignment and calculates L2 distance between the embeddings of two images."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from scipy import misc
import tensorflow as tf
import numpy as np
import os
import sys
import argparse
import facenet
import align_dlib
import pdb
def main(args):
    align = align_dlib.AlignDlib(os.path.expanduser(args.dlib_face_predictor))
    #image_paths = [args.image1, args.image2]
    landmarkIndices = align_dlib.AlignDlib.OUTER_EYES_AND_NOSE
    images_list = get_image_paths(args.image_folder)



    with tf.Graph().as_default():

        with tf.Session() as sess:
      
            # Load the model
            print('Loading model "%s"' % args.model_file)
            facenet.load_model(args.model_file)
 
            while True:   
              # Get input and output tensors
              #image_paths = [args.image1, args.image2]
              #image_paths = [images_list[0],images_list[1],images_list[2]]
              image_paths = images_list
              pdb.set_trace()
              images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
              phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
              embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
              #image_size = int(images_placeholder.get_shape()[1])
              image_size = 96           
             
              # Run forward pass to calculate embeddings
              images = load_and_align_data(image_paths, image_size, align, landmarkIndices)
              feed_dict = { images_placeholder: images, phase_train_placeholder: False }
              emb = sess.run(embeddings, feed_dict=feed_dict)
              #dist = np.sqrt(np.sum(np.square(np.subtract(emb[0,:], emb[1,:]))))
              n = len(image_paths)
              dist = np.zeros([n,n])
              for i in range(n):
                 for j in range(n):
                   dist[i,j] = np.dot(emb[i,:],emb[j,:])
              print('Cosine distance between the embeddings: ')
              print(dist)
            
def load_and_align_data(image_paths, image_size, align, landmarkIndices):
    nrof_samples = len(image_paths)
    img_list = [None] * nrof_samples
    for i in xrange(nrof_samples):
        img = misc.imread(image_paths[i])
        print(image_paths[i])
        aligned = align.align(image_size, img, landmarkIndices=landmarkIndices, skipMulti=True)
        prewhitened = facenet.prewhiten(aligned)
        img_list[i] = prewhitened
    images = np.stack(img_list)
    return images

def get_image_paths(paths):
    dataset = []
    for path in paths.split(':'):
        path_exp = os.path.expanduser(path)
        classes = os.listdir(path_exp)
        classes.sort()
        nrof_classes = len(classes)
        for i in range(nrof_classes):
            class_name = classes[i]
            facedir = os.path.join(path_exp, class_name)
            dataset.append(facedir)
            #if os.path.isdir(facedir):
                #images = os.listdir(facedir)
                #image_paths = [os.path.join(facedir,img) for img in images]
                #dataset.append(ImageClass(class_name, image_paths))
  
    return dataset


def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--model_file', type=str, 
        help='File containing the model parameters as well as the model metagraph (with extension ".meta")',
        default='/mcg/home/mcg/machine-learning/origin/facenet/facenet/data/20160514-234418/model.ckpt-500000')
    parser.add_argument('--image_folder', type=str, help='the folder of images to calculate the cosine distance each other.')
    #parser.add_argument('--image1', type=str, help='First image to compare.')
    #parser.add_argument('--image2', type=str, help='Second image to compare.')
    parser.add_argument('--dlib_face_predictor', type=str,
        help='File containing the dlib face predictor.', default='/mcg/home/mcg/machine-learning/origin/facenet/facenet/data/shape_predictor_68_face_landmarks.dat')
    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
