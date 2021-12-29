#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

____ collections _____ defaultdict

c_ Graph:
    ___  - (self
        nodes  set()
        edges  defaultdict(li__)
        distances  {}
    
    ___ addNode value
        nodes.add(value)
    
    ___ addEdge  fromNode, toNode, distance
        edges[fromNode].ap..(toNode)
        distances[(fromNode, toNode)]  distance


___ dijkstra(graph, initial
    visited  {initial : 0}
    path  defaultdict(li__)

    nodes  set(graph.nodes)

    w__ nodes:
        minNode  N..
        ___ node __ nodes:
            __ node __ visited:
                __ minNode __ N..:
                    minNode  node
                ____ visited[node] < visited[minNode]:
                    minNode  node
        __ minNode __ N..:
            b__

        nodes.remove(minNode)
        currentWeight  visited[minNode]

        ___ edge __ graph.edges[minNode]:
            weight  currentWeight + graph.distances[(minNode, edge)]
            __ edge no. __ visited or weight < visited[edge]:
                visited[edge]  weight
                path[edge].ap..(minNode)
    
    r_ visited, path

customGraph  Graph()
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


