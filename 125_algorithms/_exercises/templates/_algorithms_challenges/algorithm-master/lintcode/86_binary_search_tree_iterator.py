"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    ___ __init__(self, root):
        self.stack = []
        self.node = root

    """
    @return: True if there has next node, or false
    """
    ___ hasNext(self):
        return self.node or self.stack

    """
    @return: return next node
    """
    ___ next(self):
        node = self.node
        stack = self.stack

        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()

        nxt = node

        self.node = node.right

        return nxt
