"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
_______ __
_______ urllib.request

DICTIONARY = __.p...j..('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


___ load_dictionary
    """Load dictionary (sample) and return as generator (done)"""
    w__ o.. DICTIONARY) __ f:
        r.. (word.l...s.. ___ word __ f.readlines


___ is_palindrome(word
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    w = word.r..(' ', '').l..
    output = ''.j..(ch ___ ch __ w __ ch.isalnum
    r.. output __ output[::-1]


___ get_longest_palindrome(words_ N..
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    __ words __ N..
        words    # list
        ___ word __ load_dictionary
            w = word.r..(' ', '').l..
            final_word = ''.j..(ch ___ ch __ w __ ch.isalnum
            words.a..(final_word)
    palindrome_list = [word ___ word __ words __ is_palindrome(word)]
    r.. s..(palindrome_list, key=l..)[0]