import os
import urllib.request
import re
from collections import Counter

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


def get_harry_most_common_word():
    stopwords = open(stopwords_file).read().split()
    text = open(harry_text).read().lower()
    filtered = re.sub(r'[^A-Za-z\s*]', '', text).split()
    words = [word for word in filtered if word not in stopwords]
    return Counter(words).most_common(1)[0]