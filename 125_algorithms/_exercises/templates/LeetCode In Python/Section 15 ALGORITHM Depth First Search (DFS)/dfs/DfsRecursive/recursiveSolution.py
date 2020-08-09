
from collections ______ defaultdict

# This class represents a directed graph using adjacency list representation


class Graph:

    # Constructor
    ___ __init__(self

        self.graph = defaultdict(list)

    ___ setEdge(self, u, v
        self.graph[u].append(v)
        print(self.graph)

    ___ DFS(self, u, visited
        visited.add(u)
        print(u, end=' ')

        for v in self.graph[u]:
            __ v not in visited:
                self.DFS(v, visited)


g = Graph()
g.setEdge(2, 1)
g.setEdge(2, 5)
g.setEdge(5, 6)
g.setEdge(5, 8)
g.setEdge(6, 9)


visited = set()

g.DFS(2, visited)
