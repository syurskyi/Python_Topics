"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
_______ os
_______ urllib.request

DICTIONARY = os.path.j..('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


___ load_dictionary
    """Load dictionary (sample) and return as generator (done)"""
    w__ open(DICTIONARY) __ f:
        r.. (word.l...s.. ___ word __ f.readlines())


___ is_palindrome(word: s..):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    s__ = ''.j..(c.l.. ___ c __ word __ c.isalpha())
    r.. s__ __ s__[::-1]


___ get_longest_palindrome(words_ N..
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    __ words __ N..
        words = load_dictionary()
    pals = [word ___ word __ words __ is_palindrome(word)]
    r.. s..(pals, key=l.... x:-l..(x))[0]
