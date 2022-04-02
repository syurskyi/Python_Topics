"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
    ___ inorderTraversal  root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        p..    # list
        __ root __ N..
            r.. p..
        stack    # list
        w.... stack o. root __ n.. N..
            __ root __ n.. N..
                stack.a..(root)
                root = root.left
            ____:
                root = stack.pop()
                p...a..(root.val)
                root = root.right
        r.. p..
