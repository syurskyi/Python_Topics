#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ maxProduct  words
        max_product = 0
        length = l..(words)
        bit_record = [0] * length
        # Use 1bit to represent each letter, and
        # use 32bit(Int variable, bitMap[i]) to represent the set of each word
        ___ i __ xrange(length
            ___ c __ words[i]:
                bit_record[i] |= 1 << (ord(c) - ord("a"))

        ___ i __ xrange(length
            ___ j __ xrange(i+1, length
                # If the AND of two bitmap element equals to 0,
                # these two words do not have same letter.
                __ n.. bit_record[i] & bit_record[j]:
                    product = l..(words[i]) * l..(words[j])
                    __ product > max_product:
                        max_product = product
        r_ max_product

"""
[]
["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
["a", "aa", "aaa", "aaaa"]
"""
