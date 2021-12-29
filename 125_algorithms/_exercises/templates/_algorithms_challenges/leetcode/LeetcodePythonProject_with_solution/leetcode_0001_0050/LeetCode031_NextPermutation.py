'''
Created on Aug 28, 2017

@author: MT
'''

class Solution(object):
    ___ nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = l..(nums)-1
        while j > 0 and nums[j-1] >= nums[j]:
            j -= 1
        self.reverse(nums, j, l..(nums)-1)
        __ j __ 0:
            r..
        i = j-1
        while j+1 < l..(nums) and nums[i] >= nums[j]:
            j += 1
        nums[i], nums[j] = nums[j], nums[i]
    
    ___ reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    
    ___ test(self):
        testCases = [
            [1, 2, 3],
            [3, 2, 1],
            [1, 1, 5],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            self.nextPermutation(nums)
            print('nums: %s' % nums)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
