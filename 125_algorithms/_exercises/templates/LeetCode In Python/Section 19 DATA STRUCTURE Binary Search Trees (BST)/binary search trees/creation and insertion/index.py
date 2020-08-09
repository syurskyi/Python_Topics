

class Node:
    ___ __init__(self, value
        self.left = None
        self.right = None
        self.data = value


___ insert(root, node
    __(root is None
        root = node
        r_

    __(root.data < node.data
        __(root.right is None
            root.right = node
        ____
            insert(root.right, node)
    ____
        __(root.left is None
            root.left = node
        ____
            insert(root.left, node)


___ preorder(node
    __(node is not None
        print(node.data)
        preorder(node.left)
        preorder(node.right)


#	         5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8
tree = Node(5)

#	         5
#       /  	      \
#     None	       None

insert(tree, Node(3))

#	         5
#       /  	      \
#     3	            None

insert(tree, Node(2))

#	         5
#       /  	      \
#     3	            None
#   /
#  2
insert(tree, Node(4))

#	         5
#       /  	      \
#     3	            None
#   /   \
#  2     4
insert(tree, Node(7))

#	         5
#       /  	      \
#     3	            7
#   /   \
#  2     4
insert(tree, Node(6))

#	         5
#       /  	      \
#     3	            7
#   /   \        /
#  2     4      6
insert(tree, Node(8))

#	         5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8


# 5 3 2 4 7 6 8
preorder(tree)
