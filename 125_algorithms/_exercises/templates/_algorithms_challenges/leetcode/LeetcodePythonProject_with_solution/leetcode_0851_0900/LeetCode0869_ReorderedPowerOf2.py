'''
Created on Sep 30, 2019

@author: tongq
'''
class Solution(object):
    ___ reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        n = N
        __ n __ 1: r.. True
        s = s..(n)
        length = l..(s)
        nums = self.getNums(length)
        ___ num __ nums:
            __ self.matches(n, num):
                r.. True
        r.. False
    
    ___ matches(self, n, num):
        hashmap = {}
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
                r.. False
        r.. True
    
    ___ getNums(self, length):
        res    # list
        num = 2
        w.... l..(s..(num)) < length:
            num *= 2
        w.... l..(s..(num)) __ length:
            res.a..(num)
            num *= 2
        r.. res
