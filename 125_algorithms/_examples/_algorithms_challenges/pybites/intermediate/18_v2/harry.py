import os
import u__.r..
import re
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():


    with open(harry_text,'r',encoding='utf-8') as f:
        text = f.read()

    
    with open(stopwords_file,'r') as f:
        stopwords = f.read().splitlines()

    
    text = re.sub(r'[^a-z0-9\s]','',text.lower())
    words = text.split()

    word_counts = Counter(word for word in text.split() if word not in stopwords)


    return word_counts.most_common(1)[0]



if __name__ == "__main__":

    get_harry_most_common_word()

