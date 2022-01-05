'''
Created on Apr 13, 2017

@author: MT
'''

c_ Solution(o..):
    ___ findMaximumXOR  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = 0
        mask = 0
        ___ i __ r..(32, -1, -1):
            mask = mask | (1<<i)
            hashset = set()
            ___ num __ nums:
                hashset.add(num&mask)
            tmp = maxVal | (1<<i)
            ___ prefix __ hashset:
                __ tmp ^ prefix __ hashset:
                    maxVal = tmp
                    _____
        r.. maxVal
