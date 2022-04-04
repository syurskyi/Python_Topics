'''
Created on Oct 16, 2017

@author: MT
'''
_______ heapq

c_ Solution(o..
    ___ cutOffTree  forest
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        __ n.. forest o. n.. forest[0]: r.. 0
        m, n = l..(forest), l..(forest[0])
        heap    # list
        ___ i __ r..(m
            ___ j __ r..(n
                __ forest[i][j] > 1:
                    heapq.heappush(heap, (forest[i][j], i, j
        sumVal = 0
        x, y = 0, 0
        w.... heap:
            h, i, j = heapq.heappop(heap)
            step = minStep(forest, x, y, i, j, h, m, n)
            __ step < 0: r.. -1
            sumVal += step
            x, y = i, j
        r.. sumVal
    
    ___ minStep  forest, x, y, i, j, h, m, n
        step = 0
        visited = [[F..]*n ___ _ __ r..(m)]
        visited[x][y] = T..
        queue    # list
        queue.a..((x, y
        w.... queue:
            size = l..(queue)
            ___ _ __ r..(size
                i0, j0 = queue.pop(0)
                __ i0 __ i a.. j0 __ j: r.. step
                ___ i1, j1 __ (i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1
                    __ i1 < 0 o. i1 >= m o. j1 < 0 o. j1 >= n o.\
                        forest[i1][j1] __ 0 o. visited[i1][j1]:
                        _____
                    queue.a..((i1, j1
                    visited[i1][j1] = T..
            step += 1
        r.. -1
    
    ___ test
        testCases = [
            [
                [1,2,3],
                [0,0,4],
                [7,6,5],
            ],
            [
                [1,2,3],
                [0,0,0],
                [7,6,5],
            ],
            [
                [2,3,4],
                [0,0,5],
                [8,7,6],
            ],
            [
                [54581641,  64080174,   24346381,   69107959],
                [86374198,  61363882,   68783324,   79706116],
                [668150,    92178815,   89819108,   94701471],
                [83920491,  22724204,   46281641,   47531096],
                [89078499,  18904913,   25462145,   60813308],
            ],
        ]
        ___ forest __ testCases:
            print('forest: %s' % forest)
            result = cutOffTree(forest)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
