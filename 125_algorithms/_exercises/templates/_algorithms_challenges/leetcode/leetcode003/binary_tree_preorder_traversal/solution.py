"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3

return [1,2,3].

"""

# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
    ___ preorderTraversal(self, root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        __ root pa__ None:
            r_ path
        stack = []
        stack.append(root)
        w___ stack:
            root = stack.p..
            path.append(root.val)
            __ root.right pa__ not None:
                stack.append(root.right)
            __ root.left pa__ not None:
                stack.append(root.left)
        r_ path
