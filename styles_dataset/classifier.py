#!/usr/bin/python

# Author : Sreenatha Bhatlapenumarthi
# Date : February 14, 2014
''' Trains SVM classifier for paintings using HOG features '''

# Imports
import cv2
import numpy as np
import sys
import os

# Global parameters
#bin_n = int(raw_input("Enter number of bins: ")) # Number of bins
# Accuracy vs bin-size
bin_n = int(raw_input()) # Number of bins
# Accuracy vs training-size
#bin_n = 64
svm_params = dict( kernel_type = cv2.SVM_LINEAR,
		                    svm_type = cv2.SVM_C_SVC,
				                        C=1 )
affine_flags = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR

test_directory = './test'
label_file = './train_label_file'
results_filename = './results'
results_file = open(results_filename, 'w+')

# Function definitions
def hog(img):
	gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
	gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
	mag, ang = cv2.cartToPolar(gx, gy)
	# quantizing binvalues in (0...16)
	bins = np.int32(bin_n*ang/(2*np.pi))
	# Divide to 4 sub-squares
	bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]
	mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
	hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
	hist = np.hstack(hists)
	return hist


# Extract HOG features and labels from training data
#print 'Enter training-label filename : ',
#label_file = raw_input()
train_directory, label_file_name = os.path.split(label_file)	
label_data = open(label_file,'r').readlines()
labels = []
train_images = []
for line in label_data:
  train_images.append(line.split()[0])
  labels.append(line.split()[1])
labels = np.float32(labels)
trainData = []
for image_name in train_images:
  image_loc = train_directory + '/' + image_name
  # Load the image in GREY_SCALE
  img = cv2.imread(image_loc,0)
  hog_img = hog(img)	
  trainData.append(list(hog_img))

# Train the SVM classifier on the extracted training data	
trainData = np.float32(trainData)
svm = cv2.SVM()
svm.train(trainData,labels, params=svm_params)
svm.save('svm_data.dat')

# Extract the test data
#print 'Enter test image directory : ',
#test_directory = raw_input()
testData = []
test_images = []
for image_name in os.listdir(test_directory):
  image_loc = test_directory + '/' + image_name
  test_images.append(image_name)	
  img = cv2.imread(image_loc,0)
  hog_img = hog(img)	
  testData.append(list(hog_img))

# Test the SVM classifer
testData = np.float32(testData)	
results = svm.predict_all(testData)
results = list(results)	
#print 'Results : '
for i in range(len(results)):
#  print "Image: "+ test_images[i] + " Class: ", results[i][0]
  results_file.write(test_directory + '/' +  test_images[i] + ' ' + str(results[i][0]) + '\n')

results_file.close()
