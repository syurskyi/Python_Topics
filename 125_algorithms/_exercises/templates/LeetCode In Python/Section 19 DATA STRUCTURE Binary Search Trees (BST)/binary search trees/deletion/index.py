

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


___ minValueNode(node
    w___(node.left is not None
        node = node.left
    r_ node


___ deleteNode(node, key
    __(node is None
        r_ node
    # If the key to be deleted is smaller than the node's
    # key then it lies in  left subtree
    __ key < node.data:
        node.left = deleteNode(node.left, key)
    # If the kye to be delete is greater than the node's key
    # then it lies in right subtree
    ____(key > node.data
        node.right = deleteNode(node.right, key)
    # If key is same as node's key, then this is the node
    # to be deleted
    ____
        # Node with only one child or no child
        __ node.left is None:
            temp = node.right
            node = None
            r_ temp
        ____ node.right is None:
            temp = node.left
            node = None
            r_ temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(node.right)
        # Copy the inorder successor's content to this node
        node.data = temp.data
        # Delete the inorder successor
        node.right = deleteNode(node.right, temp.data)

    r_ node


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

deleteNode(tree, 7)

#	           5
#       /  	      \
#     3	            8
#   /   \        /     \
#  2     4      6       None


# 5 3 2 4 8 6
preorder(tree)
