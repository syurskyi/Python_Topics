# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

____ r__ _______ r..


c_ Solution:
    ___ - , head
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        head = head

    ___ getRandom
        """
        Returns a random node's value.
        :rtype: int
        """
        res = node = head
        i = 0

        w.... node:
            __ r..(0, i) __ i:
                res = node
            node = node.next
            i += 1

        r.. res.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
