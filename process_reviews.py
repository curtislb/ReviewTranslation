#!/usr/bin/env python

import gzip
import pandas as pd
import sys


def parse_reviews(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)


def get_data_frame(path):
    i = 0
    df = {}
    for d in parse_reviews(path):
        df[i] = d
        i += 1

    return pd.DataFrame.from_dict(df, orient='index')


def main():
    df = get_data_frame(sys.argv[1])
    print df.size


if __name__ == '__main__':
    main()