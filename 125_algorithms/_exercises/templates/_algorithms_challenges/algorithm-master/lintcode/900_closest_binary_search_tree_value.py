"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    ___ closestValue  root, target
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        __ n.. root:
            r.. f__('-inf')

        __ root.left a.. target < root.val:
            left = closestValue(root.left, target)

            __ a..(left - target) < a..(root.val - target
                r.. left

        __ root.right a.. target > root.val:
            right = closestValue(root.right, target)

            __ a..(right - target) < a..(root.val - target
                r.. right

        r.. root.val
