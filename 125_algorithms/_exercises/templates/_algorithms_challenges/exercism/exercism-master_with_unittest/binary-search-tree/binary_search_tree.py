class TreeNode(object):
    ___ __init__(self, data, left=None, right_ N..
        self.data = data
        self.left = left
        self.right = right

    ___ __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    ___ __init__(self, tree_data):
        self.head = None
        for node_data in tree_data:
            self.insert(node_data)

    ___ data(self):
        return self.head

    ___ sorted_data(self):
        return [node.data for node in self.inorder_traversal(self.head)]

    ___ insert(self, node_data):
        new_node = TreeNode(node_data)
        __ self.head is None:
            self.head = new_node
        else:
            self.insert_node_at(new_node, self.head)

    ___ insert_node_at(self, new_node, position):
        __ new_node.data <= position.data:
            __ position.left is None:
                position.left = new_node
            else:
                self.insert_node_at(new_node, position.left)
        elif new_node.data > position.data:
            __ position.right is None:
                position.right = new_node
            else:
                self.insert_node_at(new_node, position.right)

    ___ inorder_traversal(self, node):
        __ node.left:
            yield from self.inorder_traversal(node.left)
        yield node
        __ node.right:
            yield from self.inorder_traversal(node.right)
