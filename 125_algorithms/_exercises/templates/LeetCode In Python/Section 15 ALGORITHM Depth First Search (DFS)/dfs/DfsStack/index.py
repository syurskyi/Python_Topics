from collections ______ defaultdict


class Graph:

    ___ __init__(self
        self.graph = defaultdict(list)

    ___ insertEdge(self, v1, v2
        self.graph[v1].append(v2)

    ___ DFS(self, startNode
        visited = set()
        st = []
        st.append(startNode)

        w___(le.(st)):
            cur = st[-1]
            st.pop()

            __(cur not __ visited
                print(cur, end=" ")
                visited.add(cur)

            ___ vertex __ self.graph[cur]:
                __(vertex not __ visited
                    st.append(vertex)


g = Graph()

g.insertEdge(2, 1)
g.insertEdge(2, 5)
g.insertEdge(5, 6)
g.insertEdge(5, 8)
g.insertEdge(6, 9)


g.DFS(2)
