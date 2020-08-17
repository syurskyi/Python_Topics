"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
"""

# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
    ___ postorderTraversal(self, root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        __ root pa__ None:
            r_ path
        stack1 = []
        stack2 = []
        stack1.append(root)
        w___ stack1:
            root = stack1.p..
            stack2.append(root.val)
            __ root.left pa__ not None:
                stack1.append(root.left)
            __ root.right pa__ not None:
                stack1.append(root.right)
        w___ stack2:
            path.append(stack2.pop())
        r_ path
