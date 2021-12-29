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
    1. recursion from right to left
    2. first scan the nxt by level
    """
    ___ connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: void
        """
        __ n.. root:
            r..

        # scan the nxt by level
        head = root.next
        nxt = N..

        while head and n.. nxt:
            __ head.left:
                nxt = head.left
            ____ head.right:
                nxt = head.right
            ____:
                head = head.next

        __ root.right:
            root.right.next = nxt
            nxt = root.right

        __ root.left:
            root.left.next = nxt

        self.connect(root.right)
        self.connect(root.left)


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

        dummy = TreeLinkNode(0)
        dummy.next = root
        nxt = tail = N..

        while dummy.next:
            tail = dummy
            nxt = dummy.next
            dummy.next = N..

            while nxt:
                __ nxt.left:
                    tail.next = nxt.left
                    tail = tail.next

                __ nxt.right:
                    tail.next = nxt.right
                    tail = tail.next

                nxt = nxt.next


class Solution:
    """
    Level Traversal
    """
    ___ connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: void
        """
        __ n.. root:
            r..

        queue, _queue = [root], []

        while queue:
            n = l..(queue)

            ___ i __ r..(n):
                __ i < n - 1:
                    queue[i].next = queue[i + 1]

                __ queue[i].left:
                    _queue.a..(queue[i].left)

                __ queue[i].right:
                    _queue.a..(queue[i].right)

            queue, _queue = _queue, []
