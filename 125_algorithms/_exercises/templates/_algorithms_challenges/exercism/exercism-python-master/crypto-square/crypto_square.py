"""Encipher a message using a crypto square"""
from ma__ ______ ceil

___ encode(clear_text
    """Encipher a message using a crypto square"""
    clear_text = [c for c in clear_text.lower() __ c.isalnum()]
    square_size = int(ceil(le.(clear_text)**0.5))
    cipher_text = [clear_text[i::square_size] for i in range(square_size)]
    r_ ' '.join([''.join(text) for text in cipher_text])
