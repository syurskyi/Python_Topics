# """A palindrome is a word, phrase, number, or other sequence of characters
# which reads the same backward as forward"""
# _______ __
# _______ u__.r..
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
#         r.. word.l...s.. ___ ? __ f.r..
#
#
# ___ _clean_wordword
#     r.. "".j.. char.l.. ___ ? __ ? __ ?.i..
#
#
# ___ is_palindrome word
#     """Return if word is palindrome, 'madam' would be one.
#        Case insensitive, so Madam is valid too.
#        It should work for phrases too so strip all but alphanumeric chars.
#        So "No 'x' in 'Nixon'" should pass (see tests for more)"""
#     word_clean  ? ?
#     __ ? __ ?  ||-1
#         r.. T..
#     r.. F..
#
#
# ___ get_longest_palindrome words_ N..
#     """Given a list of words return the longest palindrome
#        If called without argument use the load_dictionary helper
#        to populate the words list"""
#     __ words __ N..
#         words  ?
#
#     palindrome    # dict
#     ___ word __ ?
#         __ i.. ?
#             palindrome_length  l.. ? ?
#             ??  ?
#     r.. m.. ? k.._p__.g..
#
#
# #if __name__ == "__main__":
#     #is_palindrome("madam")
#     #is_palindrome("A Toyota’s a Toyota.")
#     #print(get_longest_palindrome(["A Toyota’s a Toyota.", "madam"]))
#     #print(get_longest_palindrome())