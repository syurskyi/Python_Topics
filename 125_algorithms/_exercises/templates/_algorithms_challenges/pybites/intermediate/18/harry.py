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

    # Stopwords
    w__ o.. stopwords_file) __ file:
        stopwords = [word.s.. ___ word __ file]

    # Harry text
    w__ o.. harry_text) __ file:
        content_remove_apos = [line.r..("'", "").r..("’", "") ___ line __ file]
        harry_content = [__.sub(r"\W+", " ", line).s...l.. ___ line __ content_remove_apos]

        final_words    # list
        ___ line __ harry_content:
            current_line = line.s..(" ")
            ___ word __ current_line:
                __ word __ "":
                    _____
                __ word n.. __ stopwords:
                    final_words.a..(word)

        counter = C..(final_words)
        r.. counter.m..[0]