'''
Created on Oct 15, 2019

@author: tongq
'''
c_ Solution(object):
    ___ reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        _______ heapq
        graph = [[-1]*N ___ _ __ r..(N)]
        ___ edge __ edges:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]
        res = 0
        h    # list
        visited = [F..]*N
        heapq.heappush(h, (-M, 0))
        w.... h:
            cur = heapq.heappop(h)
            start = cur[1]
            move = -cur[0]
            __ visited[start]:
                continue
            visited[start] = T..
            res += 1
            ___ i __ r..(N):
                __ graph[start][i] != -1:
                    __ move > graph[start][i] a.. n.. visited[i]:
                        heapq.heappush(h, ( -(move-graph[start][i]-1), i) )
                    graph[i][start] -= m..(move, graph[start][i])
                    res += m..(move, graph[start][i])
        r.. res
