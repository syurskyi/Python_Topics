'''
Created on Jun 10, 2018

@author: tongq
'''
class Solution(object):
    ___ sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        ___ i __ r..(N):
            graph[i] = set()
        ___ i, j __ edges:
            graph[i].add(j)
            graph[j].add(i)
        res = [0]*N
        count = [0]*N
        self.dfs(0, set(), graph, res, count)
        self.dfs2(0, set(), graph, res, count, N)
        r.. res
    
    ___ dfs(self, root, visited, graph, res, count):
        visited.add(root)
        ___ i __ graph[root]:
            __ i n.. __ visited:
                self.dfs(i, visited, graph, res, count)
                count[root] += count[i]
                res[root] += res[i]+count[i]
        count[root] += 1
    
    ___ dfs2(self, root, visited, graph, res, count, N):
        visited.add(root)
        ___ i __ graph[root]:
            __ i n.. __ visited:
                res[i] = res[root] - count[i] + N - count[i]
                self.dfs2(i, visited, graph, res, count, N)
    
    ##########################################################
    ######################## OWN TLE #########################
    ##########################################################
    ___ sumOfDistancesInTree_own_TLE(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = N
        graph = {}
        ___ i __ r..(n):
            graph[i]    # list
        ___ edge __ edges:
            graph[edge[0]].a..(edge[1])
            graph[edge[1]].a..(edge[0])
        res    # list
        ___ i __ r..(n):
            res.a..(self.bfs(graph, i))
        r.. res
    
    ___ bfs(self, graph, i):
        res = 0
        queue = [i]
        visited = set([i])
        level = 1
        w.... queue:
            size = l..(queue)
            ___ _ __ r..(size):
                node = queue.pop(0)
                ___ node0 __ graph[node]:
                    __ node0 n.. __ visited:
                        res += level
                        visited.add(node0)
                        queue.a..(node0)
            level += 1
        r.. res
    
    ___ test(self):
        testCases = [
            [
                6,
                [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]],
            ],
        ]
        ___ n, edges __ testCases:
            print('n: %s' % n)
            print('edges: %s' % edges)
            result = self.sumOfDistancesInTree(n, edges)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
