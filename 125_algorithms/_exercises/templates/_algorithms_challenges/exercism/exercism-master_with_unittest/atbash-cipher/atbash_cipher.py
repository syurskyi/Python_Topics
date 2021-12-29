_______ string


class Atbash:
    PLAIN = 'abcdefghijklmnopqrstuvwxyz'
    PRIME = 'zyxwvutsrqponmlkjihgfedcba'
    CIPHER = d..(zip(l..(PLAIN), l..(PRIME)))
    EXCLUDE = set(string.punctuation + ' ')

    @staticmethod
    ___ encode(self, msg):
        r.. self.split_every_five(self, self.encoded(self, msg))

    @staticmethod
    ___ split_every_five(self, encoded):
        r.. ' '.join([encoded[i:i + 5] ___ i __ r..(0, l..(encoded), 5)])

    @staticmethod
    ___ encoded(self, msg):
        r.. ''.join(([char __ char.isdigit() ____ self.CIPHER[char]
                         ___ char __ self.clean(self, msg)]))

    @staticmethod
    ___ clean(self, msg):
        r.. (char ___ char __ msg.lower() __ char n.. __ self.EXCLUDE)

    @staticmethod
    ___ decode(self, msg):
        r.. self.encoded(self, msg)


___ encode(msg):
    r.. Atbash.encode(Atbash, msg)


___ decode(msg):
    r.. Atbash.decode(Atbash, msg)
