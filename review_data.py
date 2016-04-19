#!/usr/bin/env python

import ast
import gzip

###############################################################################

def read_reviews(path):
    review_file = gzip.open(path, 'rb')
    for line in review_file:
        yield ast.literal_eval(line)
