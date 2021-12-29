'''
Created on Mar 2, 2017

@author: MT
'''

class Solution(object):
    ___ validTree(self, n, edges):
        roots = [-1]*n
        ___ e __ edges:
            root0 = self.findRoot(roots, e[0])
            root1 = self.findRoot(roots, e[1])
            __ root0 != root1:
                roots[root0] = root1
            ____:
                r.. False
        r.. l..(edges) __ n-1
    
    ___ findRoot(self, roots, ind):
        while roots[ind] != -1:
            ind = roots[ind]
        r.. ind
    
    ___ validTreeBFS(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        hashmap = {}
        ___ i __ r..(n):
            hashmap[i]    # list
        ___ edge __ edges:
            hashmap[edge[0]].a..(edge[1])
            hashmap[edge[1]].a..(edge[0])
        queue    # list
        queue.a..(0)
        visited = [False]*n
        while queue:
            top = queue[0]
            queue.pop(0)
            __ visited[top]:
                r.. False
            visited[top] = True
            ___ i __ hashmap[top]:
                __ n.. visited[i]:
                    queue.a..(i)
        ___ b __ visited:
            __ n.. b:
                r.. False
        r.. True
    
    ___ validTreeDFS(self, n, edges):
        hashmap = {}
        ___ i __ r..(n):
            hashmap[i]    # list
        ___ edge __ edges:
            hashmap[edge[0]].a..(edge[1])
            hashmap[edge[1]].a..(edge[0])
        visited = [False]*n
        __ n.. self.helper(0, -1, hashmap, visited):
            r.. False
        ___ b __ visited:
            __ n.. b: r.. False
        r.. True
    
    ___ helper(self, curr, parent, hashmap, visited):
        __ visited[curr]: r.. False
        visited[curr] = True
        ___ i __ hashmap[curr]:
            __ i != parent and n.. self.helper(i, curr, hashmap, visited):
                r.. False
        r.. True
    
    ___ test(self):
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
            print('n: %s' % (n))
            print('edges: %s' % (edges))
            result = self.validTree(n, edges)
            print('result: %s' % (result))
            print('-='*20+'-')
        
__ __name__ __ '__main__':
    Solution().test()
