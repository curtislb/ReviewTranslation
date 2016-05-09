#!/usr/bin/env python

import ast
import sys
import nltk
import numpy as np

from review_data import read_reviews

###############################################################################

def main():

    low = 3.0
    high = 4.0
    target_language = u"english"

    topics = []
    with open(sys.argv[1]) as infile:
        for topic in infile:
            topics.append(ast.literal_eval(topic))
            
    outfiles = []
    prefix = sys.argv[3]
    for i in xrange(len(topics)):
        outfile = []
        outfile.append(open(prefix + str(i) + "-.json" ,"w"))
        outfile.append(open(prefix + str(i) + "=.json" ,"w"))    
        outfile.append(open(prefix + str(i) + "+.json" ,"w"))    
        outfiles.append(outfile)
    counter = 0
    for review in read_reviews(sys.argv[2]):

        if review['lang'] != target_language:
            continue

        text = review['text']
        tokens = nltk.word_tokenize(text)
        best_value = [0]*len(topics)

        for token in tokens:
            for i in xrange(len(topics)):
                if token in topics[i]:
                    best_value[i] += topics[i][token]
        
        rating = review['rating']
        del review['lang']
        del review['rating']
        if rating < low:
            outfiles[np.argmax(best_value)][0].write(str(review) + '\n') 
       
        elif rating > high:
            outfiles[np.argmax(best_value)][2].write(str(review) + '\n')     

        else:
            outfiles[np.argmax(best_value)][1].write(str(review) + '\n')     

        counter+=1
        if counter %10000 == 0:
            for outfile in outfiles:
                for ofile in outfile:
                    ofile.flush()

    for outfile in outfiles:
        for ofile in outfile:
            ofile.close()

if __name__ == '__main__':
    main()
