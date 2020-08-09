class Solution:
    ___ isBipartite(self, graph
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}

        for node in range(le.(graph)):
            __ node not in color:
                color[node] = 0
            for nei in graph[node]:
                __ nei not in color:
                    color[nei] = color[node] ^ 1
                ____ color[nei] __ color[node]:
                    r_ False

        r_ True
