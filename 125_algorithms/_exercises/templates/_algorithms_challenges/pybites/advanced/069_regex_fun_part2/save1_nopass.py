# _______ __
#
#
# ___ has_timestamp text
#     """Return True if text has a timestamp of this format:
#        2014-07-03T23:30:37"""
#     r.. b.. __.s.. _ \_ 4 -\_ 2 -\_ 2 T\_ 2 |\_ 2 |\_ 2  ?
#
#
# ___ is_integer number
#     """Return True if number is an integer"""
#     r.. b.. __.s.. _ ^[-+]?\d+$  s.. ?
#
#
# ___ has_word_with_dashes text
#     """Returns True if text has one or more words with dashes"""
#     r.. b.. __.s.. _ \w+-\w+?
#
#
# ___ remove_all_parenthesis_words text
#     """Return text but without any words or phrases in parenthesis:
#        'Good morning (afternoon)' -> 'Good morning' (so don't forget
#        leading spaces)"""
#     r.. __.s.. _  \([^)]*\)  ' ' ?
#
#
# ___ split_string_on_punctuation text
#     """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
#        ['hi', 'how are you doing', 'blabla']
#        (make sure you strip trailing spaces)"""
#     r.. l.. f.. N.., __.s.. _ \s?[?!\.,;]\s? ?
#
#
# ___ remove_duplicate_spacing text
#     """Replace multiple spaces by one space"""
#     r.. __.s.. _ \s{2,} ' ' ?
#
#
# ___ has_three_consecutive_vowels word
#     """Returns True if word has at least 3 consecutive vowels"""
#     r.. b.. __.s.. _ [aeiou]{3,} ?
#
#
# ___ convert_emea_date_to_amer_date date
#     """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
#        (AMER date format)"""
#     pattern __.c.. _  \_ 2 /(\_ 2 /(\_ 4
#     m ?.m.. ?
#     r.. _* m.g.. 2)}/{m.g.. 1)}/{m.g.. 3)}' __ m ____ m