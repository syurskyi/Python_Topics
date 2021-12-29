c_ Queue():
    ___  -
        items  []

    ___ enqueue  item):
        items.a..(item)

    ___ dequeue
        __ le.(items):
            r_ items.pop(0)

    ___ peek
        __ le.(items):
            r_ items[0].value


c_ Node():
    ___  -   value):
        value  value
        left  N..
        right  N..


c_ BinaryTree():
    ___  -   value):
        root  Node(value)

    ___ levelorder  start):
        __ start __ N..:
            r_

        queue  Queue()
        queue.enqueue(start)
        traversal  []

        w__ le.(queue.items) > 0:
            traversal.a..(queue.peek())
            node  queue.dequeue()

            __ node.left:
                queue.enqueue(node.left)
            __ node.right:
                queue.enqueue(node.right)

        r_ traversal


tree  BinaryTree(3)

tree.root.left  Node(4)
tree.root.left.left  Node(6)
tree.root.left.right  Node(7)

tree.root.left.left.right  Node(20)

tree.root.right  Node(5)
tree.root.right.left  Node(8)
tree.root.right.right  Node(9)

tree.root.right.left.left  Node(10)

print(tree.levelorder(tree.root))