_______ r__
_______ s__


c_ Cipher:

    random_key_length = 100

    ___ - , key_ N..
        key = key __ key __ n.. N.. ____ generate_random_key()
        __ n.. valid_key
            r.. ValueError()

    ___ encode  phrase
        r.. ''.j..([chr(wrap(o..(c) + offset(i))) ___ i, c __
                        e..(clean(phrase))])

    ___ decode  phrase
        r.. ''.j..([chr(wrap(o..(c) - offset(i))) ___ i, c __
                        e..(clean(phrase))])

    ___ clean  phrase
        r.. l..(filter(s...isalpha, phrase.lower()))

    ___ generate_random_key
        r.. ''.j..(r__.SystemRandom().choice(s__.ascii_lowercase)
                       ___ _ __ r..(random_key_length))

    ___ valid_key
        r.. key.isalpha() a.. key.islower()

    ___ offset  index
        r.. wrap(o..(key[index % l..(key)]) - 97)

    ___ wrap  val
        w.... val > 122:
            val -= 26
        w.... val < 97:
            val += 26
        r.. val


c_ Caesar:

    cipher = Cipher('d')

    @classmethod
    ___ encode(cls, phrase
        r.. cls.cipher.encode(phrase)

    @classmethod
    ___ d.. cls, phrase
        r.. cls.cipher.d.. phrase)
