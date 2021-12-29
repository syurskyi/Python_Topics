#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Prims Algorithm  in Python
_____ sys
c_ Graph:
    ___  -   vertexNum, edges, nodes
        edges  edges
        nodes  nodes
        vertexNum  vertexNum
        MST  []
    
    ___ printSolution(self
        print("Edge : Weight")
        ___ s, d, w __ MST:
            print("%s -> %s: %s" % (s, d, w))
    
    ___ primsAlgo(self
        visited  [0]*vertexNum
        edgeNum0
        visited[0]T..
        w__ edgeNum<vertexNum-1:
            m..  sys.maxsize
            ___ i __ ra__(vertexNum
                __ visited[i]:
                    ___ j __ ra__(vertexNum
                        __ ((no. visited[j]) a__ edges[i][j]
                            __ m.. > edges[i][j]:
                                m..  edges[i][j]
                                s  i
                                d  j
            MST.ap..([nodes[s], nodes[d], edges[s][d]])
            visited[d]  T..
            edgeNum + 1
        printSolution()



edges  [[0, 10, 20, 0, 0],
		[10, 0, 30, 5, 0],
		[20, 30, 0, 15, 6],
		[0, 5, 15, 0, 8],
		[0, 0, 6, 8, 0]]
nodes  ["A","B","C","D","E"]
g  Graph(5, edges, nodes)
g.primsAlgo()
