_______ string


c_ Atbash:
    PLAIN = 'abcdefghijklmnopqrstuvwxyz'
    PRIME = 'zyxwvutsrqponmlkjihgfedcba'
    CIPHER = d..(z..(l..(PLAIN), l..(PRIME)))
    EXCLUDE = set(string.punctuation + ' ')

    @staticmethod
    ___ encode(self, msg):
        r.. split_every_five(self, encoded(self, msg))

    @staticmethod
    ___ split_every_five(self, encoded):
        r.. ' '.j..([encoded[i:i + 5] ___ i __ r..(0, l..(encoded), 5)])

    @staticmethod
    ___ encoded(self, msg):
        r.. ''.j..(([char __ char.isdigit() ____ CIPHER[char]
                         ___ char __ clean(self, msg)]))

    @staticmethod
    ___ clean(self, msg):
        r.. (char ___ char __ msg.l.. __ char n.. __ EXCLUDE)

    @staticmethod
    ___ decode(self, msg):
        r.. encoded(self, msg)


___ encode(msg):
    r.. Atbash.encode(Atbash, msg)


___ decode(msg):
    r.. Atbash.decode(Atbash, msg)
