#!/usr/bin/env python

import ast
import gzip
import nltk
import numpy as np
import sys

from collections import Counter
from nltk.corpus import stopwords

###############################################################################

languages = [u'english', u'spanish']

stopword_sets = [set(stopwords.words(lang)) for lang in languages]

###############################################################################

def detect_language(tokens):
    token_set = set(tokens)

    lang_scores = []
    for stopword_set in stopword_sets:
        common_words = stopword_set & token_set
        lang_scores.append(len(common_words))

    return languages[np.argmax(lang_scores)]


# def make_dict_str(dictionary):
#     str_list = ['{']
#     for key, value in dictionary.iteritems():
#         str_list.append(repr(key))
#         str_list.append(':')
#         str_list.append(repr(value))
#         str_list.append(',')
#
#     str_list[-1] = '}'
#     return ''.join(str_list)


def read_reviews(path):
    review_file = gzip.open(path, 'rb')
    for line in review_file:
        yield ast.literal_eval(line)

###############################################################################

def main():
    lang_counts = Counter()
    for review in read_reviews(sys.argv[1]):
        text = review['reviewText']
        tokens = [t.lower() for t in nltk.wordpunct_tokenize(text)]
        if tokens:
            lang = detect_language(tokens)
            lang_counts[lang] += 1
    
    print lang_counts


if __name__ == '__main__':
    main()
