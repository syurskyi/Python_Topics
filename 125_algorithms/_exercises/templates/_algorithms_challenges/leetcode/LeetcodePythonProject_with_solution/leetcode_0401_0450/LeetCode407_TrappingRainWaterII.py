'''
Created on Apr 10, 2017

@author: MT
'''
c_ Solution(o..
    ___ trapRainWater  heightMap
        _______ h__
        __ n.. heightMap o. n.. heightMap[0]:
            r.. 0
        m, n l..(heightMap), l..(heightMap 0
        heap    # list
        visited [[F..]*n ___ _ __ r..(m)]
        ___ i __ r..(m
            ___ j __ r..(n
                __ i__0 o. j__0 o. i__m-1 o. j__n-1:
                    h__.heappush(heap, (heightMap[i][j], i, j
                    visited[i][j] T..
        res 0
        w.... heap:
            height, i, j h__.heappop(heap)
            ___ x, y __ (i+1, j), (i, j+1), (i-1, j), (i, j-1
                __ 0<_x<m a.. 0<_y<n a.. n.. visited[x][y]:
                    res += m..(0, height-heightMap[x][y])
                    h__.heappush(heap, (m..(height, heightMap[x][y]), x, y
                    visited[x][y] T..
        r.. res
    
    ___ test
        testCases [
            [
                [1,4,3,1,3,2],
                [3,2,1,3,2,4],
                [2,3,3,2,3,1],
            ],
        ]
        ___ heightMap __ testCases:
            print('heightMap:')
            print('\n'.j..([s..(row) ___ row __ heightMap]
            result trapRainWater(heightMap)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
