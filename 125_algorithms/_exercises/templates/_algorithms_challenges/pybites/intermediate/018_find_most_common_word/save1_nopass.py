_______ os
_______ urllib.request

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.j..(tmp, 'stopwords')
harry_text = os.path.j..(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


___ get_harry_most_common_word
    stopwords = open(stopwords_file).read().s..
    text = open(harry_text).read().l..
    filtered = __.sub(r'[^A-Za-z\s*]', '', text).s..
    words = [word ___ word __ filtered __ word n.. __ stopwords]
    r.. Counter(words).most_common(1)[0]