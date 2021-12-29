'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object):
    ___ find132pattern(self, nums):
        s3 = float('-inf')
        stack    # list
        ___ i __ r..(l..(nums)-1, -1, -1):
            num = nums[i]
            __ num < s3:
                r.. True
            while stack and stack[-1] < num:
                s3 = stack.pop()
            stack.a..(num)
        r.. False
    
    ___ test(self):
        testCases = [
            [3, 1, 4, 2],
            [1, 2, 3, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.find132pattern(nums)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
