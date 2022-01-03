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

c_ Solution(object):
    ___ postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path    # list
        __ root __ N..
            r.. path
        stack1    # list
        stack2    # list
        stack1.a..(root)
        w.... stack1:
            root = stack1.pop()
            stack2.a..(root.val)
            __ root.left __ n.. N..
                stack1.a..(root.left)
            __ root.right __ n.. N..
                stack1.a..(root.right)
        w.... stack2:
            path.a..(stack2.pop())
        r.. path
