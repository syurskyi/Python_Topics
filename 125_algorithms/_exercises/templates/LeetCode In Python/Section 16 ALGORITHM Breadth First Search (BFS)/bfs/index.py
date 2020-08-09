
from collections ______ defaultdict


class Graph:

    ___ __init__(self
        self.graph = defaultdict(list)

    ___ setEdge(self, u, v
        self.graph[u].append(v)

    ___ bfs(self, s
        visited = set()

        queue = []
        queue.append(s)

        visited.add(s)

        w___ queue:
            u = queue.pop(0)
            print(u, end=" ")

            ___ v __ self.graph[u]:
                __ v not __ visited:
                    queue.append(v)
                    visited.add(v)


g = Graph()
g.setEdge(2, 1)
g.setEdge(2, 5)
g.setEdge(5, 6)
g.setEdge(5, 8)
g.setEdge(6, 9)

g.bfs(2)
