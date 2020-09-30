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
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    ___ zigzagLevelOrder(self, root
        __ root pa__ None:
            r_   # list
        res =   # list
        queue =   # list
        rev = False  # Reverse direction
        level =   # list
        queue.append(root)
        queue.append(None)
        w___ queue:
            root = queue.pop(0)
            __ root pa__ None:
                __ queue:
                    queue.append(None)
                res.append(level)
                level =   # list
                rev = not rev  # Toggle direction
            ____
                __ rev:
                    level.insert(0, root.val)
                ____
                    level.append(root.val)
                __ root.left pa__ not None:
                    queue.append(root.left)
                __ root.right pa__ not None:
                    queue.append(root.right)
        r_ res
