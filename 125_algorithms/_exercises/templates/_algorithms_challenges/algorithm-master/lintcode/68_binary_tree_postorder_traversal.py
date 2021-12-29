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
        ans = []
        __ not root:
            return ans

        stack = []
        node = last_visit = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack[-1]

            __ (not node.right or
                last_visit __ node.right):

                stack.pop()

                ans.append(node.val)
                last_visit = node
                node = None
            else:
                node = node.right

        return ans
