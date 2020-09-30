'''
Created on Apr 13, 2017

@author: MT
'''

class Solution(object
    ___ findMaximumXOR(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = 0
        mask = 0
        ___ i __ range(32, -1, -1
            mask = mask | (1<<i)
            hashset = set()
            ___ num __ nums:
                hashset.add(num&mask)
            tmp = maxVal | (1<<i)
            ___ prefix __ hashset:
                __ tmp ^ prefix __ hashset:
                    maxVal = tmp
                    break
        r_ maxVal
