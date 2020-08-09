'''
Created on Oct 16, 2017

@author: MT
'''
______ heapq

class Solution(object
    ___ cutOffTree(self, forest
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        __ not forest or not forest[0]: r_ 0
        m, n = le.(forest), le.(forest[0])
        heap = []
        ___ i in range(m
            ___ j in range(n
                __ forest[i][j] > 1:
                    heapq.heappush(heap, (forest[i][j], i, j))
        sumVal = 0
        x, y = 0, 0
        w___ heap:
            h, i, j = heapq.heappop(heap)
            step = self.minStep(forest, x, y, i, j, h, m, n)
            __ step < 0: r_ -1
            sumVal += step
            x, y = i, j
        r_ sumVal
    
    ___ minStep(self, forest, x, y, i, j, h, m, n
        step = 0
        visited = [[False]*n ___ _ in range(m)]
        visited[x][y] = True
        queue = []
        queue.append((x, y))
        w___ queue:
            size = le.(queue)
            ___ _ in range(size
                i0, j0 = queue.pop(0)
                __ i0 __ i and j0 __ j: r_ step
                ___ i1, j1 in (i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1
                    __ i1 < 0 or i1 >= m or j1 < 0 or j1 >= n or\
                        forest[i1][j1] __ 0 or visited[i1][j1]:
                        continue
                    queue.append((i1, j1))
                    visited[i1][j1] = True
            step += 1
        r_ -1
    
    ___ test(self
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
        ___ forest in testCases:
            print('forest: %s' % forest)
            result = self.cutOffTree(forest)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
