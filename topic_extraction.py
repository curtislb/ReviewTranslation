from __future__ import print_function
from time import time

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

import sys
import numpy as np
from review_data import read_reviews
import nltk
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize

n_samples = 2000
n_features = 1000
n_topics = 10
n_top_words = 50

def print_top_words(model, feature_names):
	for topic_idx, topic in enumerate(model.components_):
                print("{",end = "")

                for i in topic.argsort()[:-n_top_words:-1]:
                        print('"{}": {}, '.format(feature_names[i], topic[i]), end="")
                print("}")

print("Loading dataset...")
t0 = time()

#counter = 0
#p_stemmer = PorterStemmer()
data_samples = []
for review in read_reviews(sys.argv[1]):
#        if counter > 100:
#                break
#        counter += 1
#        if review["lang"] == "english":
#                tokens = word_tokenize(review["text"])
#                data_samples.append(" ".join([p_stemmer.stem(i) for i in tokens]))
        data_samples.append(review['text'])
print("done in %0.3fs." % (time() - t0))
# Use tf-idf features for NMF.

#print("Extracting tf-idf features for LDA...")
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=n_features)
t0 = time()
tf = tf_vectorizer.fit_transform(data_samples)
#print("done in %0.3fs." % (time() - t0))

#print("Fitting LDA models with tf features, n_samples=%d and n_features=%d..."% (n_samples, n_features))
lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=5,
                                learning_method='online', learning_offset=50.,
                                random_state=0)
t0 = time()
lda.fit(tf)
print("LDA fit done in %0.3fs." % (time() - t0))

print("\nTopics in LDA model:")
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names)
