_______ s__

_______ p__

____ spelling _______ suggest_word, load_words


@p__.f..(scope='module')
___ a_words
    """Get only a[abcdefghijklm]-words to speed up tests"""
    words = load_words()
    r.. {word ___ word __ words
            __ word.startswith('a') a.. l..(word) > 1
            a.. word[1] __ s__.ascii_letters[:13]}


@p__.m__.p..("word, expected", [
    ('acheive', 'achieve'),
    ('accross', 'across'),
    ('acceptible', 'acceptable'),
    ('allmost', 'almost'),
    ('aquire', 'acquire'),
    ('agressive', 'aggressive'),
    ('accomodate', 'accommodate'),
    ('accidentaly', 'accidentally'),
])
___ test_suggest_word(word, expected, a_words):
    ... suggest_word(word, words=a_words) __ expected