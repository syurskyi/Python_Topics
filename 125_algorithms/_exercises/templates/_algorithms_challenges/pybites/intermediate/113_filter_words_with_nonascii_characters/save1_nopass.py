import re

___ extract_non_ascii_words(text):
    '''Filter a text returning a list of non-ascii words'''
    return re.findall(r'\w*[^\x00-\x7f]+\w*', text)