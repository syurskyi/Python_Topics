_______ re

___ capitalize_sentences(text: str) -> str:
    '''Returns sentence with correct capitalisation.'''
    ___ upper_it(m):
        r.. m.group().upper()
    text = text.strip().splitlines()
    r.. '\n'.join([re.sub(r'^\w', upper_it, line) ___ line __ text])