_______ os
_______ urllib.request
_______ re
____ collections _______ Counter

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


___ get_harry_most_common_word():
    stopwords = open(stopwords_file).read().s..
    text = open(harry_text).read().lower()
    filtered = re.sub(r'[^A-Za-z\s*]', '', text).s..
    words = [word ___ word __ filtered __ word n.. __ stopwords]
    r.. Counter(words).most_common(1)[0]