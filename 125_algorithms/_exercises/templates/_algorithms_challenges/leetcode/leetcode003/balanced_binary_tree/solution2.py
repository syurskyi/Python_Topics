"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ___ isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ root __ None:
            return True
        else:
            __ self.height(root) != -1:
                return True
            else:
                return False

    ___ height(self, root):
        # Return -1 if not balanced
        __ root __ None:
            return 0
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            __ left_height == -1 or right_height == -1:
                return -1
            else:
                __ abs(left_height - right_height) <= 1:
                    return max(left_height, right_height) + 1
                else:
                    return -1
