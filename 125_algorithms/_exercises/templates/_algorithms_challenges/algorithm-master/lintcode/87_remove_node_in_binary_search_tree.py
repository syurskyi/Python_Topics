"""
Main Concept:
https://discuss.leetcode.com/topic/65792/recursive-easy-to-understand-java-solution


Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: target: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    ___ removeNode(self, root, target
        __ not root:
            r_ root

        __ root.val __ target:
            __ not root.left:
                r_ root.right
            __ not root.right:
                r_ root.left

            min_node = self.find_min(root.right)
            root.val = min_node.val
            root.right = self.removeNode(root.right, root.val)

            r_ root

        __ target < root.val:
            root.left = self.removeNode(root.left, target)
        ____
            root.right = self.removeNode(root.right, target)

        r_ root

    ___ find_min(self, node
        __ not node:
            r_ node
        w___ node.left:
            node = node.left
        r_ node
