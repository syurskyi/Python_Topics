import re

def capitalize_sentences(text: str) -> str:
    '''Returns sentence with correct capitalisation.'''
    def upper_it(m):
        return m.group().upper()
    text = text.strip().splitlines()
    return '\n'.join([re.sub(r'^\w', upper_it, line) for line in text])