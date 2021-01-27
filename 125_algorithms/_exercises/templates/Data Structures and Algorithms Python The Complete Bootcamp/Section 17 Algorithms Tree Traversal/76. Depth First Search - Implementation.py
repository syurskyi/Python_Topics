class Node():
    ___ __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    ___ __init__(self, value):
        self.root = Node(value)

    ___ preorder(self, start, traversal):
        # Root -> Left -> Right
        __ start is None:
            r_

        traversal.append(start.value)
        self.preorder(start.left, traversal)
        self.preorder(start.right, traversal)

        r_ traversal

    ___ inorder(self, start, traversal):
        # Left -> Root -> Right
        __ start is None:
            r_

        self.inorder(start.left, traversal)
        traversal.append(start.value)
        self.inorder(start.right, traversal)

        r_ traversal

    ___ postorder(self, start, traversal):
        # Left -> Right -> Root
        __ start is None:
            r_

        self.postorder(start.left, traversal)
        self.postorder(start.right, traversal)
        traversal.append(start.value)

        r_ traversal


tree = BinaryTree(3)

tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(tree.preorder(tree.root, []))
print(tree.inorder(tree.root, []))
print(tree.postorder(tree.root, []))