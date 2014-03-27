#!/usr/bin/python

import sys
import os

print 'Enter results filename : ',
results = open(raw_input(), 'r+').readlines()
print 'Enter test-label filename : ',
test_labels = open(raw_input(), 'r+').readlines()

#print results
#print test_labels

accuracy = 0.0
labels = {}
#confusion_matrix = [[] for i in range(len(results))

for result in results:
  [test_img, label] = result.split()
  labels[test_img] = label

for test_label in test_labels:
  [test_img, label] = test_label.split()
  if float(labels[test_img]) == float(label):
    accuracy += 1.0

print 'Accuracy : ', (accuracy/len(results))*100, '%'

