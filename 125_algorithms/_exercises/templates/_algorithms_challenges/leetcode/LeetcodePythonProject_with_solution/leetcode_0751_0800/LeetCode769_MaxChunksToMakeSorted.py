'''
Created on Apr 4, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ maxChunksToSorted  arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = l..(arr)
        maxOfLeft = [0]*n
        minOfRight = [0]*n
        maxOfLeft[0] = arr[0]
        ___ i __ r..(1, n):
            maxOfLeft[i] = m..(maxOfLeft[i-1], arr[i])
        minOfRight[-1] = arr[-1]
        ___ i __ r..(n-2, -1, -1):
            minOfRight[i] = m..(minOfRight[i+1], arr[i])
        res = 0
        ___ i __ r..(n-1):
            __ maxOfLeft[i] <= minOfRight[i+1]:
                res += 1
        r.. res+1
    
    ___ test
        testCases = [
            [4,3,2,1,0],
            [1,0,2,3,4],
            [0,2,1,4,3],
        ]
        ___ arr __ testCases:
            print('arr: %s' % arr)
            result = maxChunksToSorted(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
