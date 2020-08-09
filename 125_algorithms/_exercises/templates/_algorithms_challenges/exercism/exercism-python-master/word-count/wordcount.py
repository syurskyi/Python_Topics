"""Catalogs and counts the number of words used in a phrase"""
from collections ______ Counter
______ re

___ word_count(phrase
    """Returns dictionary with a count of words used"""
    r_ Counter(word ___ word in
        re.split(r'[\W_]+',
                 phrase.lower(), flags=re.UNICODE)
        __ word)
