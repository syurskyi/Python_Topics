class TreeNode(object):
    ___ __init__(self, data, left=N.., right_ N..
        self.data = data
        self.left = left
        self.right = right

    ___ __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        r.. fmt.f..(self.data, self.left, self.right)


class BinarySearchTree(object):
    ___ __init__(self, tree_data):
        self.head = N..
        ___ node_data __ tree_data:
            self.insert(node_data)

    ___ data(self):
        r.. self.head

    ___ sorted_data(self):
        r.. [node.data ___ node __ self.inorder_traversal(self.head)]

    ___ insert(self, node_data):
        new_node = TreeNode(node_data)
        __ self.head __ N..
            self.head = new_node
        ____:
            self.insert_node_at(new_node, self.head)

    ___ insert_node_at(self, new_node, position):
        __ new_node.data <= position.data:
            __ position.left __ N..
                position.left = new_node
            ____:
                self.insert_node_at(new_node, position.left)
        ____ new_node.data > position.data:
            __ position.right __ N..
                position.right = new_node
            ____:
                self.insert_node_at(new_node, position.right)

    ___ inorder_traversal(self, node):
        __ node.left:
            y.. ____ self.inorder_traversal(node.left)
        y.. node
        __ node.right:
            y.. ____ self.inorder_traversal(node.right)
