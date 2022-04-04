'''
Created on Mar 14, 2017

@author: MT
'''
c_ Solution(o..
    ___ findMinHeightTrees  n, edges
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ n __ 0: r.. []
        __ n __ 1: r.. [0]
        graph = [s..() ___ _ __ r..(n)]
        ___ e __ edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        leaves    # list
        ___ i, nodes __ e..(graph
            __ l..(nodes) __ 1:
                leaves.a..(i)
        __ n.. leaves:
            r.. []
        w.... n > 2:
            n = n-l..(leaves)
            newLeaves    # list
            ___ leaf __ leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                __ l..(graph[neighbor]) __ 1:
                    newLeaves.a..(neighbor)
            leaves = newLeaves
        r.. leaves
    
    ___ test
        testCases = [
            (4, [[1, 0], [1, 2], [1, 3]]),
            (6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]),
        ]
        ___ n, edges __ testCases:
            print('edges: %s' % (edges
            result = findMinHeightTrees(n, edges)
            print('result: %s' % (result
            print('-='*20+'-')
    
__ _____ __ _____
    Solution().test()
