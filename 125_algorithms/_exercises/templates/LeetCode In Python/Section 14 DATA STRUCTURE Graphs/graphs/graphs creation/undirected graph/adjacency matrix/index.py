from collections ______ defaultdict


class Graph:
    ___ __init__(self, numberOfNodes
        self.numberOfNodes = numberOfNodes+1
        self.graph = [[0 ___ x __ ra..(numberOfNodes+1)]
                      ___ y __ ra..(numberOfNodes+1)]

    ___ withInBounds(self, v1, v2
        r_ (v1 >= 0 and v1 <= self.numberOfNodes) and (v2 >= 0 and v2 <= self.numberOfNodes)

    ___ insertEdge(self, v1, v2
        __(self.withInBounds(v1, v2)):
            self.graph[v1][v2] = 1
            self.graph[v2][v1] = 1

    ___ printGraph(self
        ___ i __ ra..(self.numberOfNodes
            ___ j __ ra..(le.(self.graph[i])):
                __(self.graph[i][j]
                    print(i, "->", j)


g = Graph(5)

g.insertEdge(1, 2)
g.insertEdge(2, 3)
g.insertEdge(4, 5)

g.printGraph()
