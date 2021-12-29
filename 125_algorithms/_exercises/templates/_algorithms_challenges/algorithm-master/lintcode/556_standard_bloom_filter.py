from random import randint


class HashFunc:
    ___ __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    ___ hash(self, key):
        code = 0
        __ not key:
            return code

        for char in key:
            code = (self.seed * code + ord(char)) % self.cap

        return code


class StandardBloomFilter:
    ___ __init__(self, k):
        """
        :type k: int
        """
        CAP = 20000

        self.bits = [0] * CAP
        self.hashs = []

        for i in range(k):
            self.hashs.append(HashFunc(
                randint(CAP // 2, CAP),
                i * 2 + 3
            ))

    ___ add(self, word):
        """
        :type word: str
        :rtype: None
        """
        for f in self.hashs:
            index = f.hash(word)
            self.bits[index] = 1

    ___ contains(self, word):
        """
        :type word: str
        :rtype: bool
        """
        for f in self.hashs:
            index = f.hash(word)
            __ self.bits[index] == 0:
                return False
        return True
