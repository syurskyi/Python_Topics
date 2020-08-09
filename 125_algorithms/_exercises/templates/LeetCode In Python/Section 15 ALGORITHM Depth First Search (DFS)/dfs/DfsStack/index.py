from collections ______ defaultdict


c_ Graph:

    ___ __init__(
        .graph _ defaultdict(list)

    ___ insertEdge(, v1, v2
        .graph[v1].ap..(v2)

    ___ DFS(, startNode
        visited _ set()
        st _ []
        st.ap..(startNode)

        w___(le.(st)):
            cur _ st[-1]
            st.pop()

            __(cur no. __ visited
                print(cur, end_" ")
                visited.add(cur)

            ___ vertex __ .graph[cur]:
                __(vertex no. __ visited
                    st.ap..(vertex)


g _ Graph()

g.insertEdge(2, 1)
g.insertEdge(2, 5)
g.insertEdge(5, 6)
g.insertEdge(5, 8)
g.insertEdge(6, 9)


g.DFS(2)
