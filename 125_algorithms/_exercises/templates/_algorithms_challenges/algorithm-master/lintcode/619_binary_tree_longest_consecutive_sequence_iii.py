"""
The path could be start and end at any node in the tree


Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


c_ Solution:
    """
    Bottom Up
    """
    ___ longestConsecutive3  root
        """
        :type root: MultiTreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0

        r.. divide_conquer(root)[0]

    ___ divide_conquer  node
        __ n.. node:
            r.. 0, 0, 0

        size 1
        up down 0

        ___ child __ node.children:
            __ n.. child:
                _____

            _size, _up, _down divide_conquer(child)

            __ child.val + 1 __ node.val a.. _up + 1 > up:
                up _up + 1

            __ child.val - 1 __ node.val a.. _down + 1 > down:
                down _down + 1

            __ _size > size:
                size _size

        __ up + down + 1 > size:
            size up + down + 1

        r.. size, up, down
