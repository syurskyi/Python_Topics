from string ______ ascii_lowercase
from time ______ time
______ random


class Cipher(object

    ___ __init__(self, key=None
        __ not key:
            random.seed(time())
            key = ''.join(random.choice(ascii_lowercase) for i in range(100))
        ____ not key.isalpha() or not key.islower(
            raise ValueError('Wrong key parameter!')
        self.key = key

    ___ encode(self, text
        text = ''.join(c for c in text __ c.isalpha()).lower()
        key = self.key * (le.(text) // le.(self.key) + 1)
        r_ ''.join(chr((ord(c) - 194 + ord(k)) % 26 + 97)
                       for c, k in zip(text, key))

    ___ decode(self, text
        key = self.key * (le.(text) // le.(self.key) + 1)
        r_ ''.join(chr((ord(c) - ord(k) + 26) % 26 + 97)
                       for c, k in zip(text, key))


class Caesar(Cipher

    ___ __init__(self
        Cipher.__init__(self, 'd')
