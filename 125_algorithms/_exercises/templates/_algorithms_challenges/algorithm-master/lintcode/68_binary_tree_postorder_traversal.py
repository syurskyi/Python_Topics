"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    ___ postorderTraversal(self, root):
        ans    # list
        __ n.. root:
            r.. ans

        stack    # list
        node = last_visit = root

        w.... node o. stack:
            w.... node:
                stack.a..(node)
                node = node.left

            node = stack[-1]

            __ (n.. node.right o.
                last_visit __ node.right):

                stack.pop()

                ans.a..(node.val)
                last_visit = node
                node = N..
            ____:
                node = node.right

        r.. ans
