

c_ Node:
    ___  - (, value
        .left _ N..
        .right _ N..
        .data _ value


___ insert(root, node
    __(root is N..
        root _ node
        r_

    __(root.data < node.data
        __(root.right is N..
            root.right _ node
        ____
            insert(root.right, node)
    ____
        __(root.left is N..
            root.left _ node
        ____
            insert(root.left, node)


___ preorder(node
    __(node is no. N..
        print(node.data)
        preorder(node.left)
        preorder(node.right)


___ minValueNode(node
    w___(node.left is no. N..
        node _ node.left
    r_ node


___ deleteNode(node, key
    __(node is N..
        r_ node
    # If the key to be deleted is smaller than the node's
    # key then it lies in  left subtree
    __ key < node.data:
        node.left _ deleteNode(node.left, key)
    # If the kye to be delete is greater than the node's key
    # then it lies in right subtree
    ____(key > node.data
        node.right _ deleteNode(node.right, key)
    # If key is same as node's key, then this is the node
    # to be deleted
    ____
        # Node with only one child or no child
        __ node.left is N..
            temp _ node.right
            node _ N..
            r_ temp
        ____ node.right is N..
            temp _ node.left
            node _ N..
            r_ temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp _ minValueNode(node.right)
        # Copy the inorder successor's content to this node
        node.data _ temp.data
        # Delete the inorder successor
        node.right _ deleteNode(node.right, temp.data)

    r_ node


#	           5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8
tree _ Node(5)

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