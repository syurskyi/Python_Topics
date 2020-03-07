class Tree:
    root = None

    def __iter__(self):
        def g(node):
            if node:
                yield node
                yield from g(node.left)
                yield from g(node.right)
        return g(self.root)

class Node:
    left = None
    right = None
    value = None

    def __init__(self, value):
        self.value = value
