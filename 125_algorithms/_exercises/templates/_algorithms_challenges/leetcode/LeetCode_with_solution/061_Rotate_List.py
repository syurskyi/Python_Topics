# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    ___ rotateRight  head, k
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        __ n.. head or k __ 0:
            r_ head

        slow = fast = head
        length = 1

        w.. k and fast.next:
            fast = fast.next
            length += 1
            k -= 1

        __ k != 0:
            k = (k + length - 1) % length # original k % length
            r_ rotateRight(head, k)
        ____
            w.. fast.next:
                fast = fast.next
                slow = slow.next
            r_ rotate(head, fast, slow)

    ___ rotate  head, fast, slow
        fast.next = head
        head = slow.next
        slow.next = N..
        r_ head