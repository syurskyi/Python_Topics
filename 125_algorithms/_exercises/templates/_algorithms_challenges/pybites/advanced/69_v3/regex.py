# _______ __
#
#
# ___ has_timestamp text
#     """Return True if text has a timestamp of this format:
#        2014-07-03T23:30:37"""
#     r.. __.s.. _ \d{4}(-\d\d){2}T(\d\d:){2}\d\d ? __ n.. N..
#
#
# ___ is_integer number
#     """Return True if number is an integer"""
#     r.. __.m.. _ ^[-+]?\d+$ s.. ? __ n.. N..
#
#
# ___ has_word_with_dashes text
#     """Returns True if text has one or more words with dashes"""
#     r.. __.s.. _ \b(\w+-)+\w+\b ? __ n.. N..
#
#
# ___ remove_all_parenthesis_words text
#     """Return text but without any words or phrases in parenthesis:
#        'Good morning (afternoon)' -> 'Good morning' (so don't forget
#        leading spaces)"""
#     r.. __.s.. _  *\(.+?\) '' ?
#
#
# ___ split_string_on_punctuation text
#     """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
#        ['hi', 'how are you doing', 'blabla']
#        (make sure you strip trailing spaces)"""
#     r.. l.. f.. N.., __.s.. _ [?!.,;] * ?
#
#
# ___ remove_duplicate_spacingtext
#     """Replace multiple spaces by one space"""
#     r.. __.s.. _  + ' ' ?
#
#
# ___ has_three_consecutive_vowels word
#     """Returns True if word has at least 3 consecutive vowels"""
#     r.. __.s.. _ [aeiou]{3} ? __.I..
#
#
# ___ convert_emea_date_to_amer_date date
#     """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
#        (AMER date format)"""
#     r.. __.s.. _ (\d\d)/(\d\d)/(\d{4}) _ \2/\1/\3 s.. ?
