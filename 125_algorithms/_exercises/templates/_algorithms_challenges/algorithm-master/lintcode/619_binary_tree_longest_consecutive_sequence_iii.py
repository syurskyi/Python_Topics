"""
The path could be start and end at any node in the tree


Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    """
    Bottom Up
    """
    ___ longestConsecutive3(self, root):
        """
        :type root: MultiTreeNode
        :rtype: int
        """
        __ not root:
            return 0

        return self.divide_conquer(root)[0]

    ___ divide_conquer(self, node):
        __ not node:
            return 0, 0, 0

        size = 1
        up = down = 0

        for child in node.children:
            __ not child:
                continue

            _size, _up, _down = self.divide_conquer(child)

            __ child.val + 1 == node.val and _up + 1 > up:
                up = _up + 1

            __ child.val - 1 == node.val and _down + 1 > down:
                down = _down + 1

            __ _size > size:
                size = _size

        __ up + down + 1 > size:
            size = up + down + 1

        return size, up, down
