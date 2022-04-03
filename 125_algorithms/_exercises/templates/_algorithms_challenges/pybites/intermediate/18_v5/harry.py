_______ __
_______ u__.r..
_______ __
____ c.. _______ C..

# data provided

stopwords_file = __.p...j..('/tmp', 'stopwords')
harry_text = __.p...j..('/tmp', 'harry')
u__.r...u..('http://bit.ly/2EuvyHB', stopwords_file)
u__.r...u..('http://bit.ly/2C6RzuR', harry_text)

WORD_REGEX = r"(['\w]+)"
word_regex = __.c..(WORD_REGEX)


___ get_harry_most_common_word
    w__ o.. harry_text) __ f:
        words = word_regex.f..(f.r...l..
    w__ o.. stopwords_file) __ f:
        stops = word_regex.f..(f.r...l..
    r.. C..([x ___ x __ words __ x n.. __ stops]).most_common(1)[0]
