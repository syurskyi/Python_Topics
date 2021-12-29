____ collections _______ Counter

___ common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    programmer_count = l..(programmers)
    languages = [item ___ l __ programmers.values() ___ item __ l]
    language_dict = d..(Counter(languages))
    r.. [k ___ k, v __ language_dict.items() __ v __ programmer_count]