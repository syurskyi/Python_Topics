'''
Created on Mar 18, 2017

@author: MT
'''

c_ Solution(o..
    ___ countComponents  n, edges
        count = n
        roots = [-1]*count
        ___ edge __ edges:
            root1 = findRoot(roots, edge[0])
            root2 = findRoot(roots, edge[1])
            __ root1 != root2:
                roots[root1] = root2
                count -_ 1
#         print('roots: %s' % roots)
        r.. count
    
    ___ findRoot  roots, ind
        w.... roots[ind] != -1:
            ind = roots[ind]
        r.. ind
    
    ___ countComponentsAnother  n, edges
        count = n
        roots = l..(r..(n
        ___ edge __ edges:
            root1 = find(roots, edge[0])
            root2 = find(roots, edge[1])
            __ root1 != root2:
                roots[root1] = roots[root2]
                count -_ 1
        r.. count
        
    ___ find  roots, ind
        w.... roots[ind] != ind:
            roots[ind] = roots[roots[ind]]
            ind = roots[ind]
        r.. ind
    
    ___ test
        testCases = [
            (5, [[0, 1], [1, 2], [3, 4]]),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]]),
            (3, [[0, 1], [0, 2]]),
        ]
        ___ n, edges __ testCases:
            print('n: %s' % (n
            print('edges: %s' % (edges
            result = countComponents(n, edges)
            result = countComponentsOwn(n, edges)
            print('result: %s' % (result
            print('-='*20+'-')
    
__ _____ __ _____
    Solution().test()

