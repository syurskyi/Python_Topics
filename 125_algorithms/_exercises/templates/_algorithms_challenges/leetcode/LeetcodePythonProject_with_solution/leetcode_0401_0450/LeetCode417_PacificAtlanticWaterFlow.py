'''
Created on Apr 12, 2017

@author: MT
'''

c_ Solution(o..
    ___ pacificAtlantic  matrix
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        __ n.. matrix o. n.. matrix[0]: r.. []
        m, n = l..(matrix), l..(matrix[0])
        pacific = [[F..]*n ___ _ __ r..(m)]
        atlantic = [[F..]*n ___ _ __ r..(m)]
        ___ i __ r..(m
            dfs(matrix, i, 0, pacific)
            dfs(matrix, i, n-1, atlantic)
        ___ j __ r..(n
            dfs(matrix, 0, j, pacific)
            dfs(matrix, m-1, j, atlantic)
        result    # list
        ___ i __ r..(m
            ___ j __ r..(n
                __ pacific[i][j] a.. atlantic[i][j]:
                    result.a..([i, j])
        r.. result
    
    ___ dfs  matrix, i, j, visited
        visited[i][j] = T..
        m, n = l..(matrix), l..(matrix[0])
        ___ x, y __ (i+1, j), (i-1, j), (i, j+1), (i, j-1
            __ 0 <_ x < m a.. 0 <_ y < n a..\
                n.. visited[x][y] a.. matrix[x][y] >_ matrix[i][j]:
                dfs(matrix, x, y, visited)
