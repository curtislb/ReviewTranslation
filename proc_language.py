#!/usr/bin/env python

import nltk
import numpy as np
import sys

from nltk.corpus import stopwords
from review_data import read_reviews

###############################################################################

languages = stopwords.fileids()

stopword_sets = [set(stopwords.words(lang)) for lang in languages]

target_languages = [u'english', u'spanish']

###############################################################################

def detect_language(tokens):
    token_set = set(tokens)

    lang_scores = []
    for stopword_set in stopword_sets:
        common_words = stopword_set & token_set
        lang_scores.append(len(common_words))

    best_index = np.argmax(lang_scores)
    best_lang = languages[best_index]
    best_score = lang_scores[best_index]
    lang_cover = float(best_score) / len(token_set)
    return best_lang, lang_cover

###############################################################################

def main():
    with open(sys.argv[2], 'w') as outfile:
        for review in read_reviews(sys.argv[1]):
            text = review['reviewText']
            tokens = [t.lower() for t in nltk.wordpunct_tokenize(text)]
            if tokens:
                lang, cover = detect_language(tokens)
                if lang in target_languages:
                    new_dict = {
                        'text': text,
                        'rating': review['overall'],
                        'lang': lang,
                        'cover': cover,
                    }
                    outfile.write(str(new_dict) + '\n')


if __name__ == '__main__':
    main()
