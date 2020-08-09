'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object
    ___ find132pattern(self, nums
        s3 = float('-inf')
        stack = []
        for i in range(le.(nums)-1, -1, -1
            num = nums[i]
            __ num < s3:
                r_ True
            w___ stack and stack[-1] < num:
                s3 = stack.pop()
            stack.append(num)
        r_ False
    
    ___ test(self
        testCases = [
            [3, 1, 4, 2],
            [1, 2, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.find132pattern(nums)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
