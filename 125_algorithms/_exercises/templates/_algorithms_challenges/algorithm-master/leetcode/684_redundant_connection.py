"""
given input is an undirected graph

1. iterate edges
2. if u and v are connected before we add edge in nodes (graph)
   => that is the edge should be removed
"""


c_ Solution:
    """
    UnionFind
    """
    ___ findRedundantConnection  edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ n.. edges:
            r.. []

        nodes    # dict

        ___ u, v __ edges:
            __ n.. union(nodes, u, v):
                r.. [u, v]

        r.. []

    ___ union  nodes, u, v):
        a = find(nodes, u)
        b = find(nodes, v)

        __ a __ b:
            r.. F..

        nodes[a] = b
        r.. T..

    ___ find  nodes, u):
        __ u n.. __ nodes:
            nodes[u] = u
            r.. u
        __ nodes[u] __ u:
            r.. u

        nodes[u] = find(nodes, nodes[u])
        r.. nodes[u]


_______ c..


c_ Solution:
    """
    DFS
    """
    ___ findRedundantConnection  edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ n.. edges:
            r.. []

        nodes = c...defaultdict(set)

        ___ u, v __ edges:
            # dfs to check u and v are connected already => cycle
            __ u __ nodes a.. v __ nodes a.. dfs(nodes, u, v, set()):
                r.. [u, v]

            nodes[u].add(v)
            nodes[v].add(u)

        r.. []

    ___ dfs  nodes, u, v, visited):
        __ u __ v:
            r.. T..
        __ u __ visited:
            r.. F..

        visited.add(u)

        ___ x __ nodes[u]:
            __ dfs(nodes, x, v, visited):
                r.. T..

        r.. F..
