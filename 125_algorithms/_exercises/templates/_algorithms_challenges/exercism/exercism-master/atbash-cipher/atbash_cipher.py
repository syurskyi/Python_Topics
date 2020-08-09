______ string


class Atbash:
    PLAIN = 'abcdefghijklmnopqrstuvwxyz'
    PRIME = 'zyxwvutsrqponmlkjihgfedcba'
    CIPHER = dict(zip(list(PLAIN), list(PRIME)))
    EXCLUDE = set(string.punctuation + ' ')

    @staticmethod
    ___ encode(self, msg
        r_ self.split_every_five(self, self.encoded(self, msg))

    @staticmethod
    ___ split_every_five(self, encoded
        r_ ' '.join([encoded[i:i + 5] ___ i in range(0, le.(encoded), 5)])

    @staticmethod
    ___ encoded(self, msg
        r_ ''.join(([char __ char.isdigit() else self.CIPHER[char]
                         ___ char in self.clean(self, msg)]))

    @staticmethod
    ___ clean(self, msg
        r_ (char ___ char in msg.lower() __ char not in self.EXCLUDE)

    @staticmethod
    ___ decode(self, msg
        r_ self.encoded(self, msg)


___ encode(msg
    r_ Atbash.encode(Atbash, msg)


___ decode(msg
    r_ Atbash.decode(Atbash, msg)
