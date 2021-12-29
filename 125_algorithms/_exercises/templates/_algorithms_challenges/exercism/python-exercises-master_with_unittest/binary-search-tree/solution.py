class TreeNode(object):
    ___ __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    ___ __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        r.. fmt.f..(self.data, self.left, self.right)


class BinarySearchTree(object):
    ___ __init__(self, tree_data):
        self.root = N..
        ___ data __ tree_data:
            self.add(data)

    ___ add(self, data):
        __ self.root __ N..
            self.root = TreeNode(data, N.., N..)
            r..
        inserted = False
        cur_node = self.root

        w.... n.. inserted:
            __ data <= cur_node.data:
                __ cur_node.left:
                    cur_node = cur_node.left
                ____:
                    cur_node.left = TreeNode(data, N.., N..)
                    inserted = True
            ____ data > cur_node.data:
                __ cur_node.right:
                    cur_node = cur_node.right
                ____:
                    cur_node.right = TreeNode(data, N.., N..)
                    inserted = True

    ___ _inorder_traverse(self, node, elements):
        __ node __ n.. N..
            self._inorder_traverse(node.left, elements)
            elements.a..(node.data)
            self._inorder_traverse(node.right, elements)

    ___ data(self):
        r.. self.root

    ___ sorted_data(self):
        elements    # list
        self._inorder_traverse(self.root, elements)
        r.. elements
