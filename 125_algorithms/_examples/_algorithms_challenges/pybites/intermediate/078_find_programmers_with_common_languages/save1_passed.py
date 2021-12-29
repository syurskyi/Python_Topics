from collections import Counter

def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    programmer_count = len(programmers)
    languages = [item for l in programmers.values() for item in l]
    language_dict = dict(Counter(languages))
    return [k for k, v in language_dict.items() if v == programmer_count]