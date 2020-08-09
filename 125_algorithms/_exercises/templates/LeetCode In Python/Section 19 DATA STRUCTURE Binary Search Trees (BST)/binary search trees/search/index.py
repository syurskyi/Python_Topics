

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


___ search(node, key
    print("Current Node is: ", node.data)
    __(node is None
        print("No node found")
        r_ None
    __(node.data __ key
        print("Node found !")
        r_ node

    __(node.data < key
        r_ search(node.right, key)

    r_ search(node.left, key)


#	           5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8
tree = Node(5)

insert(tree, Node(3))


insert(tree, Node(2))

insert(tree, Node(4))

insert(tree, Node(7))

insert(tree, Node(6))

insert(tree, Node(8))

search(tree, 8)
