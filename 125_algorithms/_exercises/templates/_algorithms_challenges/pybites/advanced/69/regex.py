_______ __


___ has_timestamp(text
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""


    r.. __.s.. _ \d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}',text) __ n.. N..


___ is_integer(number
    """Return True if number is an integer"""

    
    number s.. ?

    r.. __.s.. _ ^\-?\d+$',number) __ n.. N..





___ has_word_with_dashes(text
    """Returns True if text has one or more words with dashes"""


    r.. __.s.. _ [a-zA-Z\d]+\-[a-zA-Z\d]+',text) __ n.. N..


___ remove_all_parenthesis_words(text
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""

    r.. __.s.. _ \s*\(.+?\)','',text)


___ split_string_on_punctuation(text
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""

    r.. [v ___ v __ __.s.. _ [?!.,;]\s*',text) __ v !_ '']


___ remove_duplicate_spacing(text
    """Replace multiple spaces by one space"""


    r.. __.s.. _ \s{2,}',' ',text)


___ has_three_consecutive_vowels(word
    """Returns True if word has at least 3 consecutive vowels"""

    r.. __.s.. _ [aeiou]{3,}',word,flags=__.I)


___ convert_emea_date_to_amer_date(date
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""


    ___
        dates __.f.. _ (\d\d)/(\d\d)/(\d{4})",date)[0]
    ______:
        r.. date
    ____
        r.. '/'.j..((dates[1],dates[0],dates[-1]
