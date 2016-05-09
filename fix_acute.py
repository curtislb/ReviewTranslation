import re
import sys

from review_data import read_reviews


def main():
    for review in read_reviews(sys.argv[1]):
        if review["lang"] == u"spanish":
            review['text'] = re.sub(r'&([a-z])acute;', r'\1', review['text'])
            print review
        else:
            print review
        
if __name__ == '__main__':
    main()
