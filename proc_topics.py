#!/usr/bin/env python

import sys

from review_data import make_data_frame

###############################################################################

def main():
    data_frame = make_data_frame(sys.argv[1])
    print data_frame.size


if __name__ == '__main__':
    main()
