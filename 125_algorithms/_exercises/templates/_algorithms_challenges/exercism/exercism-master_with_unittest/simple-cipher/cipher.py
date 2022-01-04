_______ random
_______ string


c_ Cipher:

    random_key_length = 100

    ___ - , key_ N..
        key = key __ key __ n.. N.. ____ generate_random_key()
        __ n.. valid_key
            r.. ValueError()

    ___ encode(self, phrase):
        r.. ''.j..([chr(wrap(ord(c) + offset(i))) ___ i, c __
                        e..(clean(phrase))])

    ___ decode(self, phrase):
        r.. ''.j..([chr(wrap(ord(c) - offset(i))) ___ i, c __
                        e..(clean(phrase))])

    ___ clean(self, phrase):
        r.. l..(filter(s...isalpha, phrase.lower()))

    ___ generate_random_key
        r.. ''.j..(random.SystemRandom().choice(string.ascii_lowercase)
                       ___ _ __ r..(random_key_length))

    ___ valid_key
        r.. key.isalpha() a.. key.islower()

    ___ offset(self, index):
        r.. wrap(ord(key[index % l..(key)]) - 97)

    ___ wrap(self, val):
        w.... val > 122:
            val -= 26
        w.... val < 97:
            val += 26
        r.. val


c_ Caesar:

    cipher = Cipher('d')

    @classmethod
    ___ encode(cls, phrase):
        r.. cls.cipher.encode(phrase)

    @classmethod
    ___ decode(cls, phrase):
        r.. cls.cipher.decode(phrase)
