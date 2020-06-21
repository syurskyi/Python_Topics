from tree import Tree, Node

TESTTREE = Tree()
TESTTREE.root = Node(42)
NODES = (1, 2, 3, 4, 5, 6)

def populate_tree(node, vals, left):
    if vals:
        node.left = Node(vals[0])
        if len(vals) > 1:
            node.right = Node(vals[1])
        if left:
            populate_tree(node.left, vals[2:], not left)
        else:
            populate_tree(node.right, vals[2:], left)

populate_tree(TESTTREE.root, NODES, True)
