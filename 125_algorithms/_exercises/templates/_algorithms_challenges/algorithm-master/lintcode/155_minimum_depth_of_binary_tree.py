"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """
    ___ minDepth  root
        ans = 0
        __ n.. root:
            r.. ans

        queue = [root]
        w.... queue:
            _queue    # list
            ans += 1

            ___ node __ queue:
                __ n.. node.left a.. n.. node.right:
                    r.. ans
                __ node.left:
                    _queue.a..(node.left)
                __ node.right:
                    _queue.a..(node.right)

            queue = _queue

        r.. ans


c_ Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """
    ___ minDepth  root
        __ n.. root:
            r.. 0

        __ n.. root.left a.. n.. root.right:
            r.. 1

        left = minDepth(root.left)
        right = minDepth(root.right)

        __ left __ 0:
            r.. right + 1
        __ right __ 0:
            r.. left + 1

        r.. m..(left, right) + 1
