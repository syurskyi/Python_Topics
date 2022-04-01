_______ s__


c_ Atbash:
    PLAIN = 'abcdefghijklmnopqrstuvwxyz'
    PRIME = 'zyxwvutsrqponmlkjihgfedcba'
    CIPHER = d..(z..(l..(PLAIN), l..(PRIME)))
    EXCLUDE = s..(s__.punctuation + ' ')

    @staticmethod
    ___ encode  msg):
        r.. split_every_five  encoded  msg))

    @staticmethod
    ___ split_every_five  encoded):
        r.. ' '.j..([encoded[i:i + 5] ___ i __ r..(0, l..(encoded), 5)])

    @staticmethod
    ___ encoded  msg):
        r.. ''.j..(([char __ char.i.. ____ CIPHER[char]
                         ___ char __ clean  msg)]))

    @staticmethod
    ___ clean  msg):
        r.. (char ___ char __ msg.l.. __ char n.. __ EXCLUDE)

    @staticmethod
    ___ decode  msg):
        r.. encoded  msg)


___ encode(msg):
    r.. Atbash.encode(Atbash, msg)


___ decode(msg):
    r.. Atbash.decode(Atbash, msg)
