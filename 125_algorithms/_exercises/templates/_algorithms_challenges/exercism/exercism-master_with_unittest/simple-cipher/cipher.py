_______ random
_______ string


class Cipher:

    random_key_length = 100

    ___ __init__(self, key_ N..
        self.key = key __ key __ n.. N.. ____ self.generate_random_key()
        __ n.. self.valid_key():
            raise ValueError()

    ___ encode(self, phrase):
        r.. ''.join([chr(self.wrap(ord(c) + self.offset(i))) ___ i, c __
                        enumerate(self.clean(phrase))])

    ___ decode(self, phrase):
        r.. ''.join([chr(self.wrap(ord(c) - self.offset(i))) ___ i, c __
                        enumerate(self.clean(phrase))])

    ___ clean(self, phrase):
        r.. l..(filter(str.isalpha, phrase.lower()))

    ___ generate_random_key(self):
        r.. ''.join(random.SystemRandom().choice(string.ascii_lowercase)
                       ___ _ __ r..(self.random_key_length))

    ___ valid_key(self):
        r.. self.key.isalpha() and self.key.islower()

    ___ offset(self, index):
        r.. self.wrap(ord(self.key[index % l..(self.key)]) - 97)

    ___ wrap(self, val):
        while val > 122:
            val -= 26
        while val < 97:
            val += 26
        r.. val


class Caesar:

    cipher = Cipher('d')

    @classmethod
    ___ encode(cls, phrase):
        r.. cls.cipher.encode(phrase)

    @classmethod
    ___ decode(cls, phrase):
        r.. cls.cipher.decode(phrase)
