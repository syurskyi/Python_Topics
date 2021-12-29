#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

c_ Graph:
    ___  -   gdictN..
        __ gdict __ N..:
            gdict  {}
        gdict  gdict
    
    ___ addEdge  vertex, edge
        gdict[vertex].ap..(edge)
    
    ___ bfs  vertex
        visited  [vertex]
        queue  [vertex]
        w__ queue:
            deVertex  queue.pop(0)
            print(deVertex)
            ___ adjacentVertex __ gdict[deVertex]:
                __ adjacentVertex no. __ visited:
                    visited.ap..(adjacentVertex)
                    queue.ap..(adjacentVertex)
    
    ___ dfs  vertex
        visited  [vertex]
        stack  [vertex]
        w__ stack:
            popVertex  stack.pop()
            print(popVertex)
            ___ adjacentVertex __ gdict[popVertex]:
                __ adjacentVertex no. __ visited:
                    visited.ap..(adjacentVertex)
                    stack.ap..(adjacentVertex)
    



customDict  { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }



g  Graph(customDict)
g.dfs("a")

