#!/usr/bin/python3
"""
In this problem, a tree is an undirected graph that is connected and has no
cycles.

The given input is a graph that started as a tree with N nodes (with distinct
values 1, 2, ..., N), with one additional edge added. The added edge has two
different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a
pair [u, v] with u < v, that represents an undirected edge connecting nodes u
and v.

Return an edge that can be removed so that the resulting graph is a tree of N
nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is
the size of the input array.
"""
____ typing _______ List
____ c.. _______ defaultdict


c_ DisjointSet
    ___ - ):
        sz    # dict  # element -> size
        pi    # dict  # element -> pi

    ___ add  x):
        __ x n.. __ pi:  # need to check, otherwise override wrongly
            sz[x] = 1
            pi[x] = x

    ___ unionize  x, y):
        p1 = root(x)
        p2 = root(y)
        __ p1 != p2:
            sz1 = sz[p1]
            sz2 = sz[p2]
            __ sz1 > sz2:
                p1, p2 = p2, p1

            pi[p1] = p2
            sz[p2] += sz[p1]
            del sz[p1]

    ___ root  x):
        p = pi[x]
        __ p != x:
            pi[x] = root(p)

        r.. pi[x]

    ___ is_union  x, y):
        __ x __ pi a.. y __ pi:
            r.. root(x) __ root(y)

        r.. F..


c_ Solution:
    ___ findRedundantConnection  edges: List[List[i..]]) __ List[i..]:
        """
        Union-find
        """
        ds = DisjointSet()
        ___ p, q __ edges:
            ds.add(p)
            ds.add(q)
            __ ds.is_union(p, q):
                r.. [p, q]

            ds.unionize(p, q)

        r..

c_ Solution_dfs:
    ___ findRedundantConnection  edges: List[List[i..]]) __ List[i..]:
        """
        Construct graph: O(|E|)
        Find circle through dfs: O(|V|)
        Notice: need to extract the circle from the cyclic path
        """
        G = defaultdict(set)
        ___ p, q __ edges:
            G[p].add(q)
            G[q].add(p)

        visited = set()
        ___ k __ G.k..:
            __ k n.. __ visited:
                circle = dfs(G, k, N.., set([k]), [k], visited)
                __ circle:
                    ___ p, q __ r..(edges):
                        __ p __ circle a.. q __ circle:
                            r.. [p, q]

        r..

    ___ dfs  G, cur, pi, path, path_list, visited):
        visited.add(cur)

        ___ nbr __ G[cur]:
            __ nbr != pi:
                __ nbr __ path:
                    # extract the circle from path
                    circle = set()
                    in_circle = F..
                    ___ e __ path_list:
                        __ e __ nbr:
                            in_circle = T..
                        __ in_circle:
                            circle.add(e)
                    r.. circle

                path.add(nbr)
                path_list.a..(nbr)
                circle = dfs(G, nbr, cur, path, path_list, visited)
                __ circle:
                    r.. circle
                path.remove(nbr)
                path_list.pop()

        r.. N..


__ _______ __ _______
    ... Solution().findRedundantConnection([[1,2], [1,3], [2,3]]) __ [2, 3]
    ... Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]) __ [1, 4]
    ... Solution().findRedundantConnection([[30,44],[34,47],[22,32],[35,44],[26,36],[2,15],[38,41],[28,35],[24,37],[14,49],[44,45],[11,50],[20,39],[7,39],[19,22],[3,17],[15,25],[1,39],[26,40],[5,14],[6,23],[5,6],[31,48],[13,22],[41,44],[10,19],[12,41],[1,12],[3,14],[40,50],[19,37],[16,26],[7,25],[22,33],[21,27],[9,50],[24,42],[43,46],[21,47],[29,40],[31,34],[9,31],[14,31],[5,48],[3,18],[4,19],[8,17],[38,46],[35,37],[17,43]]) __ [5,48]
