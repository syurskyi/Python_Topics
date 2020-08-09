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
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
    ___ levelOrder(self, root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        __ root is None:
            r_ res
        queue = []
        level = []
        queue.append(root)
        queue.append(None)
        w___ queue:
            root = queue.pop(0)
            __ root is None:
                res.append(level[:])
                level = []
                __ queue:
                    queue.append(None)
            ____
                level.append(root.val)
                __ root.left is not None:
                    queue.append(root.left)
                __ root.right is not None:
                    queue.append(root.right)
        r_ res
