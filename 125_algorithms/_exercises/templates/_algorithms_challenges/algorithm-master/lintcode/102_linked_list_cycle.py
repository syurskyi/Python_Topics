"""
Definition of ListNode
class ListNode(object
    ___ __init__(self, val, next=None
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    ___ hasCycle(self, head
        """
        if its a cycle, and then we can ensure
        the 2-pace pointer and the 1-pace pointer
        will eventually meet
        otherwise its a list => at some point there will be no `node.next`
        """
        __ not head or not head.next:
            r_ False

        slow = head
        fast = head.next
        w___ slow != fast:
            __ not fast.next or not fast.next.next:
                r_ False

            slow = slow.next
            fast = fast.next.next

        r_ True
