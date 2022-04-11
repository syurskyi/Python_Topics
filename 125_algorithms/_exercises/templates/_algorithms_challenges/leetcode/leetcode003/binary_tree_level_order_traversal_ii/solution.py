"""
Given a binary tree, return the bottom-up level order traversal of its nodes'
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
    ___ levelOrderBottom  root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack    # list
        __ root __ N..
            r.. stack
        queue    # list
        level    # list
        queue.a..(root)
        queue.a..(N..)
        w.... queue:
            root queue.p.. 0)
            __ root __ N..
                stack.a..(level | )
                level    # list
                __ queue:
                    queue.a..(N..)
            ____
                level.a..(root.val)
                __ root.left __ n.. N..
                    queue.a..(root.left)
                __ root.right __ n.. N..
                    queue.a..(root.right)
        res    # list
        w.... stack:
            res.a..(stack.pop
        r.. res
