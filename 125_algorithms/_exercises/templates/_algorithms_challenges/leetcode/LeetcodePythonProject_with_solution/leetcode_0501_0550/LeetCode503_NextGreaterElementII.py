'''
Created on May 10, 2017

@author: MT
'''

c_ Solution(o..
    ___ nextGreaterElements  nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res    # list
        n = l..(nums)
        stack = l..(r..(n-1, -1, -1))
        ___ i __ r..(n-1, -1, -1
            w.... stack a.. nums[stack[-1]] <= nums[i]:
                stack.pop()
            __ stack:
                res.insert(0, nums[stack[-1]])
            ____:
                res.insert(0, -1)
            stack.a..(i)
        r.. res
    
    ___ test
        testCases = [
#             [1, 2, 1],
            [1, 6, 2, 7, 4, 5],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = nextGreaterElements(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
