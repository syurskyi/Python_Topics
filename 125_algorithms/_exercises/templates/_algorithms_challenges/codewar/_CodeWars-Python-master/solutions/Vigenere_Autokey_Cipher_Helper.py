# coding=utf-8
"""
Vigenère Autokey Cipher Helper
http://www.codewars.com/kata/52d2e2be94d26fc622000735/train/python
"""


c_ VigenereAutokeyCipher:
    ___ - , key, abc
        key = key
        abc = abc

    ___ encode  text
        result    # list
        key = key + ''.j..([t ___ t __ text __ t __ abc])
        index = 0
        ___ c __ text:
            __ c __ abc:
                offset = abc.i.. key[index])
                result.a..(abc[(abc.i.. c) + offset) % l..(abc)])
                index += 1
            ____
                result.a..(c)
        r.. ''.j..(result)

    ___ decode  text
        result    # list
        key = key
        index = 0
        ___ c __ text:
            __ c __ abc:
                offset = abc.i.. key[index])
                decoded = abc[(abc.i.. c) - offset) % l..(abc)]
                result.a..(decoded)
                key += decoded
                index += 1
            ____
                result.a..(c)
        r.. ''.j..(result)