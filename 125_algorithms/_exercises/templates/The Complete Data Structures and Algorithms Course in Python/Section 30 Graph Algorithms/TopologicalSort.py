#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

from collections import defaultdict

class Graph:
    ___ __init__(self, numberofVertices
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices
    
    ___ addEdge(self, vertex, edge
        self.graph[vertex].append(edge)
    
    ___ topogologicalSortUtil(self, v, visited, stack
        visited.append(v)

        for i in self.graph[v]:
            __ i not in visited:
                self.topogologicalSortUtil(i, visited, stack)
        
        stack.insert(0, v)
    
    ___ topologicalSort(self

        visited = []
        stack = []

        for k in list(self.graph
            __ k not in visited:
                self.topogologicalSortUtil(k, visited, stack)
        
        print(stack)
    
    

customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

customGraph.topologicalSort()