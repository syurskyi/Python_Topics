"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    ___ sortList(self, head):
        r.. self.merge_sort(head)

    ___ quick_sort(self, head):
        __ n.. head o. n.. head.next:
            r.. head

        mid = self.find_middle(head)

        left_dummy = left_tail = ListNode(0)
        mid_dummy = mid_tail = ListNode(0)
        right_dummy = right_tail = ListNode(0)

        w.... head:
            __ head.val < mid.val:
                left_tail.next = head
                left_tail = head
            ____ head.val > mid.val:
                right_tail.next = head
                right_tail = head
            ____:
                mid_tail.next = head
                mid_tail = head
            head = head.next

        left_tail.next = mid_tail.next = right_tail.next = N..

        left_dummy.next = self.quick_sort(left_dummy.next)
        right_dummy.next = self.quick_sort(right_dummy.next)

        dummy = tail = ListNode(0)
        ___ node __ [left_dummy, mid_dummy, right_dummy]:
            tail.next = node.next
            tail = self.get_tail(tail)

        r.. dummy.next

    ___ merge_sort(self, head):
        __ n.. head o. n.. head.next:
            r.. head

        left = head
        mid = self.find_middle(head)
        right = mid.next
        mid.next = N..

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        dummy = tail = ListNode(0)

        w.... left a.. right:
            __ left.val < right.val:
                tail.next = left
                left = left.next
            ____:
                tail.next = right
                right = right.next
            tail = tail.next

        __ left:
            tail.next = left
        ____:
            tail.next = right

        r.. dummy.next

    ___ find_middle(self, head):
        slow, fast = head, head.next

        w.... fast a.. fast.next:
            slow = slow.next
            fast = fast.next.next

        r.. slow

    ___ get_tail(self, head):
        __ n.. head:
            r..

        w.... head.next:
            head = head.next

        r.. head
