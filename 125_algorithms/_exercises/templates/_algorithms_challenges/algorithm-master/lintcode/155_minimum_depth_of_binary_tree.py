"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """
    ___ minDepth(self, root):
        ans = 0
        __ n.. root:
            r.. ans

        queue = [root]
        while queue:
            _queue    # list
            ans += 1

            ___ node __ queue:
                __ n.. node.left and n.. node.right:
                    r.. ans
                __ node.left:
                    _queue.a..(node.left)
                __ node.right:
                    _queue.a..(node.right)

            queue = _queue

        r.. ans


class Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """
    ___ minDepth(self, root):
        __ n.. root:
            r.. 0

        __ n.. root.left and n.. root.right:
            r.. 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        __ left __ 0:
            r.. right + 1
        __ right __ 0:
            r.. left + 1

        r.. m..(left, right) + 1
