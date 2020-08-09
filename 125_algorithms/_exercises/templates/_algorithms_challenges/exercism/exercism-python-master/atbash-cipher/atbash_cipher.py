"""Encodes and decodes text using the atbash cipher"""
from re ______ sub

___ decode(cipher_text
    """Decodes atbash cipher text"""
    clear_text = ''
    for char in cipher_gen(cipher_text
        clear_text += char
    r_ clear_text

___ encode(clear_text
    """Encodes atbash cipher text,
    spaces added after every 5 characters to hide word boundaries"""
    cipher_text = ''
    for num, char in enumerate(cipher_gen(clear_text), 1
        cipher_text += char
        __ num % 5 __ 0:
            cipher_text += ' '
    # Removes possiable trailing space
    r_ cipher_text.strip()

___ cipher_gen(text
    """Strips whitespace and punctuation, converts to lower case,
    and translates a->z, b->y, ... z->a"""
    text = sub(r'\W', '', text)
    # ASCII codes for a-z are 97-122
    # Function to covert a->z is y = -x + (97 + 122)
    atbash = lambda c: chr(-ord(c) + 219)
    for char in text.lower(
        # Skips digits
        __ char in '1234567890':
            yield char
        ____
            yield atbash(char)
