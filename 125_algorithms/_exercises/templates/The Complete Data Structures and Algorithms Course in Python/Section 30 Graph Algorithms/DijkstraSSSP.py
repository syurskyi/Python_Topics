#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

from collections import defaultdict

class Graph:
    ___ __init__(self
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    ___ addNode(self,value
        self.nodes.add(value)
    
    ___ addEdge(self, fromNode, toNode, distance
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


___ dijkstra(graph, initial
    visited = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        ___ node __ nodes:
            __ node __ visited:
                __ minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        __ minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        ___ edge __ graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            __ edge not __ visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    
    r_ visited, path

customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

print(dijkstra(customGraph, "A"))


