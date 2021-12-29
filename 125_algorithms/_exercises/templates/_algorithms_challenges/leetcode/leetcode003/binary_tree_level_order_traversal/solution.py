"""
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ___ levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res    # list
        __ root __ N..
            r.. res
        queue    # list
        level    # list
        queue.a..(root)
        queue.a..(N..)
        while queue:
            root = queue.pop(0)
            __ root __ N..
                res.a..(level[:])
                level    # list
                __ queue:
                    queue.a..(N..)
            ____:
                level.a..(root.val)
                __ root.left __ n.. N..
                    queue.a..(root.left)
                __ root.right __ n.. N..
                    queue.a..(root.right)
        r.. res
