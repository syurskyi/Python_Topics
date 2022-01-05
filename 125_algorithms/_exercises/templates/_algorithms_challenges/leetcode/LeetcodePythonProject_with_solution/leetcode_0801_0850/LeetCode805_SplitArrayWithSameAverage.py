'''
Created on Apr 24, 2018

@author: tongq
'''
c_ Solution(object):
    ___ splitArraySameAverage  A):
        """
        :type A: List[int]
        :rtype: bool
        """
        arr = A
        __ l..(arr) __ 1: r.. F..
        sumA = 0
        ___ num __ arr:
            sumA += num
        arr.s..()
        ___ lenOfB __ r..(1, l..(arr)//2+1):
            __ (sumA*lenOfB)%l..(arr) __ 0:
                __ check(arr, (sumA*lenOfB)/l..(arr), lenOfB, 0):
                    r.. T..
        r.. F..
    
    ___ check  arr, leftSum, leftNum, startIdx):
        __ leftNum __ 0: r.. leftSum __ 0
        __ arr[startIdx] > leftSum/leftNum:
            r.. F..
        ___ i __ r..(startIdx, l..(arr)-leftNum+1):
            __ i > startIdx a.. arr[i] __ arr[i-1]:
                _____
            __ check(arr, leftSum-arr[i], leftNum-1, i+1):
                r.. T..
        r.. F..
    
    ___ test
        testCases = [
            [1,2,3,4,5,6,7,8],
            [11,1,15,2,14,16,8,9,4],
            [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5],
        ]
        ___ arr __ testCases:
            print('arr: %s' % arr)
            result = splitArraySameAverage(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

