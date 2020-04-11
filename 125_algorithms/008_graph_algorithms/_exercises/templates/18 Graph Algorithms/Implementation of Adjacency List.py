# # Implementation of a Graph as an Adjacency List
# # Using dictionaries, it is easy to implement the adjacency list in Python. In our implementation of the Graph abstract
# # data type we will create two classes: Graph, which holds the master list of vertices, and Vertex,
# # which will represent each vertex in the graph.
# # Each Vertex uses a dictionary to keep track of the vertices to which it is connected, and the weight of each edge.
# # This dictionary is called connectedTo. The constructor simply initializes the id, which will typically be a string,
# # and the connectedTo dictionary. The addNeighbor method is used add a connection from this vertex to another.
# # The getConnections method returns all of the vertices in the adjacency list, as represented by the connectedTo
# # instance variable. The getWeight method returns the weight of the edge from this vertex to the vertex passed as
# # a parameter.
#
# c_ Vertex
#     ___ - key
#         id _ key
#         connectedTo _    # dict
#
#     ___ addNeighbor nbr weight_0
#         c..|? _ ?
#
#     ___ -s
#         r_ st. i. + ' connectedTo: ' + st.||x.i. ___ ? __ c..
#
#     ___ getConnections
#         r_ c__.k..
#
#     ___ getId
#         r_ i.
#
#     ___ getWeight nbr
#         r_ c..|?
#
# # In order to implement a Graph as an Adjacency List what we need to do is define the methods our
# # Adjacency List object will have:
# #
# #     Graph() creates a new, empty graph.
# #     addVertex(vert) adds an instance of Vertex to the graph.
# #     addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
# #     addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
# #     getVertex(vertKey) finds the vertex in the graph named vertKey.
# #     getVertices() returns the list of all vertices in the graph.
# #     in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.
#
# c_ Graph
#     ___ -
#         vertList _   # dict
#         numVertices _ 0
#
#     ___ addVertex key
#         n.. _ ? + 1
#         newVertex _ ? ?
#         v..|? _ ?
#         r_ ?
#
#     ___ getVertex n
#         __ ? __ v..
#             r_ v..|?
#         ____
#             r_ N..
#
#     ___ -c n
#         r_ n __ v..
#
#     ___ addEdge f t cost_0
#         __ f no. __ v..
#             nv _ a.. ?
#         __ t no. __ v..
#             nv _ a.. ?
#         v..|?.aN.. v..|? c..
#
#     ___ getVertices
#         r_ v__.k..
#
#     ___ -i
#         r_ i.. v__.v..
#
# # Let's see a simple example of how to use this:
#
# g _ ?
# ___ i __ ra.. 6
#     g.a.. ?
#
# ?.v..
#
# # {0: <__main__.Vertex instance at 0x10476b680>,
# #  1: <__main__.Vertex instance at 0x104cce5f0>,
# #  2: <__main__.Vertex instance at 0x10395d950>,
# #  3: <__main__.Vertex instance at 0x1039c00e0>,
# #  4: <__main__.Vertex instance at 0x1039c4e60>,
# #  5: <__main__.Vertex instance at 0x1039c45f0>}
# #
# ?.a.. 0,1,2
# #
# ___ vertex __ g
#     print ?
#     print ?.g..
#     print '\n'
#
# # 0 connectedTo: [1]
# # [<__main__.Vertex instance at 0x104cce5f0>]
# # 1 connectedTo: []
# # []
#
# # 2 connectedTo: []
# # []
# #
# #
# # 3 connectedTo: []
# # []
# #
# #
# # 4 connectedTo: []
# # []
# #
# #
# # 5 connectedTo: []
# # []
# #
# #
# # Great Job!