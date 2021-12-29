_______ re

___ capitalize_sentences(text: str) -> str:
    '''Returns sentence with correct capitalisation.'''
    ___ upper_it(m):
        r.. m.group().upper()
    r.. re.sub(r'^\w', upper_it, text.strip())