"""
Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
"""


class Solution:
    """
    Recursion
    """
    ___ connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: void
        """
        __ n.. root:
            r..

        __ root.left:
            root.left.next = root.right

        __ root.right a.. root.next:
            root.right.next = root.next.left

        # leave to None if root.right: root.right.next = None

        self.connect(root.left)
        self.connect(root.right)


class Solution:
    """
    Iteration
    """
    ___ connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: void
        """
        __ n.. root:
            r..

        head = root
        nxt = N..

        # this loop only for find left
        w.... head:
            nxt = head
            head = nxt.left

            # this loop find for every next, do level move
            w.... nxt:
                __ nxt.left:
                    nxt.left.next = nxt.right

                __ nxt.right a.. nxt.next:
                    nxt.right.next = nxt.next.left

                nxt = nxt.next
