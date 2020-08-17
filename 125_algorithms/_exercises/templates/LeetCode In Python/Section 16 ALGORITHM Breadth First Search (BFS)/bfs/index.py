
____ co.. ______ d_d_


c_ Graph:

    ___  - (
        .graph _ d_d_(list)

    ___ setEdge u, v
        .graph[u].ap..(v)

    ___ bfs s
        visited _ set()

        queue _   # list
        queue.ap..(s)

        visited.add(s)

        w___ queue:
            u _ queue.pop(0)
            print(u, end_" ")

            ___ v __ .graph[u]:
                __ v no. __ visited:
                    queue.ap..(v)
                    visited.add(v)


g _ Graph()
g.setEdge(2, 1)
g.setEdge(2, 5)
g.setEdge(5, 6)
g.setEdge(5, 8)
g.setEdge(6, 9)

g.bfs(2)
