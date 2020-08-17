"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
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
    ___ insertNode(self, root, node
        __ not root:
            r_ node

        __ node.val < root.val:
            root.left = self.insertNode(root.left, node)
        ____
            root.right = self.insertNode(root.right, node)

        r_ root


# iteration
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    ___ insertNode(self, root, node
        __ not root:
            r_ node

        curr = root
        w___ curr pa__ not node:
            __ node.val < curr.val:
                __ curr.left pa__ None:
                    curr.left = node
                curr = curr.left
            ____
                __ curr.right pa__ None:
                    curr.right = node
                curr = curr.right

        r_ root
