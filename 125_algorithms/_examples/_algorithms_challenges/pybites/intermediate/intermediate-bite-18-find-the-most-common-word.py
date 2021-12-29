"""
Write a function that returns the most common (non stop)word in this Harry Potter text.

Make sure you convert to lowercase, strip out non-alphanumeric characters and stopwords.
Your function should return a tuple of (most_common_word, frequency).

The template code already loads the Harry Potter text and list of stopwords in.

Check the tests for more info - have fun!

KEYWORDS: Counter, data analysis, list comprehensions
"""

import os
import urllib.request
import string
from collections import Counter
import re



# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)

def my_solution_get_harry_most_common_word():
    """
    High level concept:
    * prepare a list with stopwords
    * go over text word by word, stripping all non-alphanumeric characters
        * if a word does not exist in stopwords list, add it to another list (let's call it filtered)
    * once we have filtered list ready, feed it to the counter object
    * retrieve 1st most common object and return it
    """

    stopwords = []
    filtered = []
    f1 = open(stopwords_file, 'r')
    for line in f1:
        stopwords.append(line.strip())

    f2 = open(harry_text, 'r')
    for line in f2:
        for word in line.split():
            print(word)
            p = word.strip(string.punctuation).lower()

            if len(p) > 0 and p not in stopwords:
                filtered.append(word.strip(string.punctuation).lower())

    counter = Counter(filtered)
    return counter.most_common(1)[0]

def pyb_solution_get_harry_most_common_word():
    def get_harry_most_common_word():
        with open(stopwords_file) as f:
            stopwords = set(f.read().strip().lower().split('\n'))

        with open(harry_text) as f:
            words = [re.sub(r'\W+', r'', word)  # [^a-zA-Z0-9_]
                     for word in f.read().lower().split()]

            words = [word for word in words if word.strip()
                     and word not in stopwords]

            cnt = Counter(words)
            return cnt.most_common(1)[0]


print(my_solution_get_harry_most_common_word())