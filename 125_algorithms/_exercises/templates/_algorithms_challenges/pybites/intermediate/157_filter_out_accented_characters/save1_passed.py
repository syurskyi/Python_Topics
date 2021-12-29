import re

___ filter_accents(text):
    '''Return a list of accented characters in a text'''
    return sorted(list(set(re.findall(r'[\u00C0-\u00FF]', text.lower()))))