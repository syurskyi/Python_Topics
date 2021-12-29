'''
Created on Feb 26, 2017

@author: MT
'''

class Solution(object):
    ___ productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        __ n.. nums: r.. []
        length = l..(nums)
        result    # list
        result.a..(1)
        ___ i __ r..(1, length):
            result.a..(result[-1]*nums[i-1])
        right = 1
        ___ i __ r..(length-2, -1, -1):
            right *= nums[i+1]
            result[i] = right*result[i]
        r.. result
    
    ___ productExceptSelfExtra(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        __ n.. nums: r.. []
        length = l..(nums)
        left = [1]*length
        right = [1]*length
        ___ i __ r..(1, length):
            left[i] = left[i-1]*nums[i-1]
        ___ i __ r..(length-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        result    # list
        print('left:  %s' % left)
        print('right: %s' % right)
        ___ i __ r..(length):
            result.a..(left[i]*right[i])
        r.. result
    
    ___ test(self):
        testCases = [
            [1, 2, 3, 4],
            [9, 0, -2],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.productExceptSelf(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
