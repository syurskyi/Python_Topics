class Solution:
    ___ isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}

        for node in range(len(graph)):
            __ node not in color:
                color[node] = 0
            for nei in graph[node]:
                __ nei not in color:
                    color[nei] = color[node] ^ 1
                elif color[nei] == color[node]:
                    return False

        return True
