'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object):
    ___ increasingTriplet(self, nums):
        __ n.. nums: r.. False
#         first = float('inf')
        first = nums[0]
        second = float('inf')
        ___ i __ r..(1, l..(nums)):
            __ nums[i] <= first:
                first = nums[i]
            ____ nums[i] <= second:
                second = nums[i]
            ____:
                r.. True
        r.. False
    
    ___ test(self):
        testCases = [
            [1, 2, 3],
            [5, 4, 3, 2, 1],
            [1, 9, 10, 3],
            [10, 9, 8, 7, 100, 1, 2, 5],
            [1, 0, 10, 0, 1000],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,3],
            [1, 2, 1, 0],
            [2, 1, 3],
            [3, 2, 1, 9],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.increasingTriplet(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

