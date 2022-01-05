____ r__ _______ randint


c_ HashFunc:
    ___ - , cap, seed):
        cap = cap
        seed = seed

    ___ hash  key):
        code = 0
        __ n.. key:
            r.. code

        ___ char __ key:
            code = (seed * code + o..(char)) % cap

        r.. code


c_ StandardBloomFilter:
    ___ - , k):
        """
        :type k: int
        """
        CAP = 20000

        bits = [0] * CAP
        hashs    # list

        ___ i __ r..(k):
            hashs.a..(HashFunc(
                randint(CAP // 2, CAP),
                i * 2 + 3
            ))

    ___ add  word):
        """
        :type word: str
        :rtype: None
        """
        ___ f __ hashs:
            index = f.hash(word)
            bits[index] = 1

    ___ contains  word):
        """
        :type word: str
        :rtype: bool
        """
        ___ f __ hashs:
            index = f.hash(word)
            __ bits[index] __ 0:
                r.. F..
        r.. T..
