# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    ___ isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        __ fast:
            slow = slow.next

        while slow and slow.val == rev.val:
            slow = slow.next
            rev = rev.next

        return not rev


class Solution:
    ___ isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = nxt = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next

            nxt = slow.next
            slow.next = rev
            rev = slow
            slow = nxt

        __ fast:
            slow = slow.next

        while slow and slow.val == rev.val:
            slow = slow.next
            rev = rev.next

        return not rev
