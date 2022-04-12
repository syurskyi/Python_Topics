'''
Created on Feb 20, 2017

@author: MT
'''
c_ Solution(o..
    ___ getSkyline  buildings
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        _______ h__
        heights    # list
        ___ b __ buildings:
            heights.a..([b[0], -b[2]])
            heights.a..([b[1], b[2]])
        heights.s..()
        heap [0]
        res    # list
        prev 0
        ___ h __ heights:
            __ h[1] < 0:
                h__.heappush(heap, h[1])
            ____
                heap.remove(-h[1])
                h__.heapify(heap)
            curr -heap[0]
            __ curr !_ prev:
                res.a..([h[0], curr])
            prev curr
        r.. res
    
    ___ test
        testCases [
            [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ],
        ]
        ___ buildings __ testCases:
            print('buildings: %s' % (buildings
            result getSkyline(buildings)
            print('result: %s' % (result
            print('-='*20+'-')
    
__ _____ __ _____
    Solution().test()
