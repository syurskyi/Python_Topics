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

    # Stopwords
    with open(stopwords_file) as file:
        stopwords = [word.strip() for word in file]

    # Harry text
    with open(harry_text) as file:
        content_remove_apos = [line.replace("'", "").replace("’", "") for line in file]
        harry_content = [re.sub(r"\W+", " ", line).strip().lower() for line in content_remove_apos]

        final_words = []
        for line in harry_content:
            current_line = line.split(" ")
            for word in current_line:
                if word == "":
                    continue
                if word not in stopwords:
                    final_words.append(word)

        counter = Counter(final_words)
        return counter.most_common()[0]