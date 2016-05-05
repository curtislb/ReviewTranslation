#!/usr/bin/env python

import nltk
import numpy as np
import sys

from nltk.corpus import stopwords
from review_data import read_reviews

###############################################################################

def main():
    with open(sys.argv[2], 'w') as outfile:
        for review in read_reviews(sys.argv[1]):
            text = review['text']
            
            tokens = [t.lower() for t in nltk.wordpunct_tokenize(text)]
            if len(tokens) > 5:
            	outfile.write(str(review) + '\n')

if __name__ == '__main__':
    main()
