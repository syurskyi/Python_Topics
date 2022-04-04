#!/usr/bin/python3
"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split
everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same
group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people
numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in
this way.

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""
____ t___ _______ List
____ c.. _______ d..


c_ Solution:
    ___ possibleBipartition  N: i.., dislikes: List[List[i..]]) __ b..:
        """
        If given likes, then we can use union-find. But this is dislikes.
        Two bipartition, A, B. For each dislike, do a dfs on A, B.
        O(N * M)

        DFS + coloring do a dfs all on nodes O(N) + O(M)
        """
        G = d..(l..)
        ___ u, v __ dislikes:
            G[u].a..(v)
            G[v].a..(u)

        visited    # dict  # 0 color red, 1 color blue
        ___ u __ r..(1, N+1
            __ u n.. __ visited:
                __ n.. dfs(u, G, visited, 0
                    r.. F..
        r.. T..

    ___ dfs  u, G, visited, color
        visited[u] = color
        ___ nbr __ G[u]:
            __ nbr __ visited:
                __ visited[nbr] __ color:
                    r.. F..
            ____:
                __ n.. dfs(nbr, G, visited, color ^ 1
                    r.. F..

        r.. T..
