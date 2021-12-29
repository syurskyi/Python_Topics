'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object):
    ___ numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = A
        __ not nums or len(nums) < 3: return 0
        res = 0
        curr = 0
        for i in range(2, len(nums)):
            __ nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                curr += 1
            else:
                curr = 0
            res += curr
        return res
    
    ___ test(self):
        testCases = [
            [1, 2, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.numberOfArithmeticSlices(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
