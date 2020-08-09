from random ______ randint


class HashFunc:
    ___ __init__(self, cap, seed
        self.cap = cap
        self.seed = seed

    ___ hash(self, key
        code = 0
        __ not key:
            r_ code

        ___ char in key:
            code = (self.seed * code + ord(char)) % self.cap

        r_ code


class StandardBloomFilter:
    ___ __init__(self, k
        """
        :type k: int
        """
        CAP = 20000

        self.bits = [0] * CAP
        self.hashs = []

        ___ i in range(k
            self.hashs.append(HashFunc(
                randint(CAP // 2, CAP),
                i * 2 + 3
            ))

    ___ add(self, word
        """
        :type word: str
        :rtype: None
        """
        ___ f in self.hashs:
            index = f.hash(word)
            self.bits[index] = 1

    ___ contains(self, word
        """
        :type word: str
        :rtype: bool
        """
        ___ f in self.hashs:
            index = f.hash(word)
            __ self.bits[index] __ 0:
                r_ False
        r_ True
