'''
Created on Apr 23, 2017

@author: MT
'''

c_ Solution(o..
    ___ find132pattern  nums
        s3 = f__('-inf')
        stack    # list
        ___ i __ r..(l..(nums)-1, -1, -1
            num = nums[i]
            __ num < s3:
                r.. T..
            w.... stack a.. stack[-1] < num:
                s3 = stack.p.. )
            stack.a..(num)
        r.. F..
    
    ___ test
        testCases = [
            [3, 1, 4, 2],
            [1, 2, 3, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums
            result = find132pattern(nums)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
