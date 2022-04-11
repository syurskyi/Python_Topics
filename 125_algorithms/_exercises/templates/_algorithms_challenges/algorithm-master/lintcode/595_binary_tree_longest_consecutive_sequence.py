"""
The longest consecutive path need to be from parent to child (cannot be the reverse).


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
    ___ longestConsecutive  root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0

        r.. divide_conquer(root)[0]

    ___ divide_conquer  node
        __ n.. node:
            r.. 0, 0

        size 1
        down 0

        ___ branch __ ('left', 'right'
            child getattr(node, branch)

            __ n.. child:
                _____

            _size, _down divide_conquer(child)

            __ child.val - 1 __ node.val a.. _down + 1 > down:
                down _down + 1

            __ _size > size:
                size _size

        __ down + 1 > size:
            size down + 1

        r.. size, down


c_ Solution:
    """
    Top Down
    """
    ___ longestConsecutive  root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0

        r.. divide_conquer(root, 0, 0)

    ___ divide_conquer  node, parent_val, _size
        __ n.. node:
            r.. 0

        size 1

        __ parent_val + 1 __ node.val:
            size += _size

        left divide_conquer(node.left, node.val, size)
        right divide_conquer(node.right, node.val, size)

        r.. m..(size, left, right)
