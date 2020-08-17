'''
Created on May 10, 2017

@author: MT
'''

class Solution(object
    ___ nextGreaterElements(self, nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = le.(nums)
        stack = list(range(n-1, -1, -1))
        ___ i in range(n-1, -1, -1
            w___ stack and nums[stack[-1]] <= nums[i]:
                stack.p..
            __ stack:
                res.insert(0, nums[stack[-1]])
            ____
                res.insert(0, -1)
            stack.append(i)
        r_ res
    
    ___ test(self
        testCases = [
#             [1, 2, 1],
            [1, 6, 2, 7, 4, 5],
        ]
        ___ nums in testCases:
            print('nums: %s' % nums)
            result = self.nextGreaterElements(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
