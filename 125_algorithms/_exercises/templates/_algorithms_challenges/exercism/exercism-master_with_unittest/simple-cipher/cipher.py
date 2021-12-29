import random
import string


class Cipher:

    random_key_length = 100

    ___ __init__(self, key_ N..
        self.key = key __ key is not None else self.generate_random_key()
        __ not self.valid_key():
            raise ValueError()

    ___ encode(self, phrase):
        return ''.join([chr(self.wrap(ord(c) + self.offset(i))) for i, c in
                        enumerate(self.clean(phrase))])

    ___ decode(self, phrase):
        return ''.join([chr(self.wrap(ord(c) - self.offset(i))) for i, c in
                        enumerate(self.clean(phrase))])

    ___ clean(self, phrase):
        return list(filter(str.isalpha, phrase.lower()))

    ___ generate_random_key(self):
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase)
                       for _ in range(self.random_key_length))

    ___ valid_key(self):
        return self.key.isalpha() and self.key.islower()

    ___ offset(self, index):
        return self.wrap(ord(self.key[index % len(self.key)]) - 97)

    ___ wrap(self, val):
        while val > 122:
            val -= 26
        while val < 97:
            val += 26
        return val


class Caesar:

    cipher = Cipher('d')

    @classmethod
    ___ encode(cls, phrase):
        return cls.cipher.encode(phrase)

    @classmethod
    ___ decode(cls, phrase):
        return cls.cipher.decode(phrase)
