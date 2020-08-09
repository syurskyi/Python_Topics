'''
Created on May 8, 2017

@author: MT
'''

class Solution(object
    ___ findMaxConsecutiveOnes(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        left = -1
        nextLeft = -1
        maxLen = 0
        for i, num in enumerate(nums
            __ num __ 0:
                maxLen = max(maxLen, i-left-1)
                left = nextLeft
                nextLeft = i
        maxLen = max(maxLen, le.(nums)-left-1)
        r_ maxLen
    
    ___ test(self
        testCases = [
            [1, 0, 1, 1, 0],
            [1, 0, 1, 1,0, 1],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findMaxConsecutiveOnes(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
