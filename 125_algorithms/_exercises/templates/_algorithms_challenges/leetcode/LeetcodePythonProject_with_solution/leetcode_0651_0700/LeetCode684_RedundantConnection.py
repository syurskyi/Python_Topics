'''
Created on Oct 21, 2017

@author: MT
'''
class Solution(object):
    ___ findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = l..(edges)
        roots = [-1]*(n+1)
        ___ edge __ edges:
            root1 = self.getRoot(roots, edge[0])
            root2 = self.getRoot(roots, edge[1])
            __ root1 __ root2:
                r.. edge
            roots[root1] = root2
        r.. [-1, -1]
    
    ___ getRoot(self, roots, ind):
        while roots[ind] != -1:
            ind = roots[ind]
        r.. ind
    
    ___ test(self):
        testCases = [
            [[1, 2], [1, 3], [2, 3]],
            [[1, 2,], [2, 3], [3, 4], [1, 4], [1, 5]],
        ]
        ___ edges __ testCases:
            print('edges: %s' % edges)
            result = self.findRedundantConnection(edges)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
