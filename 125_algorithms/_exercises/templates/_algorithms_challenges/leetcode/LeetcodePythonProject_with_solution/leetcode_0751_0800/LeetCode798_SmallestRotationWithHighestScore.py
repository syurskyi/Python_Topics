'''
Created on Apr 18, 2018

@author: tongq
'''
c_ Solution(o..
    ___ bestRotation  A
        """
        :type A: List[int]
        :rtype: int
        """
        arr A
        n l..(arr)
        change [1]*n
        ___ i __ r..(n
            change[(i-arr[i]+1)%n] -_ 1
        ___ i __ r..(1, n
            change[i] += change[i-1]
        r.. change.i.. m..(change
    
    # This EASY solution is TLE    
    ___ bestRotation_slow  A
        """
        :type A: List[int]
        :rtype: int
        """
        arr A
        idx, maxVal 0, f__ '-inf'
        ___ i __ r..(l..(arr:
            val getScore(arr, i)
            __ val > maxVal:
                maxVal val
                idx i
        r.. idx
    
    ___ getScore  arr, k
        res 0
        arr0 arr[k:]+arr[:k]
        ___ i, num __ e..(arr0
            __ num <_ i: res += 1
        r.. res
    
    ___ test
        testCases [
            [2, 3, 1, 4, 0],
            [1, 3, 0, 2, 4],
        ]
        ___ arr __ testCases:
            print('arr: %s' % arr)
            result bestRotation(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
