______ string


___ _check(key
    __ key[0] not in string.digits:
        key = f'\1{key}'
    r_ key.lower()


___ sort_words_case_insensitively(words
    """Sort the provided word list ignoring case,
       one twist: numbers have to appear after letters!"""
    r_ sorted(words, key=_check)
