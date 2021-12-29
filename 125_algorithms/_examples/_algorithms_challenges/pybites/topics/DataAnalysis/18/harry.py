import os
import urllib.request
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
    common_word = []
    with open(stopwords_file) as f:
        stopwords_list = [word.strip() for word in f.readlines()]
        #print(stopwords_list)
    with open(harry_text, encoding='utf8') as f:
        for lines in f:
            for word in lines.split():
                #print(word)
                word_to_test = "".join(letter.lower() for letter in word if letter.isalnum())
                #print(word1)
                if word_to_test and word_to_test not in stopwords_list :
                    common_word.append(word_to_test)
    return Counter(common_word).most_common(1)[0]

get_harry_most_common_word()
#print(get_harry_most_common_word())