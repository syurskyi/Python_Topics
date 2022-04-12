'''
Created on Mar 21, 2018

@author: tongq
'''
c_ Solution(o..
    ___ networkDelayTime  times, N, K
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        _______ h__
        p..    # dict
        ___ t__ __ times:
            sourceMap p...g.. t__[0], {})
            __ t__[1] n.. __ sourceMap o. sourceMap[t__[1]] > t__[2]:
                sourceMap[t__[1]] t__[2]
            p..[t__[0]] sourceMap
        
        distanceMap {K:0}
        heap    # list
        h__.heappush(heap, [0, K])
        maxVal -1
        w.... heap:
            d, node h__.heappop(heap)
            __ node __ distanceMap a.. distanceMap[node] < d:
                _____
            __ node __ p..:
                ___ node0 __ p..[node]:
                    absDist d+p..[node][node0]
                    __ node0 __ distanceMap a.. distanceMap[node0] <_ absDist:
                        _____
                    distanceMap[node0] absDist
                    h__.heappush(heap, [absDist, node0])
        ___ val __ distanceMap.v..
            __ val > maxVal:
                maxVal val
        r.. maxVal __ l..(distanceMap) __ N ____ -1
    
    ___ test
        testCases [
            [
                [[2,1,1],[2,3,1],[3,4,1]],
                4,
                2,
            ],
            [
                [[1,2,1],[2,3,2],[1,3,4]],
                3,
                1,
            ],
        ]
        ___ times, N, K __ testCases:
            result networkDelayTime(times, N, K)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
