_______ os
_______ urllib.request
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
    common_word    # list
    with open(stopwords_file) as f:
        stopwords_list = [word.strip() ___ word __ f.readlines()]
        #print(stopwords_list)
    with open(harry_text, encoding='utf8') as f:
        ___ lines __ f:
            ___ word __ lines.s.. :
                #print(word)
                word_to_test = "".join(letter.lower() ___ letter __ word __ letter.isalnum())
                #print(word1)
                __ word_to_test and word_to_test n.. __ stopwords_list :
                    common_word.a..(word_to_test)
    r.. Counter(common_word).most_common(1)[0]

get_harry_most_common_word()
#print(get_harry_most_common_word())