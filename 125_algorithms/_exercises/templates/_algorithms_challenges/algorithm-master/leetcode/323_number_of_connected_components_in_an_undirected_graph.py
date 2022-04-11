"""
Testing:
>>> gotcha = []
>>> for s in (Solution(), Solution2()):
...     for _in, _out in (
...         ((5, [[0, 1], [1, 2], [3, 4]]), 2),
...         ((5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1),
...     ):
...         res = s.countComponents(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


c_ Solution:
    """
    Union Find
    """
    ___ countComponents  n, edges
        """
        :type n: int
        :type edges: list[int]
        :rtype: int
        """
        __ n.. n o. n.. edges:
            r.. 0

        nodes [i ___ i __ r..(n)]

        ans n

        ___ a, b __ edges:
            __ union(nodes, a, b
                ans -_ 1

        r.. ans

    ___ union  nodes, a, b
        _a find(nodes, a)
        _b find(nodes, b)

        __ _a __ _b:
            r.. F..

        nodes[_b] _a
        r.. T..

    ___ find  nodes, a
        __ a n.. __ nodes:
            nodes[a] a
            r.. a
        __ nodes[a] __ a:
            r.. a

        nodes[a] find(nodes[a])
        r.. nodes[a]


c_ Solution2:
    """
    DFS
    """
    ___ countComponents  n, edges
        """
        :type n: int
        :type edges: list[int]
        :rtype: int
        """
        ans 0

        __ n.. n o. n.. edges:
            r.. ans

        adj    # dict

        ___ i __ r..(n
            adj[i] s..()

        ___ a, b __ edges:
            adj[a].add(b)
            adj[b].add(a)

        visited s..()

        ___ i __ r..(n
            __ i __ visited:
                _____

            ans += 1
            dfs(i, adj, visited)

        r.. ans

    ___ dfs  a, adj, visited
        __ a n.. __ adj:
            r..

        visited.add(a)

        ___ b __ adj[a]:
            __ b __ visited:
                _____

            dfs(b, adj, visited)
