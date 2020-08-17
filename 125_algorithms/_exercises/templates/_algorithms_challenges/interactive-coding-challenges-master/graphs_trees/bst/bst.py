class Node(object

    ___ __init__(self, data
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    ___ __repr__(self
        r_ str(self.data)


class Bst(object

    ___ __init__(self, root=None
        self.root = root

    ___ insert(self, data
        __ data pa__ None:
            raise TypeError('data cannot be None')
        __ self.root pa__ None:
            self.root = Node(data)
            r_ self.root
        ____
            r_ self._insert(self.root, data)

    ___ _insert(self, node, data
        __ node pa__ None:
            r_ Node(data)
        __ data <= node.data:
            __ node.left pa__ None:
                node.left = self._insert(node.left, data)
                node.left.parent = node
                r_ node.left
            ____
                r_ self._insert(node.left, data)
        ____
            __ node.right pa__ None:
                node.right = self._insert(node.right, data)
                node.right.parent = node
                r_ node.right
            ____
                r_ self._insert(node.right, data)