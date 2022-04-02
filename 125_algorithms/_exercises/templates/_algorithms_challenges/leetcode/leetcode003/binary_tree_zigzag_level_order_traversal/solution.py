"""
Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    ___ zigzagLevelOrder  root
        __ root __ N..
            r.. []
        res    # list
        queue    # list
        rev = F..  # Reverse direction
        level    # list
        queue.a..(root)
        queue.a..(N..)
        w.... queue:
            root = queue.pop(0)
            __ root __ N..
                __ queue:
                    queue.a..(N..)
                res.a..(level)
                level    # list
                rev = n.. rev  # Toggle direction
            ____:
                __ rev:
                    level.insert(0, root.val)
                ____:
                    level.a..(root.val)
                __ root.left __ n.. N..
                    queue.a..(root.left)
                __ root.right __ n.. N..
                    queue.a..(root.right)
        r.. res
