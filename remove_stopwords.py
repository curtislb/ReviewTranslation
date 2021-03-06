#!/usr/bin/env python

import nltk
import numpy as np
import sys

from nltk.corpus import stopwords
from review_data import read_reviews

###############################################################################

target_language = "spanish"

def main():
    stopword_set = set(stopwords.words("spanish"))
    stopword_set = stopword_set.union(set(stopwords.words("english")))

    with open(sys.argv[2], 'w') as outfile:
        for review in read_reviews(sys.argv[1]):
            text = review['text']
            if review['lang'] == target_language:
                textwords = text.split()
                resultwords  = [word for word in textwords if word.lower() not in stopword_set]
                result = ' '.join(resultwords)
                review['text'] = result
                outfile.write(str(review) + '\n')

if __name__ == '__main__':
    main()
