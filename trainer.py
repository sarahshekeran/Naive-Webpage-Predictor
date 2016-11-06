import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.externals import joblib
import readcsvfile
from getsitecontent import getSiteContent
import os

#Training
label_url = readcsvfile.category_link('new_test.csv', 850)
tags_url = readcsvfile.tags('tags.csv')

count = 0
category_count = 1;

for row in label_url:
	category, site = row.split(',')

	print str(count+1)+":", category+",", site;

	result = getSiteContent(site)
	count += 1

	if result == '':
		print("%d. Failed to get content for %s" % (count, site))
	
	result += tags_url[count-1].decode('utf-8') + tags_url[count-1].decode('utf-8')
	
	#create a directory for the categories
	if not os.path.exists(category):
		os.makedirs(category)
		category_count = 1;
			
	#create a file for each webpage
	with open(os.path.join(category, category+str(category_count)+'.txt'), 'wb') as temp_file:
		temp_file.write(result.encode('utf8'))
		category_count+=1


print('done')


