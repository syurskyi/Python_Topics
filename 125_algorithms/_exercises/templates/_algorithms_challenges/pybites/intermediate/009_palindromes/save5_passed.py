# """A palindrome is a word, phrase, number, or other sequence of characters
# which reads the same backward as forward"""
# _______ __
# _______ u__.r..
#
# DICTIONARY  __.p...j.. /tmp dictionary_m_words.txt
# u__.r...u.. http://bit.ly/2Cbj6zn ?
#
#
# ___ load_dictionary
#     """Load dictionary (sample) and return as generator (done)"""
#     w__ o.. ? __ f
#         r.. word.l...s.. ___ ? __ ?.r.
#
#
# ___ is_palindrome word
#     """Return if word is palindrome, 'madam' would be one.
#        Case insensitive, so Madam is valid too.
#        It should work for phrases too so strip all but alphanumeric chars.
#        So "No 'x' in 'Nixon'" should pass (see tests for more)"""
#     w  ?.r.. ' ' '' .l..
#     output  ''.j.. ch ___ ? __ ? __ ?.i.
#     r.. ? __ ? ||-1
#
#
# ___ get_longest_palindrome words_ N..
#     """Given a list of words return the longest palindrome
#        If called without argument use the load_dictionary helper
#        to populate the words list"""
#     __ words __ N..
#         words  word ___ ? __ ?
#     longest_word  ''
#     ___ word __ ?
#         __ l.. ? > l.. ? a.. ? ?
#             l..  w..
#     r.. ?