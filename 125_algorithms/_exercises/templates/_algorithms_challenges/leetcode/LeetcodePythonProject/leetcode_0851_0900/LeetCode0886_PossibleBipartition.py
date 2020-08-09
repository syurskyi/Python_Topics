'''
Created on Oct 22, 2019

@author: tongq
'''
class Solution(object
    ___ possibleBipartition(self, N, dislikes
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = [[False]*N ___ _ in range(N)]
        ___ d in dislikes:
            graph[d[0]-1][d[1]-1] = True
            graph[d[1]-1][d[0]-1] = True
        group = [0]*N
        ___ i in range(N
            __ group[i] __ 0 and not self.dfs(graph, group, i, 1, N
                r_ False
        r_ True
    
    ___ dfs(self, graph, group, idx, g, N
        group[idx] = g
        ___ i in range(N
            __ graph[idx][i] __ 1:
                __ group[i] __ g:
                    r_ False
                __ group[i] __ 0 and not self.dfs(graph, group, i, -g, N
                    r_ False
        r_ True
    
    ___ possibleBipartition_own_TLE(self, N, dislikes
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        hashmap = {}
        ___ num in range(1, N+1
            hashmap[num] = set()
        ___ d in dislikes:
            hashmap[d[0]].add(d[1])
            hashmap[d[1]].add(d[0])
        g0, g1 = [1], []
        r_ self.dfs2(g0, g1, hashmap, 2, N)
    
    ___ dfs2(self, g0, g1, hashmap, n, N
        __ n > N:
            r_ True
        dislike0, dislike1 = False, False
        ___ num in g0:
            __ n in hashmap[num] or num in hashmap[n]:
                dislike0 = True
                break
        ___ num in g1:
            __ n in hashmap[num] or num in hashmap[n]:
                dislike1 = True
                break
        res = False
        __ not dislike0:
            res = res or self.dfs2(g0 + [n], g1, hashmap, n+1, N)
        __ not dislike1:
            res = res or self.dfs2(g0, g1 + [n], hashmap, n+1, N)
        r_ res
    
    ___ test(self
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
        ___ N, dislikes in testCases:
            res = self.possibleBipartition(N, dislikes)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
