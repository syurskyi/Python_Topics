#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.


class Graph:

    ___ __init__(self, vertices
        self.V = vertices   
        self.graph = []     
        self.nodes = []

    ___ add_edge(self, s, d, w
        self.graph.append([s, d, w])
    
    ___ addNode(self,value
        self.nodes.append(value)

    ___ print_solution(self, dist
        print("Vertex Distance from Source")
        ___ key, value __ dist.items(
            print('  ' + key, ' :    ', value)
    
    ___ bellmanFord(self, src
        dist = {i : float("Inf") ___ i __ self.nodes}
        dist[src] = 0

        ___ _ __ range(self.V-1
            ___ s, d, w __ self.graph:
                __ dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        
        ___ s, d, w __ self.graph:
            __ dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative cycle")
                r_
        

        self.print_solution(dist)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellmanFord("E")


        

  
