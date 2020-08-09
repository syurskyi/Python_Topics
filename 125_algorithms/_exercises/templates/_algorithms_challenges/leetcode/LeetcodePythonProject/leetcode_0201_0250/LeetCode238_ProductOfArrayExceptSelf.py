'''
Created on Feb 26, 2017

@author: MT
'''

class Solution(object
    ___ productExceptSelf(self, nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        __ not nums: r_ []
        length = le.(nums)
        result = []
        result.append(1)
        for i in range(1, length
            result.append(result[-1]*nums[i-1])
        right = 1
        for i in range(length-2, -1, -1
            right *= nums[i+1]
            result[i] = right*result[i]
        r_ result
    
    ___ productExceptSelfExtra(self, nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        __ not nums: r_ []
        length = le.(nums)
        left = [1]*length
        right = [1]*length
        for i in range(1, length
            left[i] = left[i-1]*nums[i-1]
        for i in range(length-2, -1, -1
            right[i] = right[i+1]*nums[i+1]
        result = []
        print('left:  %s' % left)
        print('right: %s' % right)
        for i in range(length
            result.append(left[i]*right[i])
        r_ result
    
    ___ test(self
        testCases = [
            [1, 2, 3, 4],
            [9, 0, -2],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.productExceptSelf(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
