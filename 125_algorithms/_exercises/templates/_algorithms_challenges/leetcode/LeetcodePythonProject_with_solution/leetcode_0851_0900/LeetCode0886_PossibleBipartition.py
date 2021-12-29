'''
Created on Oct 22, 2019

@author: tongq
'''
class Solution(object):
    ___ possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = [[False]*N ___ _ __ r..(N)]
        ___ d __ dislikes:
            graph[d[0]-1][d[1]-1] = True
            graph[d[1]-1][d[0]-1] = True
        group = [0]*N
        ___ i __ r..(N):
            __ group[i] __ 0 and n.. self.dfs(graph, group, i, 1, N):
                r.. False
        r.. True
    
    ___ dfs(self, graph, group, idx, g, N):
        group[idx] = g
        ___ i __ r..(N):
            __ graph[idx][i] __ 1:
                __ group[i] __ g:
                    r.. False
                __ group[i] __ 0 and n.. self.dfs(graph, group, i, -g, N):
                    r.. False
        r.. True
    
    ___ possibleBipartition_own_TLE(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        hashmap = {}
        ___ num __ r..(1, N+1):
            hashmap[num] = set()
        ___ d __ dislikes:
            hashmap[d[0]].add(d[1])
            hashmap[d[1]].add(d[0])
        g0, g1 = [1], []
        r.. self.dfs2(g0, g1, hashmap, 2, N)
    
    ___ dfs2(self, g0, g1, hashmap, n, N):
        __ n > N:
            r.. True
        dislike0, dislike1 = False, False
        ___ num __ g0:
            __ n __ hashmap[num] o. num __ hashmap[n]:
                dislike0 = True
                break
        ___ num __ g1:
            __ n __ hashmap[num] o. num __ hashmap[n]:
                dislike1 = True
                break
        res = False
        __ n.. dislike0:
            res = res o. self.dfs2(g0 + [n], g1, hashmap, n+1, N)
        __ n.. dislike1:
            res = res o. self.dfs2(g0, g1 + [n], hashmap, n+1, N)
        r.. res
    
    ___ test(self):
        testCases = [
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
            res = self.possibleBipartition(N, dislikes)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
