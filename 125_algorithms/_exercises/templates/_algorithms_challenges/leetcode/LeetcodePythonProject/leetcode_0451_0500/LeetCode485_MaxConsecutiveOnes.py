'''
Created on May 3, 2017

@author: MT
'''

class Solution(object
    ___ findMaxConsecutiveOnes(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = -1
        maxLen = 0
        ___ i, num in enumerate(nums
            __ num __ 0:
                maxLen = max(maxLen, i-prev-1)
                prev = i
        maxLen = max(maxLen, le.(nums)-prev-1)
        r_ maxLen
    
    ___ test(self
        testCases = [
            [1],
            [],
            [1, 1, 0, 1, 1, 1],
            [1, 0, 1, 1, 0, 1],
        ]
        ___ nums in testCases:
            print('nums: %s' % nums)
            result = self.findMaxConsecutiveOnes(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
