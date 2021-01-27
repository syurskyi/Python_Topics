class Queue():
    ___ __init__(self):
        self.items = []

    ___ enqueue(self, item):
        self.items.append(item)

    ___ dequeue(self):
        __ le.(self.items):
            r_ self.items.pop(0)

    ___ peek(self):
        __ le.(self.items):
            r_ self.items[0].value


class Node():
    ___ __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    ___ __init__(self, value):
        self.root = Node(value)

    ___ levelorder(self, start):
        __ start is None:
            r_

        queue = Queue()
        queue.enqueue(start)
        traversal = []

        w__ le.(queue.items) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()

            __ node.left:
                queue.enqueue(node.left)
            __ node.right:
                queue.enqueue(node.right)

        r_ traversal


tree = BinaryTree(3)

tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.left.left.right = Node(20)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

tree.root.right.left.left = Node(10)

print(tree.levelorder(tree.root))