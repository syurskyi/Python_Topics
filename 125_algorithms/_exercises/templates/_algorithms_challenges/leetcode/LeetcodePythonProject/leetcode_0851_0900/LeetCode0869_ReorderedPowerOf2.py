'''
Created on Sep 30, 2019

@author: tongq
'''
class Solution(object
    ___ reorderedPowerOf2(self, N
        """
        :type N: int
        :rtype: bool
        """
        n = N
        __ n __ 1: r_ True
        s = str(n)
        length = le.(s)
        nums = self.getNums(length)
        ___ num __ nums:
            __ self.matches(n, num
                r_ True
        r_ False
    
    ___ matches(self, n, num
        hashmap = {}
        ___ c __ str(n
            __ c __ hashmap:
                hashmap[c] += 1
            ____
                hashmap[c] = 1
        ___ c __ str(num
            __ c __ hashmap:
                hashmap[c] -= 1
                __ hashmap[c] __ 0:
                    del hashmap[c]
            ____
                r_ False
        r_ True
    
    ___ getNums(self, length
        res =   # list
        num = 2
        w___ le.(str(num)) < length:
            num *= 2
        w___ le.(str(num)) __ length:
            res.append(num)
            num *= 2
        r_ res
