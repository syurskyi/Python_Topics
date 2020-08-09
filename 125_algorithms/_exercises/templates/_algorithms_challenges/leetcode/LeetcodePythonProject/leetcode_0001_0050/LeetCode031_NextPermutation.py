'''
Created on Aug 28, 2017

@author: MT
'''

class Solution(object
    ___ nextPermutation(self, nums
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = le.(nums)-1
        w___ j > 0 and nums[j-1] >= nums[j]:
            j -= 1
        self.reverse(nums, j, le.(nums)-1)
        __ j __ 0:
            r_
        i = j-1
        w___ j+1 < le.(nums) and nums[i] >= nums[j]:
            j += 1
        nums[i], nums[j] = nums[j], nums[i]
    
    ___ reverse(self, nums, i, j
        w___ i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    
    ___ test(self
        testCases = [
            [1, 2, 3],
            [3, 2, 1],
            [1, 1, 5],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            self.nextPermutation(nums)
            print('nums: %s' % nums)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
