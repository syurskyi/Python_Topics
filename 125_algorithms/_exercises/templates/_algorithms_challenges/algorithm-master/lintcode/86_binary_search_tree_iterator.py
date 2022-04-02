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


c_ BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    ___ - , root
        stack    # list
        node = root

    """
    @return: True if there has next node, or false
    """
    ___ hasNext
        r.. node o. stack

    """
    @return: return next node
    """
    ___ next
        node = node
        stack = stack

        w.... node:
            stack.a..(node)
            node = node.left

        node = stack.pop()

        nxt = node

        node = node.right

        r.. nxt
