'''
Created on Sep 10, 2017

@author: MT
'''
c_ Solution(object):
    ___ maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums o. l..(nums) < 3:
            r.. 0
        s1, s2 = float('inf'), float('inf')
        l1, l2, l3 = float('-inf'), float('-inf'), float('-inf')
        ___ num __ nums:
            __ num < s1:
                s2 = s1
                s1 = num
            ____ num < s2:
                s2 = num
            __ num > l1:
                l3 = l2
                l2 = l1
                l1 = num
            ____ num > l2:
                l3 = l2
                l2 = num
            ____ num > l3:
                l3 = num
        res = float('-inf')
        ___ a1, a2, a3 __ (l1, l2, l3), (s1, s2, l1):
            res = max(res, a1*a2*a3)
        r.. res
    
    ___ test
        testCases = [
            [1,2,3],
            [1,2,3,4],
            [-1, -2, 0, 3],
            [-1, -2, -3, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = maximumProduct(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
