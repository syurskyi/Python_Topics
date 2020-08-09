'''
Created on Mar 5, 2017

@author: MT
'''

class Solution(object
    ___ wiggleSort(self, nums
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = le.(nums)
        ___ i in range(1, length
            __ i%2 __ 1 and nums[i-1] > nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            ____ i%2 __ 0 and nums[i-1] < nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
    
    ___ test(self
        testCases = [
            [3, 5, 2, 1, 6, 4],
        ]
        ___ nums in testCases:
            print('nums: %s' % (nums))
            self.wiggleSort(nums)
            print('after sort: %s' % (nums))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
