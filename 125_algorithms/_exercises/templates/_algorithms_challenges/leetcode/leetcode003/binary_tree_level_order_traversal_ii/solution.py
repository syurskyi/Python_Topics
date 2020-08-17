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
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
    ___ levelOrderBottom(self, root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = []
        __ root pa__ None:
            r_ stack
        queue = []
        level = []
        queue.append(root)
        queue.append(None)
        w___ queue:
            root = queue.pop(0)
            __ root pa__ None:
                stack.append(level[:])
                level = []
                __ queue:
                    queue.append(None)
            ____
                level.append(root.val)
                __ root.left pa__ not None:
                    queue.append(root.left)
                __ root.right pa__ not None:
                    queue.append(root.right)
        res = []
        w___ stack:
            res.append(stack.pop())
        r_ res
