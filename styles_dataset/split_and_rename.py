#!/usr/bin/python

import os
import sys
import shutil
import random


target_dir = './source'
train_dir = './training'
test_dir = './test'
#train_count = int(raw_input("Enter train-set size: "))
#test_count = int(raw_input("Enter test-set size: "))
# Accuracy vs bin-size
train_count = 18
test_count = 2
# Accuracy vs train-set size
#train_count = int(open('train_size','r').read().strip())
#test_count = int(open('test_size','r').read().strip())
train_label_file = open('./train_label_file','w+')
test_label_file = open('./test_label_file','w+')
class_encoding_file = open('./class_encoding','r')


## Preprocessing
class_encoding = {}
for encoding in [tuple(i.split()) for i in class_encoding_file.readlines()][:-1]:
  class_encoding[encoding[1]] = encoding[0]


total_train_count = 1
total_test_count = 1
styles_dirs = os.listdir(target_dir)
for style_dir in styles_dirs:
  style_files = os.listdir(target_dir + '/' + style_dir)
  random.shuffle(style_files)
  for i in range(train_count):
    old_address = target_dir + '/' + style_dir + '/' + style_files[i]
    new_address = train_dir + '/image_' + str(total_train_count)
    shutil.copyfile(old_address, new_address)
    total_train_count += 1
    train_label_file.write(new_address + ' ' + class_encoding[style_dir] +'\n')
  for i in range(train_count, train_count + test_count):
    old_address = target_dir + '/' + style_dir + '/' + style_files[i]
    new_address = test_dir + '/image_' + str(total_test_count)
    shutil.copyfile(old_address, new_address)
    total_test_count += 1
    test_label_file.write(new_address + ' ' + class_encoding[style_dir] +'\n')
    
train_label_file.close()
test_label_file.close()
class_encoding_file.close()
