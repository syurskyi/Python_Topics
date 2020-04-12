# # Implementation of Breadth First Search
# # An alternative algorithm called Breath-First search provides us with the ability to return the same results
# # as DFS but with the added guarantee to return the shortest-path first. This algorithm is a little more tricky
# # to implement in a recursive manner instead using the queue data-structure, as such I will only being documenting
# # the iterative approach. The actions performed per each explored vertex are the same as the depth-first implementation,
# # however, replacing the stack with a queue will instead explore the breadth of a vertex depth before moving on.
# # This behavior guarantees that the first path located is one of the shortest-paths present, based on number
# # of edges being the cost factor.
# #
# # We'll assume our Graph is in the form:
#
# graph = {'A': set(['B', 'C']),
#          'B': set(['A', 'D', 'E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B', 'F']),
#          'F': set(['C', 'E'])}
#
# # Connected Component
# #
# # Similar to the iterative DFS implementation the only alteration required is to remove the next item from
# # the beginning of the list structure instead of the stacks last.
#
# ___ bfs graph start
#     visited queue _ se. |s..
#     w__ queue
#         vertex _ ?.po. 0
#         __ ? no. __ v..
#             ?.ad. ?
#             ?.ex.. ?|v.. - v..
#     r_ ?
#
# ? ? 'A'
# # {'A', 'B', 'C', 'D', 'E', 'F'}
# #
# # Paths
# #
# # This implementation can again be altered slightly to instead return all possible paths between two vertices,
# # the first of which being one of the shortest such path.
#
# ___ bfs_paths graph start goal
#     queue _ ||s.. |s..
#     w__ ?
#         |vertex path| _ ?.po. 0
#         ___ next __ ?|v.. - se. p..
#             __ ? __ g..
#                 y__ p.. + |?
#             ____
#                 ?.ap.. ? p.. + |?
#
# li.. ? ? 'A', 'F'
# # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
# #
# # Knowing that the shortest path will be returned first from the BFS path generator method we can create
# # a useful method which simply returns the shortest path found or None if no path exists. As we are using a generator
# # this in theory should provide similar performance results as just breaking out and returning the first matching path
# # in the BFS implementation.
#
# ___ shortest_path graph start goal
#     ___
#         r_ n.. b_p.. ? ? ?
#     _______ S..
#         r_ N..
#
# ? ? 'A', 'F'
# # ['A', 'C', 'F']
# #
# # Resources