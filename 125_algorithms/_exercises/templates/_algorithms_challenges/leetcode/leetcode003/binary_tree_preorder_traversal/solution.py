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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
    ___ preorderTraversal  root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        p..    # list
        __ root __ N..
            r.. p..
        stack    # list
        stack.a..(root)
        w.... stack:
            root = stack.p.. )
            p...a..(root.val)
            __ root.right __ n.. N..
                stack.a..(root.right)
            __ root.left __ n.. N..
                stack.a..(root.left)
        r.. p..
