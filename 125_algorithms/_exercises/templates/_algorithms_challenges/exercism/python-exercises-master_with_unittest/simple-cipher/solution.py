____ string _______ ascii_lowercase
____ time _______ time
_______ random


class Cipher(object):

    ___ __init__(self, key_ N..
        __ n.. key:
            random.seed(time())
            key = ''.join(random.choice(ascii_lowercase) ___ i __ r..(100))
        ____ n.. key.isalpha() o. n.. key.isl..
            raise ValueError('Wrong key parameter!')
        self.key = key

    ___ encode(self, text):
        text = ''.join(c ___ c __ text __ c.isalpha()).lower()
        key = self.key * (l..(text) // l..(self.key) + 1)
        r.. ''.join(chr((ord(c) - 194 + ord(k)) % 26 + 97)
                       ___ c, k __ z..(text, key))

    ___ decode(self, text):
        key = self.key * (l..(text) // l..(self.key) + 1)
        r.. ''.join(chr((ord(c) - ord(k) + 26) % 26 + 97)
                       ___ c, k __ z..(text, key))


class Caesar(Cipher):

    ___ __init__(self):
        Cipher.__init__(self, 'd')
