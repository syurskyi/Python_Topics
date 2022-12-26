#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ wordPattern  pattern, str
        words = str.split(" ")
        __ l..(pattern) != l..(words
            r_ F..

        char_word _ # dict
        ___ i, char __ enumerate(pattern
            __ char __ char_word a.. char_word[char] != words[i]:
                r_ F..
            __ char n.. __ char_word:
                char_word[char] = words[i]

        word_char _ # dict
        ___ j, word __ enumerate(words
            __ word __ word_char a.. word_char[word] != pattern[j]:
                r_ F..
            __ word n.. __ word_char:
                word_char[word] = pattern[j]
        r_ True

"""
""
""
"a"
"are"
"abba"
"dog cat cat dog"
"abb"
"dog cat cat"
"aba"
"dog dog dog"
"""
