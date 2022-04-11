c_ TreeNode(o..
    ___ - , data, left, right
        data data
        left left
        right right

    ___ -s
        fmt 'TreeNode(data={}, left={}, right={})'
        r.. fmt.f..(data, left, right)


c_ BinarySearchTree(o..
    ___ - , tree_data
        root N..
        ___ data __ tree_data:
            add(data)

    ___ add  data
        __ root __ N..
            root TreeNode(data, N.., N..)
            r..
        inserted F..
        cur_node root

        w.... n.. inserted:
            __ data <_ cur_node.data:
                __ cur_node.left:
                    cur_node cur_node.left
                ____
                    cur_node.left TreeNode(data, N.., N..)
                    inserted T..
            ____ data > cur_node.data:
                __ cur_node.right:
                    cur_node cur_node.right
                ____
                    cur_node.right TreeNode(data, N.., N..)
                    inserted T..

    ___ _inorder_traverse  node, elements
        __ node __ n.. N..
            _inorder_traverse(node.left, elements)
            elements.a..(node.data)
            _inorder_traverse(node.right, elements)

    ___ data
        r.. root

    ___ sorted_data
        elements    # list
        _inorder_traverse(root, elements)
        r.. elements
