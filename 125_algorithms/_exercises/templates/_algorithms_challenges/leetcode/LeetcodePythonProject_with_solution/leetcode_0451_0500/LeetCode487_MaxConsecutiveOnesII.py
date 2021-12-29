'''
Created on May 8, 2017

@author: MT
'''

class Solution(object):
    ___ findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = -1
        nextLeft = -1
        maxLen = 0
        ___ i, num __ enumerate(nums):
            __ num __ 0:
                maxLen = max(maxLen, i-left-1)
                left = nextLeft
                nextLeft = i
        maxLen = max(maxLen, l..(nums)-left-1)
        r.. maxLen
    
    ___ test(self):
        testCases = [
            [1, 0, 1, 1, 0],
            [1, 0, 1, 1,0, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.findMaxConsecutiveOnes(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
