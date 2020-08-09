class TreeNode(object
    ___ __init__(self, data, left, right
        self.data = data
        self.left = left
        self.right = right

    ___ __str__(self
        fmt = 'TreeNode(data={}, left={}, right={})'
        r_ fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object
    ___ __init__(self, tree_data
        self._root = TreeNode(tree_data[0], None, None)
        for data in tree_data[1:]:
            branch = self._root
            w___ branch is not None:
                root = branch
                attr = 'right' __ root.data < data else 'left'
                branch = getattr(root, attr)
            setattr(root, attr, TreeNode(data, None, None))

    ___ data(self
        r_ self._root

    ___ sorted_data(self
        result = []
        queue = [self._root]
        w___ queue:
            node = queue[-1]
            __ node.left is not None and node.left not in result:
                queue.append(node.left)
            ____
                result.append(queue.pop())
                __ node.right is not None:
                    queue.append(node.right)
        r_ [n.data for n in result]
