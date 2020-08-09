from collections ______ defaultdict


class Graph:
    ___ __init__(self
        self.graph = defaultdict(list)

    ___ insertEdge(self, v1, v2
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    ___ printGraph(self
        ___ node __ self.graph:
            ___ v __ self.graph[node]:
                print(node, "->", v)


g = Graph()

g.insertEdge(1, 2)
g.insertEdge(2, 3)
g.insertEdge(4, 5)

g.printGraph()
