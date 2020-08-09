"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
______ os
______ urllib.request

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


___ load_dictionary(
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        r_ (word.lower().strip() for word in f.readlines())


___ is_palindrome(word: str
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    string = ''.join(c.lower() for c in word __ c.isalpha())
    r_ string __ string[::-1]


___ get_longest_palindrome(words=None
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    __ words is None:
        words = load_dictionary()
    pals = [word for word in words __ is_palindrome(word)]
    r_ sorted(pals, key=lambda x:-le.(x))[0]
