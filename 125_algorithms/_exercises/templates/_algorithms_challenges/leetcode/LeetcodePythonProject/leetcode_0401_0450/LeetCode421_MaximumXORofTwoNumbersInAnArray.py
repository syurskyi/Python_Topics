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
        for i in range(32, -1, -1
            mask = mask | (1<<i)
            hashset = set()
            for num in nums:
                hashset.add(num&mask)
            tmp = maxVal | (1<<i)
            for prefix in hashset:
                __ tmp ^ prefix in hashset:
                    maxVal = tmp
                    break
        r_ maxVal
