'''
Created on Oct 22, 2019

@author: tongq
'''
c_ Solution(o..
    ___ possibleBipartition  N, dislikes
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph [[F..]*N ___ _ __ r..(N)]
        ___ d __ dislikes:
            graph[d[0]-1][d[1]-1] T..
            graph[d[1]-1][d[0]-1] T..
        group [0]*N
        ___ i __ r..(N
            __ group[i] __ 0 a.. n.. dfs(graph, group, i, 1, N
                r.. F..
        r.. T..
    
    ___ dfs  graph, group, idx, g, N
        group[idx] g
        ___ i __ r..(N
            __ graph[idx][i] __ 1:
                __ group[i] __ g:
                    r.. F..
                __ group[i] __ 0 a.. n.. dfs(graph, group, i, -g, N
                    r.. F..
        r.. T..
    
    ___ possibleBipartition_own_TLE  N, dislikes
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        hashmap    # dict
        ___ num __ r..(1, N+1
            hashmap[num] s..()
        ___ d __ dislikes:
            hashmap[d[0]].add(d[1])
            hashmap[d[1]].add(d[0])
        g0, g1 [1], []
        r.. dfs2(g0, g1, hashmap, 2, N)
    
    ___ dfs2  g0, g1, hashmap, n, N
        __ n > N:
            r.. T..
        dislike0, dislike1 F.., F..
        ___ num __ g0:
            __ n __ hashmap[num] o. num __ hashmap[n]:
                dislike0 T..
                _____
        ___ num __ g1:
            __ n __ hashmap[num] o. num __ hashmap[n]:
                dislike1 T..
                _____
        res F..
        __ n.. dislike0:
            res res o. dfs2(g0 + [n], g1, hashmap, n+1, N)
        __ n.. dislike1:
            res res o. dfs2(g0, g1 + [n], hashmap, n+1, N)
        r.. res
    
    ___ test
        testCases [
            [
                4,
                [[1, 2], [1, 3], [2, 4]],
            ],
            [
                3,
                [[1,2],[1,3],[2,3]],
            ],
        ]
        ___ N, dislikes __ testCases:
            res possibleBipartition(N, dislikes)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
