
class Node:
    ___ __init__(self, data
        self.data = data
        self.left = None
        self.right = None


___ is_subtree(tree, subtree

    __ subtree is None:
        r_ True
    __ tree is None:
        r_ False

    tree1 = []
    tree2 = []

    in_order(tree, tree1)
    in_order(subtree, tree2)

    str1 = tree1.__str__().replace("[", "").replace("]", "")
    str2 = tree2.__str__().replace("[", "").replace("]", "")

    __ str1.find(str2) == -1:
        r_ False

    tree1 = []
    tree2 = []

    pre_order(tree, tree1)
    pre_order(subtree, tree2)

    str3 = tree1.__str__().replace("[", "").replace("]", "")
    str4 = tree2.__str__().replace("[", "").replace("]", "")

    __ str3.find(str4) == -1:
        r_ False
    r_ True


___ in_order(tree, tree1

    __ tree is None:
        r_

    in_order(tree.left, tree1)
    tree1.append(tree.data)
    in_order(tree.right, tree1)


___ pre_order(tree, tree1

    __ tree is None:
        r_

    tree1.append(tree.data)
    pre_order(tree.left, tree1)
    pre_order(tree.right, tree1)


root1 = Node(1);
root1.left = Node(2);
root1.right = Node(3);
root1.left.left = Node(4);
root1.left.right = Node(5);
root1.right.left = Node(6);
root1.right.right = Node(7);

root2 = Node(3)
root2.left = Node(6);
root2.right = Node(7);


is_subtree = is_subtree(root1, root2)
print(is_subtree)

