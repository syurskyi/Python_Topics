'''
Created on Mar 28, 2018

@author: tongq
'''
c_ Solution(o..
    ___ pourWater  heights, V, K
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        __ n.. heights: r.. heights
        idx 0
        w.... V > 0:
            idx K
            ___ i __ r..(K-1, -1, -1
                __ heights[i] > heights[idx]:
                    _____
                ____ heights[i] < heights[idx]:
                    idx i
            __ idx != K:
                heights[idx] += 1
                V -_ 1
                _____
            ___ i __ r..(K+1, l..(heights:
                __ heights[i] > heights[idx]:
                    _____
                ____ heights[i] < heights[idx]:
                    idx i
            heights[idx] += 1
            V -_ 1
        r.. heights
    
    ___ test
        testCases [
            [[2,1,1,2,1,2,2], 4, 3],
            [[1,2,3,4], 2, 2],
            [[3,1,3], 5, 1],
            [
                [1,2,3,4,3,2,1,2,3,4,3,2,1],
                5,
                5,
            ],
            [
                [1,2,3,4,3,2,1,2,3,4,3,2,1],
                10,
                2,
            ],
            [
                [1,2,3,4,3,2,1,2,3,4,3,2,1],
                5,
                2,
            ],
        ]
        ___ heights, v, k __ testCases:
            print('heights: %s' % heights)
            print('v: %s' % v)
            print('k: %s' % k)
            result pourWater(heights, v, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
