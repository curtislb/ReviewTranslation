#!/usr/bin/env python

import gzip
import sys


def parse_reviews(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)


def main():
    count = 0
    for review in parse_reviews(sys.argv[1]):
        count += 1
    print count


if __name__ == '__main__':
    main()