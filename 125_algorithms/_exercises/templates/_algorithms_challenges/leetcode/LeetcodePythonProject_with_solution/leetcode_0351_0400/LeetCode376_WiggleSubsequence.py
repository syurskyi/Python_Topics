'''
Created on Apr 1, 2017

@author: MT
'''

class Solution(object):
    ___ wiggleMaxLength(self, nums):
        __ n.. nums: r.. 0
        maxLen = 1
        i = 1
        while i < l..(nums):
            __ nums[i] > nums[i-1]:
                while i+1 < l..(nums) and nums[i] <= nums[i+1]:
                    i += 1
                maxLen += 1
            ____ nums[i-1] > nums[i]:
                while i+1 < l..(nums) and nums[i+1] <= nums[i]:
                    i += 1
                maxLen += 1
            i += 1
        r.. maxLen
    
    ___ test(self):
        testCases = [
            [1,7,4,9,2,5],
            [1,17,5,10,13,15,10,5,16,8],
            [1,2,3,4,5,6,7,8,9],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.wiggleMaxLength(nums)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
