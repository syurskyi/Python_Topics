# # Implement a Graph Class!
# # That's it!
# # Best of luck and reference the video lecture ___ any questions!
# # You have to fully worked out implementations in the lectures, so make sure to refer to them!
#
# c_ Graph
#     '''
#     In order to implement a Graph as an Adjacency List what we need to do is define the methods our Adjacency List object will have:
#     Graph() creates a new, empty graph.
#     addVertex(vert) adds an instance of Vertex to the graph.
#     addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
#     addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
#     getVertex(vertKey) finds the vertex in the graph named vertKey.
#     getVertices() returns the list of all vertices in the graph.
#     in returns True ___ a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.
#     '''
#     ___ -
# #         nodes = set() # all the vertexes in the graph -- could be done in the edges part
#         connections _   # dict  # all the connections start_vertex:{end_vertex:weigth}
#
# #     ___ add_node(self, node):
# #         nodes.add(node)
#
#     ___ contains v
#         r_ v __ ?.k..
#
#     ___ connect start end weight_1
# #         v = get_vertex(str(from_vertex)) or Vertex(str(from_vertex))
#         __ start no. __ ?
#             ?|? _ |e..;w..
#         ____
#             ?|s.. |e.. _ w..
#
#         __ end no. __ ?
#             ?|? _ ||  # dict
#
#     ___ get_nodes
#         r_ ?.k..
#
# #     assume there is one and only one start node (no one points to it) in the directed graph
#     ___ get_start_vertex
#         cadidates _ se. g..
#         ___ end __ ?.v..
#             ___ k __ ?.k..
#                 __ k __ c..
#                     c__.r.. ?
# #         r_ set(get_nodes()) - set(end_nodes)
#         r_ ?
#
#     ___ paint
#         print ?
#
# g _ ?
# # v1 _ Node(1)
# g.connect(1, 2)
#
# g.connect(1,3)
# g.connect(1,4)
# g.connect(2,4)
# g.connect(2,5)
# g.connect(3,5)
# g.connect(5,4)
#
# g.paint()
#
# # {1: {2: 1, 3: 1, 4: 1}, 2: {4: 1, 5: 1}, 3: {5: 1}, 4: {}, 5: {4: 1}}
# #
# g.get_nodes()
#
# # dict_keys([1, 2, 3, 4, 5])
#
# g.get_start_vertex()
# #
# # {1}
# #
# type(g.get_start_vertex())
# # set
# #
# s = set([1,2,3])
# #
# s
# #
# # {1, 2, 3}
# #
# # Good Luck!