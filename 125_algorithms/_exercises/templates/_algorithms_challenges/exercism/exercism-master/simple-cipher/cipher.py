______ random
______ string


class Cipher:

    random_key_length = 100

    ___ __init__(self, key=None
        self.key = key __ key is not None else self.generate_random_key()
        __ not self.valid_key(
            raise ValueError()

    ___ encode(self, phrase
        r_ ''.join([chr(self.wrap(ord(c) + self.offset(i))) for i, c in
                        enumerate(self.clean(phrase))])

    ___ decode(self, phrase
        r_ ''.join([chr(self.wrap(ord(c) - self.offset(i))) for i, c in
                        enumerate(self.clean(phrase))])

    ___ clean(self, phrase
        r_ list(filter(str.isalpha, phrase.lower()))

    ___ generate_random_key(self
        r_ ''.join(random.SystemRandom().choice(string.ascii_lowercase)
                       for _ in range(self.random_key_length))

    ___ valid_key(self
        r_ self.key.isalpha() and self.key.islower()

    ___ offset(self, index
        r_ self.wrap(ord(self.key[index % le.(self.key)]) - 97)

    ___ wrap(self, val
        w___ val > 122:
            val -= 26
        w___ val < 97:
            val += 26
        r_ val


class Caesar:

    cipher = Cipher('d')

    @classmethod
    ___ encode(cls, phrase
        r_ cls.cipher.encode(phrase)

    @classmethod
    ___ decode(cls, phrase
        r_ cls.cipher.decode(phrase)
