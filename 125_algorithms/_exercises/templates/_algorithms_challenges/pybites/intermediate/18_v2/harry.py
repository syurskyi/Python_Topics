_______ os
_______ urllib.request
_______ __
____ collections _______ Counter

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


    with open(harry_text,'r',encoding='utf-8') __ f:
        text = f.read()

    
    with open(stopwords_file,'r') __ f:
        stopwords = f.read().splitlines()

    
    text = __.sub(r'[^a-z0-9\s]','',text.lower())
    words = text.s..

    word_counts = Counter(word ___ word __ text.s..  __ word n.. __ stopwords)


    r.. word_counts.most_common(1)[0]



__ __name__ __ "__main__":

    get_harry_most_common_word()

