____ s__ _______ ascii_lowercase
____ time _______ time
_______ r__


c_ Cipher(o..

    ___ - , key_ N..
        __ n.. key:
            r__.seed(time())
            key = ''.j..(r__.choice(ascii_lowercase) ___ i __ r..(100))
        ____ n.. key.isalpha() o. n.. key.isl..
            r.. ValueError('Wrong key parameter!')
        key = key

    ___ encode  text
        text = ''.j..(c ___ c __ text __ c.isalpha()).l..
        key = key * (l..(text) // l..(key) + 1)
        r.. ''.j..(chr((o..(c) - 194 + o..(k)) % 26 + 97)
                       ___ c, k __ z..(text, key))

    ___ decode  text
        key = key * (l..(text) // l..(key) + 1)
        r.. ''.j..(chr((o..(c) - o..(k) + 26) % 26 + 97)
                       ___ c, k __ z..(text, key))


c_ Caesar(Cipher

    ___ -
        Cipher.- , 'd')
