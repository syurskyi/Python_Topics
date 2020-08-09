______ os
______ urllib.request
______ re
from collections ______ Counter

# data provided

stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)

WORD_REGEX = r"(['\w]+)"
word_regex = re.compile(WORD_REGEX)


___ get_harry_most_common_word(
    with open(harry_text) as f:
        words = word_regex.findall(f.read().lower())
    with open(stopwords_file) as f:
        stops = word_regex.findall(f.read().lower())
    r_ Counter([x for x in words __ x not in stops]).most_common(1)[0]
