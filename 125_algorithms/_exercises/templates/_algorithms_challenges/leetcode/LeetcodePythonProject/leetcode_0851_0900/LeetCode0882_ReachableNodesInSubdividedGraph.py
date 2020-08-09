'''
Created on Oct 15, 2019

@author: tongq
'''
class Solution(object
    ___ reachableNodes(self, edges, M, N
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        ______ heapq
        graph = [[-1]*N ___ _ in range(N)]
        ___ edge in edges:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]
        res = 0
        h = []
        visited = [False]*N
        heapq.heappush(h, (-M, 0))
        w___ h:
            cur = heapq.heappop(h)
            start = cur[1]
            move = -cur[0]
            __ visited[start]:
                continue
            visited[start] = True
            res += 1
            ___ i in range(N
                __ graph[start][i] != -1:
                    __ move > graph[start][i] and not visited[i]:
                        heapq.heappush(h, ( -(move-graph[start][i]-1), i) )
                    graph[i][start] -= min(move, graph[start][i])
                    res += min(move, graph[start][i])
        r_ res
