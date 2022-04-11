'''
Created on Apr 17, 2018

@author: tongq
'''
c_ Solution(o..
    ___ numSubarrayBoundedMax  A, L, R
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        arr, l, r A, L, R
        res 0
        j 0
        count 0
        ___ i __ r..(l..(arr:
            __ l <_ arr[i] <_ r:
                res += i-j+1
                count i-j+1
            ____ arr[i] < l:
                res += count
            ____
                j i+1
                count 0
        r.. res
    
    ___ test
        testCases [
            [
                [2, 1, 4, 3],
                2, 3,
            ],
            [
                [73,55,36,5,55,14,9,7,72,52],
                32, 69,
            ],
            [
                [2,9,2,5,6],
                2, 8
            ],
        ]
        ___ arr, l, r __ testCases:
            result numSubarrayBoundedMax(arr, l, r)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
