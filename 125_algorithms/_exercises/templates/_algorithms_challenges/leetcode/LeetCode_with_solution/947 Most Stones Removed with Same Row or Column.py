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
____ t___ _______ L..
____ c.. _______ d..


c_ Solution:
    ___ removeStones  stones: L..[L..[i..]]) __ i..:
        """
        convert to graph problem
        each component in the graph can be removed to only one node
        N - #component

        construct graph O(N^2)
        DFS - O(N)
        """
        G d..(l..)
        n l..(stones)
        ___ i __ r..(n
            ___ j __ r..(i
                __ stones[i][0] __ stones[j][0] o. stones[i][1] __ stones[j][1]:
                    G[i].a..(j)
                    G[j].a..(i)

        # dfs
        comp_cnt 0
        visited [F.. ___ _ __ r..(n)]
        ___ i __ r..(n
            __ n.. visited[i]:
                comp_cnt += 1
                dfs(G, i, visited)

        r.. n - comp_cnt

    ___ dfs  G, i, visited
        visited[i] T..
        ___ nbr __ G[i]:
            __ n.. visited[nbr]:
                dfs(G, nbr, visited)


__ _______ __ _______
    ... Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]) __ 3
