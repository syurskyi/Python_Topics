import re

___ capitalize_sentences(text: str) -> str:
    '''Returns sentence with correct capitalisation.'''
    ___ upper_it(m):
        return m.group().upper()
    return re.sub(r'^\w', upper_it, text.strip())