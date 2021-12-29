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
        l, r = 0, len(nums)-1
        while l < r:
            __ nums[l] < nums[r]:
                return nums[l]
            mid = (l+r)//2
            __ nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]
    
    ___ test(self):
        testCases = [
            [0, 1, 2, 4, 5, 6, 7],
            [4, 5, 6, 7, 0, 1, 2],
            [2, 1],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.findMin(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()