"""
The path could be start and end at any node in the tree


If use top down in this case, still need return the result from bottom
=> just use bottom up


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    Bottom Up
    """
    ___ longestConsecutive2  root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0

        r.. divide_conquer(root)[0]

    ___ divide_conquer  node):
        __ n.. node:
            r.. 0, 0, 0

        size = 1
        up = down = 0

        ___ branch __ ('left', 'right'):
            child = getattr(node, branch)

            __ n.. child:
                _____

            _size, _up, _down = divide_conquer(child)

            __ child.val + 1 __ node.val a.. _up + 1 > up:
                up = _up + 1

            __ child.val - 1 __ node.val a.. _down + 1 > down:
                down = _down + 1

            __ _size > size:
                size = _size

        __ up + down + 1 > size:
            size = up + down + 1

        r.. size, up, down
