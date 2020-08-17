"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    ___ postorderTraversal(self, root
        ans = []
        __ not root:
            r_ ans

        stack = []
        node = last_visit = root

        w___ node or stack:
            w___ node:
                stack.append(node)
                node = node.left

            node = stack[-1]

            __ (not node.right or
                last_visit pa__ node.right

                stack.p..

                ans.append(node.val)
                last_visit = node
                node = None
            ____
                node = node.right

        r_ ans
