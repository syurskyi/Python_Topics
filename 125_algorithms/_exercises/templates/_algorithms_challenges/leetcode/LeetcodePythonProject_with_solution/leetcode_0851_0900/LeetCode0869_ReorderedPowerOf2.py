'''
Created on Sep 30, 2019

@author: tongq
'''
c_ Solution(object):
    ___ reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        n = N
        __ n __ 1: r.. T..
        s = s..(n)
        length = l..(s)
        nums = getNums(length)
        ___ num __ nums:
            __ matches(n, num):
                r.. T..
        r.. F..
    
    ___ matches(self, n, num):
        hashmap    # dict
        ___ c __ s..(n):
            __ c __ hashmap:
                hashmap[c] += 1
            ____:
                hashmap[c] = 1
        ___ c __ s..(num):
            __ c __ hashmap:
                hashmap[c] -= 1
                __ hashmap[c] __ 0:
                    del hashmap[c]
            ____:
                r.. F..
        r.. T..
    
    ___ getNums(self, length):
        res    # list
        num = 2
        w.... l..(s..(num)) < length:
            num *= 2
        w.... l..(s..(num)) __ length:
            res.a..(num)
            num *= 2
        r.. res
