_______ __
_______ u__.r..
____ c.. _______ C..

# data provided
tmp  __.g.. TMP  /tmp
stopwords_file __.p...j..(tmp, 'stopwords')
harry_text __.p...j..(tmp, 'harry')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


___ get_harry_most_common_word
    common_word    # list
    w__ o.. stopwords_file) __ f:
        stopwords_list [word.s.. ___ word __ f.r..]
        #print(stopwords_list)
    w__ o.. harry_text, encoding='utf8') __ f:
        ___ lines __ f:
            ___ word __ lines.s.. :
                #print(word)
                word_to_test "".j..(letter.l.. ___ letter __ word __ letter.i..
                #print(word1)
                __ word_to_test a.. word_to_test n.. __ stopwords_list :
                    common_word.a..(word_to_test)
    r.. C..(common_word).most_common(1)[0]

get_harry_most_common_word()
#print(get_harry_most_common_word())