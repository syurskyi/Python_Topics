'''
Created on Sep 10, 2019

@author: tongq
'''
c_ Solution(object):
    ___ peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        l, r = 0, l..(arr)-1
        w.... l < r:
            m = (l+r)//2
            __ arr[m] < arr[m+1]:
                l = m+1
            ____:
                r = m
        r.. l
    
    ___ peakIndexInMountainArray_On(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        res = -1
        val = float('-inf')
        ___ i, num __ e..(arr):
            __ num > val:
                res = i
            val = max(val, num)
        r.. res
    
    ___ test
        testCases = [
            [0,1,0],
            [0,2,1,0],
        ]
        ___ a __ testCases:
            res = peakIndexInMountainArray(a)
            print('result: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
