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
        ___ i, num __ enumerate(nums
            __ num __ 0:
                maxLen = ma.(maxLen, i-prev-1)
                prev = i
        maxLen = ma.(maxLen, le.(nums)-prev-1)
        r_ maxLen
    
    ___ test(self
        testCases = [
            [1],
              # list,
            [1, 1, 0, 1, 1, 1],
            [1, 0, 1, 1, 0, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.findMaxConsecutiveOnes(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
