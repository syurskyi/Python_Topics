'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object
    ___ countComponents(self, n, edges
        count = n
        roots = [-1]*count
        for edge in edges:
            root1 = self.findRoot(roots, edge[0])
            root2 = self.findRoot(roots, edge[1])
            __ root1 != root2:
                roots[root1] = root2
                count -= 1
#         print('roots: %s' % roots)
        r_ count
    
    ___ findRoot(self, roots, ind
        w___ roots[ind] != -1:
            ind = roots[ind]
        r_ ind
    
    ___ countComponentsAnother(self, n, edges
        count = n
        roots = list(range(n))
        for edge in edges:
            root1 = self.find(roots, edge[0])
            root2 = self.find(roots, edge[1])
            __ root1 != root2:
                roots[root1] = roots[root2]
                count -= 1
        r_ count
        
    ___ find(self, roots, ind
        w___ roots[ind] != ind:
            roots[ind] = roots[roots[ind]]
            ind = roots[ind]
        r_ ind
    
    ___ test(self
        testCases = [
            (5, [[0, 1], [1, 2], [3, 4]]),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]]),
            (3, [[0, 1], [0, 2]]),
        ]
        for n, edges in testCases:
            print('n: %s' % (n))
            print('edges: %s' % (edges))
            result = self.countComponents(n, edges)
            result = self.countComponentsOwn(n, edges)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()

