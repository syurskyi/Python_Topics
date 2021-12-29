'''
Created on Feb 16, 2017

@author: MT
'''

class Solution(object):
    ___ rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = l..(nums)
        k = k % length
        __ k __ 0: r..
        arr    # list
        ___ i0 __ r..(length):
            i = length + i0 - k __ i0<k ____ i0-k
            arr.a..(nums[i])
        ___ i __ r..(length):
            nums[i] = arr[i]
    
    ___ test(self):
        testCases = [
            ([1,2,3,4,5,6,7], 3),
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            self.rotate(nums, k)
            print('after: %s' % (nums))
            print('-='*20+'-')
        
__ __name__ __ '__main__':
    Solution().test()