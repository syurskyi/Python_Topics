'''
Created on Mar 2, 2017

@author: MT
'''

c_ Solution(o..
    ___ validTree  n, edges
        roots = [-1]*n
        ___ e __ edges:
            root0 = findRoot(roots, e[0])
            root1 = findRoot(roots, e[1])
            __ root0 != root1:
                roots[root0] = root1
            ____:
                r.. F..
        r.. l..(edges) __ n-1
    
    ___ findRoot  roots, ind
        w.... roots[ind] != -1:
            ind = roots[ind]
        r.. ind
    
    ___ validTreeBFS  n, edges
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        hashmap    # dict
        ___ i __ r..(n
            hashmap[i]    # list
        ___ edge __ edges:
            hashmap[edge[0]].a..(edge[1])
            hashmap[edge[1]].a..(edge[0])
        queue    # list
        queue.a..(0)
        visited = [F..]*n
        w.... queue:
            top = queue[0]
            queue.pop(0)
            __ visited[top]:
                r.. F..
            visited[top] = T..
            ___ i __ hashmap[top]:
                __ n.. visited[i]:
                    queue.a..(i)
        ___ b __ visited:
            __ n.. b:
                r.. F..
        r.. T..
    
    ___ validTreeDFS  n, edges
        hashmap    # dict
        ___ i __ r..(n
            hashmap[i]    # list
        ___ edge __ edges:
            hashmap[edge[0]].a..(edge[1])
            hashmap[edge[1]].a..(edge[0])
        visited = [F..]*n
        __ n.. helper(0, -1, hashmap, visited
            r.. F..
        ___ b __ visited:
            __ n.. b: r.. F..
        r.. T..
    
    ___ helper  curr, parent, hashmap, visited
        __ visited[curr]: r.. F..
        visited[curr] = T..
        ___ i __ hashmap[curr]:
            __ i != parent a.. n.. helper(i, curr, hashmap, visited
                r.. F..
        r.. T..
    
    ___ test
        testCases = [
            (
                5,
                [[0, 1], [0, 2], [0, 3], [1, 4]],
            ),
            (
                5,
                [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]],
            ),
            [
                6,
                [[0,1],[1,2],[2,0],[3,4],[4,5]],
            ],
        ]
        ___ n, edges __ testCases:
            print('n: %s' % (n
            print('edges: %s' % (edges
            result = validTree(n, edges)
            print('result: %s' % (result
            print('-='*20+'-')
        
__ _____ __ _____
    Solution().test()
