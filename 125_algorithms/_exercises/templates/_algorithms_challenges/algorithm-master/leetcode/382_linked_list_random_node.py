# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

from random ______ randint


class Solution:
    ___ __init__(self, head
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    ___ getRandom(self
        """
        Returns a random node's value.
        :rtype: int
        """
        res = node = self.head
        i = 0

        w___ node:
            __ randint(0, i) __ i:
                res = node
            node = node.next
            i += 1

        r_ res.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
