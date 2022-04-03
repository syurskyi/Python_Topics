"""
Write a function that returns the most common (non stop)word in this Harry Potter text.

Make sure you convert to lowercase, strip out non-alphanumeric characters and stopwords.
Your function should return a tuple of (most_common_word, frequency).

The template code already loads the Harry Potter text and list of stopwords in.

Check the tests for more info - have fun!

KEYWORDS: Counter, data analysis, list comprehensions
"""

_______ __
_______ u__.r..
_______ s__
____ c.. _______ Counter
_______ __



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

___ my_solution_get_harry_most_common_word
    """
    High level concept:
    * prepare a list with stopwords
    * go over text word by word, stripping all non-alphanumeric characters
        * if a word does not exist in stopwords list, add it to another list (let's call it filtered)
    * once we have filtered list ready, feed it to the counter object
    * retrieve 1st most common object and return it
    """

    stopwords    # list
    filtered    # list
    f1 = o.. stopwords_file, _
    ___ line __ f1:
        stopwords.a..(line.strip

    f2 = o.. harry_text, _
    ___ line __ f2:
        ___ word __ line.s.. :
            print(word)
            p = word.strip(s__.punctuation).l..

            __ l..(p) > 0 a.. p n.. __ stopwords:
                filtered.a..(word.strip(s__.punctuation).l..

    counter = Counter(filtered)
    r.. counter.most_common(1)[0]

___ pyb_solution_get_harry_most_common_word
    ___ get_harry_most_common_word
        w__ o.. stopwords_file) __ f:
            stopwords = s..(f.r...s...l...s..('\n'))

        w__ o.. harry_text) __ f:
            words = [__.sub(r'\W+', r'', word)  # [^a-zA-Z0-9_]
                     ___ word __ f.r...l...s.. ]

            words = [word ___ word __ words __ word.s..
                     a.. word n.. __ stopwords]

            cnt = Counter(words)
            r.. cnt.most_common(1)[0]


print(my_solution_get_harry_most_common_word