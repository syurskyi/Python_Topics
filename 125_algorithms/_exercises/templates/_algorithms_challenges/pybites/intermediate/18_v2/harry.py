_______ __
_______ u__.r..
_______ __
____ c.. _______ Counter

# data provided
tmp = __.getenv("TMP", "/tmp")
stopwords_file = __.p...j..(tmp, 'stopwords')
harry_text = __.p...j..(tmp, 'harry')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


___ get_harry_most_common_word


    w__ o.. harry_text,'r',encoding='utf-8') __ f:
        text = f.r..

    
    w__ o.. stopwords_file _ __ f:
        stopwords = ?.r__.s..

    
    text = __.sub(r'[^a-z0-9\s]','',text.l..
    words = text.s..

    word_counts = Counter(word ___ word __ text.s..  __ word n.. __ stopwords)


    r.. word_counts.most_common(1)[0]



__ _______ __ _______

    get_harry_most_common_word()

