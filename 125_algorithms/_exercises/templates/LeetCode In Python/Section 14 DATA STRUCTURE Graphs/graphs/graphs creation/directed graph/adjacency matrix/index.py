____ co.. ______ d_d_


c_ Graph:
    ___  -  numberOfNodes
        .numberOfNodes _ numberOfNodes+1
        .graph _ [[0 ___ x __ ra..(numberOfNodes+1)]
                      ___ y __ ra..(numberOfNodes+1)]

    ___ withInBounds v1, v2
        r_ (v1 >_ 0 a.. v1 <_ .numberOfNodes) a.. (v2 >_ 0 a.. v2 <_ .numberOfNodes)

    ___ insertEdge v1, v2
        __(.withInBounds(v1, v2)):
            .graph[v1][v2] _ 1

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
