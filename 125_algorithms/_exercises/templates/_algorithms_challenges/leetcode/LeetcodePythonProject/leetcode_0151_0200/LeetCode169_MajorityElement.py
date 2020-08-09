'''
Created on Feb 13, 2017

@author: MT
'''

class Solution(object
    ___ majorityElement(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        count, cand = 0, -1
        ___ num in nums:
            __ cand __ num:
                count += 1
            ____ count __ 0:
                cand, count = num, 1
            ____
                count -= 1
        r_ cand
    
    ___ test(self
        testCases = [
            [1, 2, 2, 3, 2],
            [5, 1, 1, 1, 3],
            [1, 1, 1, 3],
        ]
        ___ nums in testCases:
            print('nums: %s' % (nums))
            result = self.majorityElement(nums)
            print('result: %s' % (result))
            print('-='*20 + '-')

__ __name__ __ '__main__':
    Solution().test()