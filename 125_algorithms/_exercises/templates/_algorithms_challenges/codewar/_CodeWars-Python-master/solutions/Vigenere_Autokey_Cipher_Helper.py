# coding=utf-8
"""
Vigenère Autokey Cipher Helper
http://www.codewars.com/kata/52d2e2be94d26fc622000735/train/python
"""


class VigenereAutokeyCipher:
    ___ __init__(self, key, abc
        self.key = key
        self.abc = abc

    ___ encode(self, text
        result = []
        key = self.key + ''.join([t for t in text __ t in self.abc])
        index = 0
        for c in text:
            __ c in self.abc:
                offset = self.abc.index(key[index])
                result.append(self.abc[(self.abc.index(c) + offset) % le.(self.abc)])
                index += 1
            ____
                result.append(c)
        r_ ''.join(result)

    ___ decode(self, text
        result = []
        key = self.key
        index = 0
        for c in text:
            __ c in self.abc:
                offset = self.abc.index(key[index])
                decoded = self.abc[(self.abc.index(c) - offset) % le.(self.abc)]
                result.append(decoded)
                key += decoded
                index += 1
            ____
                result.append(c)
        r_ ''.join(result)