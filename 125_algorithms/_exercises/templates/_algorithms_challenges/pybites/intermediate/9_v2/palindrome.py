# """A palindrome is a word, phrase, number, or other sequence of characters
# which reads the same backward as forward"""
# _______ __
# _______ u__.r..
# _______ __
#
# TMP  __.g.. TMP  /tmp
# DICTIONARY  __.p...j..? dictionary_m_words.txt
# u__.r...u..
#     'https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt',
#     ?
#
#
#
# ___ load_dictionary
#     """Load dictionary (sample) and return as generator (done)"""
#     w__ o.. ? __ f
#         r..  word.l...s.. ___ ? __ ?.r..
#
#
# ___ is_palindrome word
#     """Return if word is palindrome, 'madam' would be one.
#        Case insensitive, so Madam is valid too.
#        It should work for phrases too so strip all but alphanumeric chars.
#        So "No 'x' in 'Nixon'" should pass (see tests for more)"""
#
#
#
#     word  __.s.. _ \W '' w.. .l..
#
#     low,high  0,l.. ? - 1
#
#
#     w.... ? < ?
#         __ ? l.. !_ ? h..
#             r.. F..
#
#         l.. +_ 1
#         h.. -_ 1
#
#     r.. T..
#
#
#
# ___ get_longest_palindrome words_ N..
#     """Given a list of words return the longest palindrome
#        If called without argument use the load_dictionary helper
#        to populate the words list"""
#
#     __ n.. ?
#         words  ?
#
#     longest_length  f__ "-inf"
#     longest  N..
#     ___ word __ ?
#         __ i.. ?
#             __ l.. ? > ?
#                 l..  l. ?
#                 l..  w..
#
#     r.. ?
#
