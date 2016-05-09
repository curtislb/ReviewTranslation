#!/usr/bin/env python

import sys
import ast
import operator

def main():
    with open(sys.argv[1]) as infile:
        for line in infile:
            topic = ast.literal_eval(line)
            sorted_x = sorted(topic.items(), key=operator.itemgetter(1), reverse=True)
            print " ".join([i[0] for i in sorted_x])

if __name__ == "__main__":
    main()
