These are the files in our project in usage order with a description of what they do.


count_reviews.py is a script to count the number of english and spanish reviews there are in a gzip file. Used at the beginning to judge what subset of the dataset we should use.
review_data.py is an io utility file
proc_language.py reads the dataset, detects the languages, and prints out only English and Spanish reviews with only the necessary fields
filter_reviews.py removes reviews that have less than 5 words
fix_acute.py changes all accents in Spanish to the unaccented letter
remove_stopwords.py removes stopwords from both Spanish and English
topic_extraction.py loads the reviews and fits an LDA using a CountVectorizer and outputs the top 50 words of n_topics topics.
categorize_reviews.py Uses the LDA words and weights to categorize the dataset
print_categories.py Takes the LDA words and weights and prints them in correct order in human readable format