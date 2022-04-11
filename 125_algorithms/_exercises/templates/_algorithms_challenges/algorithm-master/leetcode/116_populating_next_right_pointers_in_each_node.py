"""
Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
"""


c_ Solution:
    """
    Recursion
    """
    ___ connect  root
        """
        :type root: TreeLinkNode
        :rtype: void
        """
        __ n.. root:
            r..

        __ root.left:
            root.left.next root.right

        __ root.right a.. root.next:
            root.right.next root.next.left

        # leave to None if root.right: root.right.next = None

        connect(root.left)
        connect(root.right)


c_ Solution:
    """
    Iteration
    """
    ___ connect  root
        """
        :type root: TreeLinkNode
        :rtype: void
        """
        __ n.. root:
            r..

        head root
        nxt N..

        # this loop only for find left
        w.... head:
            nxt head
            head nxt.left

            # this loop find for every next, do level move
            w.... nxt:
                __ nxt.left:
                    nxt.left.next nxt.right

                __ nxt.right a.. nxt.next:
                    nxt.right.next nxt.next.left

                nxt nxt.next
