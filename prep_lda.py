#!/usr/bin/env python

import nltk
import numpy as np
import sys

from review_data import read_reviews

def main():
    with open(sys.argv[2], 'w') as outfile:
        for review in read_reviews(sys.argv[1]):
            text = review['text']
            tokens = [t.lower() for t in nltk.wordpunct_tokenize(text)]
            if tokens:
                lang = detect_language(tokens)
                if lang in target_languages:
                    new_dict = {
                        'text': text,
                        'rating': review['overall'],
                        'lang': lang,
                    }
                    outfile.write(str(new_dict) + '\n')


if __name__ == '__main__':
    main()
