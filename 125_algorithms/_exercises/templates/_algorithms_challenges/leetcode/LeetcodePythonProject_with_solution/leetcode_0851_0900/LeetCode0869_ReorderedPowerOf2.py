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
        __ n == 1: return True
        s = str(n)
        length = len(s)
        nums = self.getNums(length)
        for num in nums:
            __ self.matches(n, num):
                return True
        return False
    
    ___ matches(self, n, num):
        hashmap = {}
        for c in str(n):
            __ c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        for c in str(num):
            __ c in hashmap:
                hashmap[c] -= 1
                __ hashmap[c] == 0:
                    del hashmap[c]
            else:
                return False
        return True
    
    ___ getNums(self, length):
        res = []
        num = 2
        while len(str(num)) < length:
            num *= 2
        while len(str(num)) == length:
            res.append(num)
            num *= 2
        return res
