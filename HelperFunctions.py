import os
import imp
import sys

import numpy as np
import pandas as pd
import re

import matplotlib.pyplot as plt

from wordcloud import WordCloud,STOPWORDS


def wordcloud_draw(data, color = 'black'):
	import matplotlib.pyplot as plt
	words = ' '.join(data)
	cleaned_word = " ".join([word for word in words.split()
							if 'flight' not in word
								and not word.startswith('flew')
								and not word.startswith('germanwing')
								and not word.startswith('passenger')
								and not word.startswith('airline')
							])
	wordcloud = WordCloud(stopwords=STOPWORDS,
					  background_color=color,
					  width=2500,
					  height=2000
					 ).generate(cleaned_word)
	plt.figure(1,figsize=(13, 13))
	plt.imshow(wordcloud)
	plt.axis('off')
	plt.show()
