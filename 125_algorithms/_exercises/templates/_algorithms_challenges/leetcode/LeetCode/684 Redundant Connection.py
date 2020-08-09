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
from typing ______ List
from collections ______ defaultdict


class DisjointSet(
    ___ __init__(self
        self.sz = {}  # element -> size
        self.pi = {}  # element -> pi

    ___ add(self, x
        __ x not in self.pi:  # need to check, otherwise override wrongly
            self.sz[x] = 1
            self.pi[x] = x

    ___ unionize(self, x, y
        p1 = self.root(x)
        p2 = self.root(y)
        __ p1 != p2:
            sz1 = self.sz[p1]
            sz2 = self.sz[p2]
            __ sz1 > sz2:
                p1, p2 = p2, p1

            self.pi[p1] = p2
            self.sz[p2] += self.sz[p1]
            del self.sz[p1]

    ___ root(self, x
        p = self.pi[x]
        __ p != x:
            self.pi[x] = self.root(p)

        r_ self.pi[x]

    ___ is_union(self, x, y
        __ x in self.pi and y in self.pi:
            r_ self.root(x) __ self.root(y)

        r_ False


class Solution:
    ___ findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Union-find
        """
        ds = DisjointSet()
        for p, q in edges:
            ds.add(p)
            ds.add(q)
            __ ds.is_union(p, q
                r_ [p, q]

            ds.unionize(p, q)

        raise

class Solution_dfs:
    ___ findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Construct graph: O(|E|)
        Find circle through dfs: O(|V|)
        Notice: need to extract the circle from the cyclic path
        """
        G = defaultdict(set)
        for p, q in edges:
            G[p].add(q)
            G[q].add(p)

        visited = set()
        for k in G.keys(
            __ k not in visited:
                circle = self.dfs(G, k, None, set([k]), [k], visited)
                __ circle:
                    for p, q in reversed(edges
                        __ p in circle and q in circle:
                            r_ [p, q]

        raise

    ___ dfs(self, G, cur, pi, path, path_list, visited
        visited.add(cur)

        for nbr in G[cur]:
            __ nbr != pi:
                __ nbr in path:
                    # extract the circle from path
                    circle = set()
                    in_circle = False
                    for e in path_list:
                        __ e __ nbr:
                            in_circle = True
                        __ in_circle:
                            circle.add(e)
                    r_ circle

                path.add(nbr)
                path_list.append(nbr)
                circle = self.dfs(G, nbr, cur, path, path_list, visited)
                __ circle:
                    r_ circle
                path.remove(nbr)
                path_list.pop()

        r_ None


__ __name__ __ "__main__":
    assert Solution().findRedundantConnection([[1,2], [1,3], [2,3]]) __ [2, 3]
    assert Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]) __ [1, 4]
    assert Solution().findRedundantConnection([[30,44],[34,47],[22,32],[35,44],[26,36],[2,15],[38,41],[28,35],[24,37],[14,49],[44,45],[11,50],[20,39],[7,39],[19,22],[3,17],[15,25],[1,39],[26,40],[5,14],[6,23],[5,6],[31,48],[13,22],[41,44],[10,19],[12,41],[1,12],[3,14],[40,50],[19,37],[16,26],[7,25],[22,33],[21,27],[9,50],[24,42],[43,46],[21,47],[29,40],[31,34],[9,31],[14,31],[5,48],[3,18],[4,19],[8,17],[38,46],[35,37],[17,43]]) __ [5,48]
