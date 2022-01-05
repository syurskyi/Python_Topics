'''
Created on Apr 8, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ isIdealPermutation  A):
        """
        :type A: List[int]
        :rtype: bool
        """
        arr = A
        cmax = 0
        ___ i __ r..(l..(arr)-2):
            cmax = m..(cmax, arr[i])
            __ cmax > arr[i+2]:
                r.. F..
        r.. T..
    
    ___ test
        testCases = [
            [1,0,2],
            [1,2,0],
        ]
        ___ arr __ testCases:
            print('arr: %s' % arr)
            result = isIdealPermutation(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
