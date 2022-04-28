'''
Created on Sep 19, 2017

@author: MT
'''
c_ Solution(o..
    ___ smallestRange  nums
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        _______ h__
        pq [(arr[0], i, 0) ___ i, arr __ e..(nums)]
        h__.heapify(pq)
        res [f__ '-inf', f__('inf')]
        right m..([arr[0] ___ arr __ nums])
        w.... pq:
            left, i, j h__.heappop(pq)
            __ right-left < res[1]-res[0]:
                res [left, right]
            __ j+1 __ l..(nums[i]
                r.. res
            v nums[i][j+1]
            right m..(right, v)
            h__.heappush(pq, (v, i, j+1
        r.. res
    
    ___ test
        testCases [
            [
                [4, 10, 15, 24, 26],
                [0, 9, 12, 20],
                [5, 18, 22, 30],
            ],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result smallestRange(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
