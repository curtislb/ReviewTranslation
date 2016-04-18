#!/usr/bin/env python

import ast
import gzip
import nltk
import sys

from collections import Counter
from nltk.corpus import stopwords

###############################################################################

def detect_language(tokens, languages=stopwords.fileids()):
    token_set = set(tokens)

    lang_scores = []
    for lang in languages:
        stopword_set = set(stopwords.words(lang))
        common_words = stopword_set & token_set
        lang_scores.append(len(common_words))

    return max(languages, key=lang_scores)


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
            lang, __ = detect_language(tokens)
            lang_counts[lang] += 1
    
    print lang_counts


if __name__ == '__main__':
    main()
