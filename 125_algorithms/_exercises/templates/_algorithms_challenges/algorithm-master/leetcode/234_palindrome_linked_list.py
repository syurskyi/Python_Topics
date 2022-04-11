# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


c_ Solution:
    ___ isPalindrome  head
        """
        :type head: ListNode
        :rtype: bool
        """
        rev N..
        slow fast head

        w.... fast a.. fast.next:
            fast fast.next.next
            rev, rev.next, slow slow, rev, slow.next

        __ fast:
            slow slow.next

        w.... slow a.. slow.val __ rev.val:
            slow slow.next
            rev rev.next

        r.. n.. rev


c_ Solution:
    ___ isPalindrome  head
        """
        :type head: ListNode
        :rtype: bool
        """
        rev nxt N..
        slow fast head

        w.... fast a.. fast.next:
            fast fast.next.next

            nxt slow.next
            slow.next rev
            rev slow
            slow nxt

        __ fast:
            slow slow.next

        w.... slow a.. slow.val __ rev.val:
            slow slow.next
            rev rev.next

        r.. n.. rev
