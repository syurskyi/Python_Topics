'''
Created on Sep 10, 2017

@author: MT
'''

c_ Solution(o..
    ___ maxDistance  arrays
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        __ n.. arrays:
            r.. 0
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]
        maxDis = 0
        ___ i __ r..(1, l..(arrays:
            arr = arrays[i]
            maxDis = m..(maxDis, abs(arr[-1]-minVal
            maxDis = m..(maxDis, abs(maxVal-arr[0]
            minVal = m..(minVal, arr[0])
            maxVal = m..(maxVal, arr[-1])
        r.. maxDis
    
    ___ test
        testCases = [
            [
                [1,2,3],
                [4,5],
                [1,2,3]
            ],
        ]
        ___ arrays __ testCases:
            print('arrays: %s' % arrays)
            result = maxDistance(arrays)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
