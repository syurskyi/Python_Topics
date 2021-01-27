#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

from collections import defaultdict

c_ Graph:
    ___  -   numberofVertices
        graph = defaultdict(li__)
        numberofVertices = numberofVertices
    
    ___ addEdge  vertex, edge
        graph[vertex].ap..(edge)
    
    ___ topogologicalSortUtil  v, visited, stack
        visited.ap..(v)

        ___ i __ graph[v]:
            __ i no. __ visited:
                topogologicalSortUtil(i, visited, stack)
        
        stack.insert(0, v)
    
    ___ topologicalSort(self

        visited = []
        stack = []

        ___ k __ li__(graph
            __ k no. __ visited:
                topogologicalSortUtil(k, visited, stack)
        
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