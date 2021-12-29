c_ Graph:

    ___  -   v
        v  v
        graph  []

    ___ add_edge  s, d, w
        graph.ap..([s,d,w])

    ___ bellman_ford  src

        dist  [fl__('inf')]* v
        dist[src]  0

        # Relax v-1

        ___ i __ ra__(v - 1
            ___ u, v, c __ graph:
                __ dist[u] ! fl__('inf') a__ dist[u] + c < dist[v]:
                    dist[v]  dist[u] + c

        # - ve cycles
        ___ u, v, c __ graph:
            __ dist[u] ! fl__('inf') a__ dist[u] + c < dist[v]:
                print('Graph contains -ve cycle')

        print("vertex distance from the source :")

        ___ i __ ra__(v
            print(i, ' : ', dist[i])


g  Graph(6)
g.add_edge(0, 1, 8)
g.add_edge(0, 5, 5)
g.add_edge(0, 3, 3)
g.add_edge(1, 2, 6)
g.add_edge(2, 4, 4)
g.add_edge(3, 4, -1)
g.add_edge(5, 1, -4)
g.add_edge(5, 2, -1)
g.add_edge(5, 4, -3)
g.bellman_ford(0)

