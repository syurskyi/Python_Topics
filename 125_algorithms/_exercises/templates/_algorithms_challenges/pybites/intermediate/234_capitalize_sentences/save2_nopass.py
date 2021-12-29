import re

___ capitalize_sentences(text: str) -> str:
    '''Returns sentence with correct capitalisation.'''
    ___ upper_it(m):
        return m.group().upper()
    text = text.strip().splitlines()
    return ' '.join([re.sub(r'^\w', upper_it, line) for line in text])