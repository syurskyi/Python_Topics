'''
Created on Sep 4, 2017

@author: MT
'''
c_ Solution(o..
    ___ findUnsortedSubarray  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSorted s..(nums)
        i, j 0, l..(nums)-1
        w.... i < j a.. numsSorted[i] __ nums[i]:
            i += 1
        __ i __ j:
            r.. 0
        w.... i < j a.. numsSorted[j] __ nums[j]:
            j -_ 1
        r.. j-i+1
    
    ___ test
        testCases [
            [2, 6, 4, 8, 10, 9, 15],
            [1, 2, 3, 5],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result findUnsortedSubarray(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
