'''
Created on Oct 7, 2017

@author: MT
'''
c_ Solution(object):
    ___ findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        _______ bisect, heapq
        ind = bisect.bisect_left(arr, x)
        __ ind __ 0:
            r.. arr[:k]
        __ ind __ l..(arr):
            r.. arr[-k:]
        heap    # list
        ___ i __ r..(max(0, ind-k), m..(l..(arr), ind+k)):
            diff = abs(x-arr[i])
            heapq.heappush(heap, (diff, arr[i]))
        res    # list
        ___ _ __ r..(k):
            res.a..(heapq.heappop(heap)[1])
        r.. s..(res)
    
    ___ test
        testCases = [
            [
                [1, 2, 3, 4, 5],
                4,
                3,
            ],
            [
                [1, 2, 3, 4, 5],
                4,
                -1,
            ],
                     [
                [1, 2, 3, 4, 5],
                4,
                9,
            ],
        ]
        ___ arr, k, x __ testCases:
            print('arr: %s' % arr)
            print('k: %s' % k)
            print('x: %s' % x)
            result = findClosestElements(arr, k, x)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
