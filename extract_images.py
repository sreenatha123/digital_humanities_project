#!/usr/bin/python

# Author : Sreenatha Bhatlapenumarthi
# Date : February 8, 2014
'''A python script to perform customized downloading of paintings from google images '''

# Import required modules
import sys
import os
import urllib
import urllib2

# Search parameters
painters = ['picasso', 'van gogh', 'dali', 'dali', 'monet', 'cezanne']
image_count = 20


for painter in painters:
  if not os.path.exists("./" + painter):
    os.makedirs("./" + painter)
  image_search_URL = 'http://www.google.com/images?q='+ painter + '+paintings&safe=active&tbs=ift:png,isz:m'
  opener = urllib2.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0')]
  page = opener.open(image_search_URL).read()
  for i in range(1,image_count+1):
    image_URL = page.split('<img')[i].split('src="')[1].split('" width')[0]
    urllib.urlretrieve(image_URL, "./" + painter + "/image_" + str(i))


