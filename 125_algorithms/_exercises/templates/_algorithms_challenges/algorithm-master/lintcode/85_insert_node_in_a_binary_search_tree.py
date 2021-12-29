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
        __ not root:
            return node

        __ node.val < root.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)

        return root


# iteration
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    ___ insertNode(self, root, node):
        __ not root:
            return node

        curr = root
        while curr is not node:
            __ node.val < curr.val:
                __ curr.left is None:
                    curr.left = node
                curr = curr.left
            else:
                __ curr.right is None:
                    curr.right = node
                curr = curr.right

        return root
