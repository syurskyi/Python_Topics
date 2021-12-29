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
        __ not root:
            return

        __ root.left:
            root.left.next = root.right

        __ root.right and root.next:
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
        __ not root:
            return

        head = root
        nxt = None

        # this loop only for find left
        while head:
            nxt = head
            head = nxt.left

            # this loop find for every next, do level move
            while nxt:
                __ nxt.left:
                    nxt.left.next = nxt.right

                __ nxt.right and nxt.next:
                    nxt.right.next = nxt.next.left

                nxt = nxt.next
