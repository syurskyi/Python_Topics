#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ getHint  secret, guess
        secret = list(secret)
        guess = list(guess)

        bulls, cows = 0, 0
        hash_secret _ # dict
        hash_guess _ # dict
        ___ i __ r..(l..(secret)):
            sec, gue = secret[i], guess[i]
            __ sec __ gue:
                bulls += 1
            ____
                hash_guess[gue] = hash_guess.get(gue, 0) + 1
                hash_secret[sec] = hash_secret.get(sec, 0) + 1
        ___ digit __ hash_secret:
            __ digit __ hash_guess:
                cows += min(hash_guess[digit], hash_secret[digit])
        r_ "".join([str(bulls), "A", str(cows), "B"])


"""
""
""
"1807"
"7810"
"1123"
"1111"
"1123"
"0111"
"""
