#!/usr/bin/python3
"""
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?



Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0


Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
"""
from typing ______ List
from collections ______ defaultdict


class Solution:
    ___ removeStones(self, stones: List[List[int]]) -> int:
        """
        convert to graph problem
        each component in the graph can be removed to only one node
        N - #component

        construct graph O(N^2)
        DFS - O(N)
        """
        G = defaultdict(list)
        n = le.(stones)
        ___ i in range(n
            ___ j in range(i
                __ stones[i][0] __ stones[j][0] or stones[i][1] __ stones[j][1]:
                    G[i].append(j)
                    G[j].append(i)

        # dfs
        comp_cnt = 0
        visited = [False ___ _ in range(n)]
        ___ i in range(n
            __ not visited[i]:
                comp_cnt += 1
                self.dfs(G, i, visited)

        r_ n - comp_cnt

    ___ dfs(self, G, i, visited
        visited[i] = True
        ___ nbr in G[i]:
            __ not visited[nbr]:
                self.dfs(G, nbr, visited)


__ __name__ __ "__main__":
    assert Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]) __ 3
