"""
The path could be start and end at any node in the tree


If use top down in this case, still need return the result from bottom
=> just use bottom up


Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    Bottom Up
    """
    ___ longestConsecutive2(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root:
            r_ 0

        r_ self.divide_conquer(root)[0]

    ___ divide_conquer(self, node
        __ not node:
            r_ 0, 0, 0

        size = 1
        up = down = 0

        ___ branch in ('left', 'right'
            child = getattr(node, branch)

            __ not child:
                continue

            _size, _up, _down = self.divide_conquer(child)

            __ child.val + 1 __ node.val and _up + 1 > up:
                up = _up + 1

            __ child.val - 1 __ node.val and _down + 1 > down:
                down = _down + 1

            __ _size > size:
                size = _size

        __ up + down + 1 > size:
            size = up + down + 1

        r_ size, up, down
