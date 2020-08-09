______ string

______ pytest

from spelling ______ suggest_word, load_words


@pytest.fixture(scope='module')
___ a_words(
    """Get only a[abcdefghijklm]-words to speed up tests"""
    words = load_words()
    r_ {word ___ word in words
            __ word.startswith('a') and le.(word) > 1
            and word[1] in string.ascii_letters[:13]}


@pytest.mark.parametrize("word, expected", [
    ('acheive', 'achieve'),
    ('accross', 'across'),
    ('acceptible', 'acceptable'),
    ('allmost', 'almost'),
    ('aquire', 'acquire'),
    ('agressive', 'aggressive'),
    ('accomodate', 'accommodate'),
    ('accidentaly', 'accidentally'),
])
___ test_suggest_word(word, expected, a_words
    assert suggest_word(word, words=a_words) __ expected