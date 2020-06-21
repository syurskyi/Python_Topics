# # Word Ladder Example Code
# # Below is the Vertex and Graph class used for the Word Ladder example code:
#
# c_ Vertex
#     ___ -  key
#         id _ ?
#         connectedTo _     # dict
#
#     ___ addNeighbor nbr weight_0
#         c..|? _ w..
#
#     ___ -s
#         r_ st. i. + ' connectedTo: ' + st. ||x.i. ___ x __ c..
#
#     ___ getConnections
#         r_ c__.k..
#
#     ___ getId
#         r_ ?
#
#     ___ getWeight nbr
#         r_ c..|?
#
# c_ Graph
#     ___ -
#         vertList _    # dict
#         numVertices _ 0
#
#     ___ addVertex key
#         numVertices _ ? + 1
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
#         r_ ? __ v..
#
#     ___ addEdge f t cost_0
#         __ f no. __ v..
#             nv _ a.. ?
#         __ t no. __ v..
#             nv _ a.. ?
#         v..|?.a.. v..|? c..
#
#     ___ getVertices
#         r_ v__.k..
#
#     ___ -i
#         r_ ? v__.v..
#
# # Code for buildGraph function:
#
# ___ buildGraph wordFile
#     d _    # dict
#     g _ ?
#
#     wfile _ o.. ? _
#     # create buckets of words that differ by one letter
#     ___ line __ ?
#         print ?
#         word _ ?|;-1
#         print ?
#         ___ i __ ra.. le. w..
#             bucket _ w..|;? + '_' + w..|?+1;
#             __ ? __ d
#                 ?|?.ap.. w..
#             ____
#                 ?|b.. _ |w..
#     # add vertices and edges for words __ the same bucket
#     ___ bucket __ d.k..
#         ___ word1 __ d|b..
#             ___ word2 __ d|b..
#                 __ ? !_ ?
#                     g.aE.. ? ?
#     r_ ?
#
# # Please reference the video for full explanation!