____ collections _____ defaultdict


c_ Graph:

    ___  -   vertices
        v  vertices
        adj  defaultdict(li__)

    ___ add_edge  u, v
        adj[u].ap..(v)

    ___ topological_sort(self
        in_degree  [0] * v

        ___ i __ adj:
            ___ j __ adj[i]:
                in_degree[j] + 1

        # creating queue
        q  []
        ___ i __ ra__(v
            __ in_degree[i] __ 0:
                q.ap..(i)

        c  0
        linear_order  []

        # One by one pop vertices from queue and append adjacents if indegree of adjacent becomes 0

        w__ q:
            x  q.pop()
            linear_order.ap..(x)
            ___ vertex __ adj[x]:
                in_degree[vertex] - 1
                __ in_degree[vertex] __ 0:
                    q.ap..(vertex)
            c + 1

        # check for negative cycle | print the linear order

        __ c ! v:
            print('Graph contains -ve cycle')
            r_
        print('linear order is: ', linear_order)


g  Graph(5);
g.add_edge(0, 1);
g.add_edge(0, 3);
g.add_edge(1, 2);
g.add_edge(3, 1);
g.add_edge(3, 2);
g.add_edge(3, 4);

g.topological_sort();