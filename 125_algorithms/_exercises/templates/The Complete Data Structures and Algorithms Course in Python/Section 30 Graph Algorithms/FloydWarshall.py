#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Floyd Warshall Algorithm in python

INF = 9999
# Printing the solution
___ printSolution(nV, distance
    ___ i __ range(nV
        ___ j __ range(nV
            __(distance[i][j] __ INF
                print("INF", end=" ")
            ____
                print(distance[i][j], end="  ")
        print(" ")


___ floydWarshall(nV, G
    distance = G
    ___ k __ range(nV
        ___ i __ range(nV
            ___ j __ range(nV
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    
    printSolution(nV, distance)

G = [[0, 8, INF,1],
    [INF, 0, 1,INF],
    [4, INF, 0,INF],
    [INF, 2, 9,1]
    ]

floydWarshall(4, G)

