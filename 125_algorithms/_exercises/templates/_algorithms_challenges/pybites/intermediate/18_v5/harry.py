_______ os
_______ urllib.request
_______ __
____ collections _______ Counter

# data provided

stopwords_file = os.path.j..('/tmp', 'stopwords')
harry_text = os.path.j..('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)

WORD_REGEX = r"(['\w]+)"
word_regex = __.c..(WORD_REGEX)


___ get_harry_most_common_word():
    with open(harry_text) as f:
        words = word_regex.findall(f.read().lower())
    with open(stopwords_file) as f:
        stops = word_regex.findall(f.read().lower())
    r.. Counter([x ___ x __ words __ x n.. __ stops]).most_common(1)[0]
