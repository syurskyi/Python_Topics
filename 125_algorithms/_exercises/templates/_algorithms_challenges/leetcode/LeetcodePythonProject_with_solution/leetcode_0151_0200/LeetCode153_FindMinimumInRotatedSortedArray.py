'''
Created on Feb 11, 2017

@author: MT
'''

class Solution(object):
    ___ findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, l..(nums)-1
        while l < r:
            __ nums[l] < nums[r]:
                r.. nums[l]
            mid = (l+r)//2
            __ nums[mid] > nums[r]:
                l = mid+1
            ____:
                r = mid
        r.. nums[l]
    
    ___ test(self):
        testCases = [
            [0, 1, 2, 4, 5, 6, 7],
            [4, 5, 6, 7, 0, 1, 2],
            [2, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.findMin(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()