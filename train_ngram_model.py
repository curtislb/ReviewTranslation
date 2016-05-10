#!/usr/bin/env python

#from nltk.model import NgramModel
from ngram import NgramModel
import sys
import cPickle as pickle

from review_data import read_reviews
from nltk.corpus import stopwords

import time

###############################################################################

def main():
    
    start = time.clock()

    #sys.argv[1] is path to training data
    #sys.argv[2] is length of n-grams

    ngram_model = NgramModel(int(sys.argv[2]), sys.argv[1], pad_right=True)

    end = time.clock()
    print 'Done computing ngram model, ' + str(end - start) + ' seconds running time'

    fileName = sys.argv[2] + 'gramModel' + '_' + sys.argv[1][3:].split('.')[0] + '.p'
    pickle.dump(ngram_model, open(fileName, 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

    end = time.clock()
    print 'Done pickling, ' + str(end - start) + ' seconds running time'
    
    '''
    #for unpickling
    fileName = sys.argv[2] + 'gramModel' + '_' + sys.argv[1][3:].split('.')[0] + '.p'
    restored_model = pickle.load(open(fileName, 'rb'))
    #end = time.clock()
    #print 'Done unpickling, ' + str(end - start) + ' seconds running time'
    '''

    print "Generated examples: "
    for i in range (200):
        #print ' '.join(ngram_model.generate(20, ('', '')))

        review = []
        context = ['', '']
        nextToken = ngram_model._generate_one(context)
        while nextToken != '.' and nextToken != '...EOR...' and len(review) < 500:
            review.append(nextToken)
            context[0] = context[1]
            context[1] = nextToken
            nextToken = ngram_model._generate_one(context)

        print ' '.join(review) + '   len: ' + str(len(review))

if __name__ == '__main__':
    main()
