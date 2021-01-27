#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

class Graph:
    ___ __init__(self, gdict=None
        __ gdict is None:
            gdict = {}
        self.gdict = gdict
    
    ___ addEdge(self, vertex, edge
        self.gdict[vertex].append(edge)
    
    ___ bfs(self, vertex
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                __ adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
    
    ___ dfs(self, vertex
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                __ adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)
    



customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }



g = Graph(customDict)
g.dfs("a")

