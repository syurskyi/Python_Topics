# coding=utf-8
"""
Vigenère Autokey Cipher Helper
http://www.codewars.com/kata/52d2e2be94d26fc622000735/train/python
"""


class VigenereAutokeyCipher:
    ___ __init__(self, key, abc):
        self.key = key
        self.abc = abc

    ___ encode(self, text):
        result    # list
        key = self.key + ''.join([t ___ t __ text __ t __ self.abc])
        index = 0
        ___ c __ text:
            __ c __ self.abc:
                offset = self.abc.index(key[index])
                result.a..(self.abc[(self.abc.index(c) + offset) % l..(self.abc)])
                index += 1
            ____:
                result.a..(c)
        r.. ''.join(result)

    ___ decode(self, text):
        result    # list
        key = self.key
        index = 0
        ___ c __ text:
            __ c __ self.abc:
                offset = self.abc.index(key[index])
                decoded = self.abc[(self.abc.index(c) - offset) % l..(self.abc)]
                result.a..(decoded)
                key += decoded
                index += 1
            ____:
                result.a..(c)
        r.. ''.join(result)