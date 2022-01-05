c_ TreeNode(o..):
    ___ - , data, left=N.., right_ N..
        data = data
        left = left
        right = right

    ___ __str__
        fmt = 'TreeNode(data={}, left={}, right={})'
        r.. fmt.f..(data, left, right)


c_ BinarySearchTree(o..):
    ___ - , tree_data):
        head = N..
        ___ node_data __ tree_data:
            insert(node_data)

    ___ data
        r.. head

    ___ sorted_data
        r.. [node.data ___ node __ inorder_traversal(head)]

    ___ insert  node_data):
        new_node = TreeNode(node_data)
        __ head __ N..
            head = new_node
        ____:
            insert_node_at(new_node, head)

    ___ insert_node_at  new_node, position):
        __ new_node.data <= position.data:
            __ position.left __ N..
                position.left = new_node
            ____:
                insert_node_at(new_node, position.left)
        ____ new_node.data > position.data:
            __ position.right __ N..
                position.right = new_node
            ____:
                insert_node_at(new_node, position.right)

    ___ inorder_traversal  node):
        __ node.left:
            y.. ____ inorder_traversal(node.left)
        y.. node
        __ node.right:
            y.. ____ inorder_traversal(node.right)
