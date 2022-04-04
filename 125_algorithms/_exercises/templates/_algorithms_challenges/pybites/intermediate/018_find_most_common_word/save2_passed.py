_______ __
_______ u__.r..
_______ __
____ c.. _______ C..

# data provided
tmp = __.g..("TMP", "/tmp")
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
    stopwords = o.. stopwords_file).r...s..
    text = o.. harry_text).r...l..
    filtered = __.sub(r'[^A-Za-z\s*]', '', text).s..
    words = [word ___ word __ filtered __ word n.. __ stopwords]
    r.. C..(words).most_common(1)[0]