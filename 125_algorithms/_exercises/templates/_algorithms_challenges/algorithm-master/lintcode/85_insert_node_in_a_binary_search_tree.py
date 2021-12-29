"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# recursion
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    ___ insertNode(self, root, node):
        __ n.. root:
            r.. node

        __ node.val < root.val:
            root.left = self.insertNode(root.left, node)
        ____:
            root.right = self.insertNode(root.right, node)

        r.. root


# iteration
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    ___ insertNode(self, root, node):
        __ n.. root:
            r.. node

        curr = root
        w.... curr __ n.. node:
            __ node.val < curr.val:
                __ curr.left __ N..
                    curr.left = node
                curr = curr.left
            ____:
                __ curr.right __ N..
                    curr.right = node
                curr = curr.right

        r.. root
