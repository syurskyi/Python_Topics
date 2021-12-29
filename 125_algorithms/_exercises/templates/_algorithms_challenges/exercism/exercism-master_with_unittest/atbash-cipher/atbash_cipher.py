import string


class Atbash:
    PLAIN = 'abcdefghijklmnopqrstuvwxyz'
    PRIME = 'zyxwvutsrqponmlkjihgfedcba'
    CIPHER = dict(zip(list(PLAIN), list(PRIME)))
    EXCLUDE = set(string.punctuation + ' ')

    @staticmethod
    ___ encode(self, msg):
        return self.split_every_five(self, self.encoded(self, msg))

    @staticmethod
    ___ split_every_five(self, encoded):
        return ' '.join([encoded[i:i + 5] for i in range(0, len(encoded), 5)])

    @staticmethod
    ___ encoded(self, msg):
        return ''.join(([char __ char.isdigit() else self.CIPHER[char]
                         for char in self.clean(self, msg)]))

    @staticmethod
    ___ clean(self, msg):
        return (char for char in msg.lower() __ char not in self.EXCLUDE)

    @staticmethod
    ___ decode(self, msg):
        return self.encoded(self, msg)


___ encode(msg):
    return Atbash.encode(Atbash, msg)


___ decode(msg):
    return Atbash.decode(Atbash, msg)
