'''
Created on Oct 15, 2017

@author: MT
'''
class Solution(object
    ___ findLengthOfLCIS(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums: r_ 0
        n = le.(nums)
        i = 0
        res = 1
        w___ i < n:
            j = i
            w___ i+1 < n and nums[i] < nums[i+1]:
                i += 1
                res = max(res, i-j+1)
            i += 1
        r_ res
    
    ___ test(self
        testCases = [
            [1, 3, 5, 4, 7],
            [2, 2, 2, 2, 2],
        ]
        ___ nums in testCases:
            print('nums: %s' % nums)
            result = self.findLengthOfLCIS(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
