import os
import imp
import sys

import numpy as np
import pandas as pd
import re

def getfile(filename,results):
   f = open(filename,encoding = 'ascii', errors='ignore' ).readlines()
   filecontents = f
   for line in filecontents:
	   results.append(line)
   return results

def get_data(file, results):
	review = []
	for x in file:
		if x == '\n':
			results.append(review)
			review = []
		if x != '\n':
			review.append(x.replace('\n',''))

	print("number of records: " + str(len(results)))		
	
	return results

def get_record(review, citiesList):
	
	REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
	record = {}

	for idx, item in enumerate(review):
		if idx == 0:
			record['review_title'] = item
		if idx == 1:
			try:
				record['customer_name'] = item.split('(')[0]
				record['review_country'] = item.split('(')[1].split(')')[0]
				record['review_date'] = item.split('(')[1].split(')')[1]
			except:
				record['name'] = re.split(r'(\d+)', item)[0]
				record['review_country'] = "unknown"
				record['review_date'] = item.replace(re.split(r'(\d+)', item)[0], "")
		if idx == 2:
			record['review_score'] = item
		if idx == 3:
			record['review_text'] = REPLACE_NO_SPACE.sub("", item)
			record['possible_route'] = ' '.join(list(set(record['review_text'].lower().split()).intersection(citiesList)))
		if idx > 3:
			 record[item.split('\t')[0]] = item.split('\t')[1]

	return record
