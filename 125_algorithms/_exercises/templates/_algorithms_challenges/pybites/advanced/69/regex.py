import re


___ has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""


    return re.search(r'\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}',text) is not None


___ is_integer(number):
    """Return True if number is an integer"""

    
    number = str(number)

    return re.search(r'^\-?\d+$',number) is not None





___ has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""


    return re.search(r'[a-zA-Z\d]+\-[a-zA-Z\d]+',text) is not None


___ remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""

    return re.sub(r'\s*\(.+?\)','',text)


___ split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""

    return [v for v in re.split(r'[?!.,;]\s*',text) __ v != '']


___ remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""


    return re.sub(r'\s{2,}',' ',text)


___ has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""

    return re.search(r'[aeiou]{3,}',word,flags=re.I)


___ convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""


    try:
        dates = re.findall(r"(\d\d)/(\d\d)/(\d{4})",date)[0]
    except:
        return date
    else:
        return '/'.join((dates[1],dates[0],dates[-1]))
