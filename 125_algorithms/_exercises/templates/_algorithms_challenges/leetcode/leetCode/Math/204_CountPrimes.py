#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ countPrimes  n
        __ n <= 2:
            r_ 0
        count = 1
        # nums = [1 for i in range(n)]
        # Faster as follows
        nums = [1] * n

        ___ num __ r..(3, n, 2
            __ nums[num] __ 1:
                count += 1
                k = num
                _____ num * k < n:
                    nums[num*k] = 0
                    k += 1
            ____
                pass
        r_ count

    # Pythonic way, beats 98% submissions.
    ___ countPrimes_2  n
        __ n <= 2:
            r_ 0
        nums = [True] * n
        nums[:2] = [False] * 2
        nums[2:n:2] = [False] * ((n-1)/2)
        ___ i __ r..(3, int(n ** 0.5) + 1, 2
            __ nums[i]:
                nums[i*i:n:i] = [False] * ((n-i*i-1)/i+1)

        r_ s..(nums)+1

"""
0
120
9999
"""
