____ string _______ ascii_lowercase
____ time _______ time
_______ random


c_ Cipher(object):

    ___ - , key_ N..
        __ n.. key:
            random.seed(time())
            key = ''.j..(random.choice(ascii_lowercase) ___ i __ r..(100))
        ____ n.. key.isalpha() o. n.. key.isl..
            r.. ValueError('Wrong key parameter!')
        key = key

    ___ encode(self, text):
        text = ''.j..(c ___ c __ text __ c.isalpha()).l..
        key = key * (l..(text) // l..(key) + 1)
        r.. ''.j..(chr((ord(c) - 194 + ord(k)) % 26 + 97)
                       ___ c, k __ z..(text, key))

    ___ decode(self, text):
        key = key * (l..(text) // l..(key) + 1)
        r.. ''.j..(chr((ord(c) - ord(k) + 26) % 26 + 97)
                       ___ c, k __ z..(text, key))


c_ Caesar(Cipher):

    ___ - ):
        Cipher.- , 'd')
