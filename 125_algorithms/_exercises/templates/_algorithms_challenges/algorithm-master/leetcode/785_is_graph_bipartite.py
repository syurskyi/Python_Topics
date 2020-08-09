class Solution:
    ___ isBipartite(self, graph
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}

        ___ node in range(le.(graph)):
            __ node not in color:
                color[node] = 0
            ___ nei in graph[node]:
                __ nei not in color:
                    color[nei] = color[node] ^ 1
                ____ color[nei] __ color[node]:
                    r_ False

        r_ True
