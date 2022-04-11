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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
    ___ postorderTraversal  root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        p..    # list
        __ root __ N..
            r.. p..
        stack1    # list
        stack2    # list
        stack1.a..(root)
        w.... stack1:
            root stack1.p.. )
            stack2.a..(root.val)
            __ root.left __ n.. N..
                stack1.a..(root.left)
            __ root.right __ n.. N..
                stack1.a..(root.right)
        w.... stack2:
            p...a..(stack2.pop
        r.. p..
