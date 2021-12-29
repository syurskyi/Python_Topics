"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ___ invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ root __ N..
            r.. N..
        ____:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left = right
            root.right = left
            r.. root
