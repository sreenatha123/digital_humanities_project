#!/usr/bin/python

# Author : Sreenatha Bhatlapenumarthi
# Date : February 8, 2014
'''A python script to perform customized downloading of paintings from google images '''

# Import required modules
import sys
import os
import urllib
import urllib2

train_dir = 'training'
test_dir = 'test'
train_label_filename = 'train_label_file'
test_label_filename = 'test_label_file'
if not os.path.exists(train_dir):
  os.makedirs(train_dir)
if not os.path.exists(test_dir):
  os.makedirs(test_dir)
train_label_file = open(train_label_filename,'w+')
train_label_string = ''
test_label_file = open(test_label_filename,'w+')
test_label_string = ''
encoding_filename = './class_encoding'
encoding_file = open(encoding_filename, 'w+')
encoding_string = ''

# Search parameters
painters = ['picasso', 'van gogh', 'dali', 'monet', 'cezanne']
#train_image_count = 10
#test_image_count = 2
train_image_count = int(raw_input("Training size : "))
test_image_count = int(raw_input("Testing size : "))

total_train_count = 0
total_test_count = 0

for i in range(len(painters)):
  pages = []
  for j in range(max(train_image_count,test_image_count)/10 + 1):
    image_search_URL = 'http://www.google.com/images?q=' + painters[i] + '+paintings&safe=active&tbs=ift:png,isz:m' + '&start=' + str(20*j)
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    pages.append(opener.open(image_search_URL).read())
 
  # Download Training images
  print 'Downloading Training images for ', painters[i]
  for j in range(train_image_count):
    image_URL = pages[j/10].split('<img')[j%10+1].split('src="')[1].split('" width')[0]
    total_train_count += 1
    image_address = train_dir + "/image_" + str(total_train_count)
    urllib.urlretrieve(image_URL, image_address)
    train_label_string += (image_address + ' ' + str(i) + '\n')

  # Download Testing images
  print 'Downloading Test Images for ', painters[i]
  for j in range(test_image_count):
    image_URL = pages[j/10].split('<img')[j%10+11].split('src="')[1].split('" width')[0]
    total_test_count += 1
    image_address = test_dir + "/image_" + str(total_test_count)
    urllib.urlretrieve(image_URL, image_address)
    test_label_string += (image_address + ' ' + str(i) + '\n')

  encoding_string += (str(i) + ' ' + painters[i] + '\n') 

train_label_file.write(train_label_string)
train_label_file.close()
test_label_file.write(test_label_string)
test_label_file.close()
encoding_file.write(encoding_string)
encoding_file.close()

