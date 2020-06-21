# c_ Node
# 	___ - val neighbors
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
# ___ clone node
# 	queue _    # LIST
#
# 	visited _    # DICT
#
# 	?.ap.. ?
#
# 	w__ le. ? > 0
# 		cur _ ?.po. 0
#
# 		new_node _ N..
#
# 		__ c.. __ v__.k..
# 			n.. _ v..|c..
# 		____
# 			new_node _ N.. c__.v.. ||
#
# 		neighbors _ n__.n..
#
# 		v..|c.. _ n..
#
# 		___ i __ ra.. le. c__.n..
# 			__ c__.n..|? __ v__.k..
# 				n__.ap.. v..|c__.n..|?
# 			____
# 				q__.ap.. c__.n..|?
# 				new_neighbor_node _ ? c__.n..|?.v.. ||
# 				n__.ap.. ?
# 				v..|c__.n..|? _ ?
#
# 	r_ v..|n..
#
#
#
#
# node = Node(1, [])
# node2 = Node(2, [])
# node3 = Node(3, [])
# node4 = Node(4, [])
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
