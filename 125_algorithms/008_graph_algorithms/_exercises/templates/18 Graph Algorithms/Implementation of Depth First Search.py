# # Implementation of Depth-First Search
# # This algorithm we will be discussing is Depth-First search which as the name hints at, explores possible vertices
# # (from a supplied root) down each branch before backtracking. This property allows the algorithm to be implemented
# # succinctly in both iterative and recursive forms. Below is a listing of the actions performed upon each visit to a node.
# #
# #     Mark the current vertex as being visited.
# #     Explore each adjacent vertex that is not included in the visited set.
# #
# # We will assume a simplified version of a graph in the following form:
# #
# # graph = {'A': set(['B', 'C']),
# #          'B': set(['A', 'D', 'E']),
# #          'C': set(['A', 'F']),
# #          'D': set(['B']),
# #          'E': set(['B', 'F']),
# #          'F': set(['C', 'E'])}
# #
# # Connected Component
# #
# # The implementation below uses the stack data-structure to build-up and return a set of vertices that are
# # accessible within the subjects connected component. Using Python s overloading of the subtraction operator
# # to remove items from a set, we are able to add only the unvisited adjacent vertices.
#
# ___ dfs graph start
#     visited, stack _ se. |s..
#     w__ s..
#         vertex _ s__.po.
#         __ ? no. __ v..
#             ?.ad. ?
#             s__.ex.. g..|v.. - v..
#     r_ ?
#
# ? ? 'A'
# # {'A', 'B', 'C', 'D', 'E', 'F'}
# #
# # The second implementation provides the same functionality as the first, however, this time we are using the more
# # succinct recursive form. Due to a common Python gotcha with default parameter values being created only once,
# # we are required to create a new visited set on each user invocation. Another Python language detail is that function
# # variables are passed by reference, resulting in the visited mutable set not having to reassigned upon each recursive
# # call.
#
# ___ dfs graph start visited_N..
#     __ visited __ N..
#         ? _ se.
#     ?.ad. s..
#     ___ nxt __ g..|s.. - v..
#         ? g.. n.. v..
#     r_ ?
#
# ? ? 'A'
# # {'A', 'B', 'C', 'D', 'E', 'F'}
# #
# # Paths
# #
# # We are able to tweak both of the previous implementations to return all possible paths between a start
# # and goal vertex. The implementation below uses the stack data-structure again to iteratively solve the problem,
# # yielding each possible path when we locate the goal. Using a generator allows the user to only compute the desired
# # amount of alternative paths.
#
# ___ dfs_paths graph start goal
#     stack _ ||s.. |s..
#     w__ ?
#         |vertex path _ ?.po.
#         ___ nxt __ g..|v.. - se. p..
#             __ ? __ g..
#                 y___ p.. + |?
#             ____
#                 ?.ap.. ? p.. + |?
#
# li.. ? ? 'A', 'F'
# # [['A', 'B', 'E', 'F'], ['A', 'C', 'F']]
# #
# # Resources