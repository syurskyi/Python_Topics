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
        __ not root:
            return

        # scan the nxt by level
        head = root.next
        nxt = None

        while head and not nxt:
            __ head.left:
                nxt = head.left
            elif head.right:
                nxt = head.right
            else:
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
        __ not root:
            return

        dummy = TreeLinkNode(0)
        dummy.next = root
        nxt = tail = None

        while dummy.next:
            tail = dummy
            nxt = dummy.next
            dummy.next = None

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
        __ not root:
            return

        queue, _queue = [root], []

        while queue:
            n = len(queue)

            for i in range(n):
                __ i < n - 1:
                    queue[i].next = queue[i + 1]

                __ queue[i].left:
                    _queue.append(queue[i].left)

                __ queue[i].right:
                    _queue.append(queue[i].right)

            queue, _queue = _queue, []
