'''
Created on Oct 15, 2017

@author: MT
'''
c_ Solution(o..
    ___ findLengthOfLCIS  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums: r.. 0
        n = l..(nums)
        i = 0
        res = 1
        w.... i < n:
            j = i
            w.... i+1 < n a.. nums[i] < nums[i+1]:
                i += 1
                res = m..(res, i-j+1)
            i += 1
        r.. res
    
    ___ test
        testCases = [
            [1, 3, 5, 4, 7],
            [2, 2, 2, 2, 2],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = findLengthOfLCIS(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
