#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Disjoint Set in Python

class DisjointSet:
    ___ __init__(self, vertices
        self.vertices = vertices
        self.parent = {}
        ___ v __ vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)
    
    ___ find(self, item
        __ self.parent[item] == item:
            r_ item
        ____
            r_ self.find(self.parent[item])
    
    ___ union(self, x, y
        xroot = self.find(x)
        yroot = self.find(y)
        __ self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        ____
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

# vertices = ["A", "B", "C", "D", "E"]

# ds = DisjointSet(vertices)
# ds.union("A", "B")
# ds.union("A", "C")
# print(ds.find("A"))