'''
Created on Oct 21, 2017

@author: MT
'''
c_ Solution(o..
    ___ findRedundantDirectedConnection  edges
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        can1 [-1, -1]
        can2 [-1, -1]
        n l..(edges)
        parent [0]*(n+1)
        ___ i __ r..(n
            __ parent[edges[i][1]] __ 0:
                parent[edges[i][1]] edges[i][0]
            ____
                can2 [edges[i][0], edges[i][1]]
                can1 [parent[edges[i][1]], edges[i][1]]
                edges[i][1] 0
        ___ i __ r..(n+1
            parent[i] i
        ___ i __ r..(n
            __ edges[i][1] __ 0:
                _____
            child edges[i][1]
            par edges[i][0]
            __ getRoot(parent, par) __ child:
                __ can1[0] __ -1:
                    r.. edges[i]
                r.. can1
            parent[child] par
        r.. can2
    
    ___ getRoot  parent, i
        w.... i !_ parent[i]:
            parent[i] parent[parent[i]]
            i parent[i]
        r.. i
    
    ___ test
        testCases [
#             [[1, 2], [1, 3], [2, 3]],
#             [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]],
            [[2,1],[3,1],[4,2],[1,4]],
        ]
        ___ edges __ testCases:
            print('edges: %s' % edges)
            result findRedundantDirectedConnection(edges)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
