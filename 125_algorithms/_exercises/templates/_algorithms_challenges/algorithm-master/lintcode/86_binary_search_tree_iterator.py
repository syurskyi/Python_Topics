"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
w___ iterator.hasNext(
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    ___ __init__(self, root
        self.stack =   # list
        self.node = root

    """
    @return: True if there has next node, or false
    """
    ___ hasNext(self
        r_ self.node or self.stack

    """
    @return: return next node
    """
    ___ next(self
        node = self.node
        stack = self.stack

        w___ node:
            stack.append(node)
            node = node.left

        node = stack.p..

        nxt = node

        self.node = node.right

        r_ nxt
