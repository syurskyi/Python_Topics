from collections ______ defaultdict


c_ Graph:
    ___ __init__(, numberOfNodes
        .numberOfNodes _ numberOfNodes+1
        .graph _ [[0 ___ x __ ra..(numberOfNodes+1)]
                      ___ y __ ra..(numberOfNodes+1)]

    ___ withInBounds(, v1, v2
        r_ (v1 >_ 0 and v1 <_ .numberOfNodes) and (v2 >_ 0 and v2 <_ .numberOfNodes)

    ___ insertEdge(, v1, v2
        __(.withInBounds(v1, v2)):
            .graph[v1][v2] _ 1
            .graph[v2][v1] _ 1

    ___ printGraph(
        ___ i __ ra..(.numberOfNodes
            ___ j __ ra..(le.(.graph[i])):
                __(.graph[i][j]
                    print(i, "->", j)


g _ Graph(5)

g.insertEdge(1, 2)
g.insertEdge(2, 3)
g.insertEdge(4, 5)

g.printGraph()
