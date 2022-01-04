_______ __


___ has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    r.. bool(__.s..(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', text))


___ is_integer(number):
    """Return True if number is an integer"""
    r.. bool(__.s..(r'^[-+]?\d+$', s..(number)))


___ has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    r.. bool(__.s..(r'\w+-\w+', text))


___ remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    r.. __.sub(r' \([^)]*\) ', ' ', text)


___ split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    r.. l..(filter(N.., __.s..(r'\s?[?!\.,;]\s?', text)))


___ remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    r.. __.sub(r'\s{2,}', ' ', text)


___ has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    r.. bool(__.s..(r'[aeiou]{3,}', word))


___ convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    pattern = __.c..(r'(\d{2})/(\d{2})/(\d{4})')
    m = pattern.m..(date)
    r.. f'{m.group(2)}/{m.group(1)}/{m.group(3)}' __ m ____ m