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

c_ Solution(o..
    ___ levelOrder  root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res    # list
        __ root __ N..
            r.. res
        queue    # list
        queue.a..(root)
        w.... queue:
            n = l..(queue)
            level    # list
            ___ i __ r..(n
                root = queue.pop(0)
                __ root.left __ n.. N..
                    queue.a..(root.left)
                __ root.right __ n.. N..
                    queue.a..(root.right)
                level.a..(root.val)
            res.a..(level | )
        r.. res
