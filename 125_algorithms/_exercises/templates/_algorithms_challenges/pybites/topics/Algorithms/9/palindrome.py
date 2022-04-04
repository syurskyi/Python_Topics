"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
_______ __
_______ u__.r..

TMP = __.g..("TMP", "/tmp")
DICTIONARY = __.p...j..(TMP, 'dictionary_m_words.txt')
u__.r...u..(
    'https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt',
    DICTIONARY
)


___ load_dictionary
    """Load dictionary (sample) and return as generator (done)"""
    w__ o.. DICTIONARY) __ f:
        r.. (word.l...s.. ___ word __ f.r..


___ is_palindrome(word
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    temp = ''.j..([i ___ i __ word.l...s.. __ i.i..])
    r.. temp[::-1] __ temp


___ get_longest_palindrome(words_ N..
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    __ words __ N..
        words = load_dictionary()
    temp_list = (word ___ word __ words __ is_palindrome(word
    r.. m..(l..(temp_list), key=l..)

