#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Disjoint Set in Python

c_ DisjointSet:
    ___  -   vertices
        vertices = vertices
        parent = {}
        ___ v __ vertices:
            parent[v] = v
        rank = dict.fromkeys(vertices, 0)
    
    ___ find  item
        __ parent[item] __ item:
            r_ item
        ____
            r_ find(parent[item])
    
    ___ union  x, y
        xroot = find(x)
        yroot = find(y)
        __ rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        ____ rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        ____
            parent[yroot] = xroot
            rank[xroot] += 1

# vertices = ["A", "B", "C", "D", "E"]

# ds = DisjointSet(vertices)
# ds.union("A", "B")
# ds.union("A", "C")
# print(ds.find("A"))