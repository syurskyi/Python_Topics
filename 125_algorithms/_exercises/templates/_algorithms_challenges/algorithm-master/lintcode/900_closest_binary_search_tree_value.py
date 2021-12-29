"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    ___ closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        __ n.. root:
            r.. float('-inf')

        __ root.left and target < root.val:
            left = self.closestValue(root.left, target)

            __ abs(left - target) < abs(root.val - target):
                r.. left

        __ root.right and target > root.val:
            right = self.closestValue(root.right, target)

            __ abs(right - target) < abs(root.val - target):
                r.. right

        r.. root.val
