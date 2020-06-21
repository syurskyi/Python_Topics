# c_ Node
# 	___ _  val neighbors
# 		? ?
# 		? ?
#
# # Example Input:
#
# # 1 <---> 2
# # ^       ^
# # |       |
# # v       v
# # 4 <---> 3
#
# # Example Output:
#
# # 1 <---> 2
# # ^       ^
# # |       |
# # v       v
# # 4 <---> 3
#
# # Visited nodes as we traverse
# # DFS - Depth First Search
# # apply recursion
#
# ___ clone_helper node visited
# 	__ ? __ N..
# 		r_ N..
# 	____ ? __ v__.k..
# 		r_ v..|?
#
# 	neighbors _    # list
# 	new_node _ N.. n__.v.. n..
#
# 	v..|n.. _ n..
#
# 	___ i __ ra.. le. n__.n..
# 		neighbor_node _ ? n__.n.|? v..
# 		n__.ap.. ?
#
# 	r_ ?
#
# ___ clone node
# 	r_ c? ? di..
#
#
# node _ Node(1, [])
# node2 _ Node(2, [])
# node3 _ Node(3, [])
# node4 _ Node(4, [])
#
# node.neighbors.append(node2)
# node.neighbors.append(node4)
#
# node2.neighbors.append(node)
# node2.neighbors.append(node3)
#
# node3.neighbors.append(node2)
# node3.neighbors.append(node4)
#
# node4.neighbors.append(node)
# node4.neighbors.append(node3)
