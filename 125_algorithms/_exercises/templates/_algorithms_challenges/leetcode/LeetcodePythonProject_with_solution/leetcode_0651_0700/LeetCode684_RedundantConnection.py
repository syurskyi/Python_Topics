'''
Created on Oct 21, 2017

@author: MT
'''
c_ Solution(object):
    ___ findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = l..(edges)
        roots = [-1]*(n+1)
        ___ edge __ edges:
            root1 = getRoot(roots, edge[0])
            root2 = getRoot(roots, edge[1])
            __ root1 __ root2:
                r.. edge
            roots[root1] = root2
        r.. [-1, -1]
    
    ___ getRoot(self, roots, ind):
        w.... roots[ind] != -1:
            ind = roots[ind]
        r.. ind
    
    ___ test
        testCases = [
            [[1, 2], [1, 3], [2, 3]],
            [[1, 2,], [2, 3], [3, 4], [1, 4], [1, 5]],
        ]
        ___ edges __ testCases:
            print('edges: %s' % edges)
            result = findRedundantConnection(edges)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
