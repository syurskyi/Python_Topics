"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """
    ___ minDepth(self, root
        ans = 0
        __ not root:
            r_ ans

        queue = [root]
        w___ queue:
            _queue = []
            ans += 1

            for node in queue:
                __ not node.left and not node.right:
                    r_ ans
                __ node.left:
                    _queue.append(node.left)
                __ node.right:
                    _queue.append(node.right)

            queue = _queue

        r_ ans


class Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """
    ___ minDepth(self, root
        __ not root:
            r_ 0

        __ not root.left and not root.right:
            r_ 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        __ left __ 0:
            r_ right + 1
        __ right __ 0:
            r_ left + 1

        r_ min(left, right) + 1
