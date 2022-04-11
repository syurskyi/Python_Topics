'''
Created on Apr 12, 2018

@author: tongq
'''
c_ Solution(o..
    ___ findCheapestPrice  n, flights, src, dst, K
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        _______ heapq
        graph    # dict
        ___ f __ flights:
            __ f[0] n.. __ graph:
                graph[f[0]] [[f[2], f[1]]]
            ____
                graph[f[0]].a..([f[2], f[1]])
        pq [[0, K+1, src]]
        w.... pq:
            size l..(pq)
            ___ _ __ r..(size
                curLen, level, node heapq.heappop(pq)
                __ node __ dst:
                    r.. curLen
                __ level > 0:
                    ___ dist, node0 __ graph.g.. node, []
                        heapq.heappush(pq, [curLen+dist, level-1, node0])
        r.. -1
    
    ___ test
        testCases [
            [3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1],
            [3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0],
            [4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1],
            [4, [[0,3,59],[2,0,83],[2,3,32],[0,2,97],[3,1,16],[1,3,16]], 3, 0, 3],
            [5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0, 2, 2],
        ]
        ___ n, flights, src, dst, k __ testCases:
            result findCheapestPrice(n, flights, src, dst, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
