"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    ___ hasCycle(self, head):
        """
        if its a cycle, and then we can ensure
        the 2-pace pointer and the 1-pace pointer
        will eventually meet
        otherwise its a list => at some point there will be no `node.next`
        """
        __ n.. head o. n.. head.next:
            r.. False

        slow = head
        fast = head.next
        w.... slow != fast:
            __ n.. fast.next o. n.. fast.next.next:
                r.. False

            slow = slow.next
            fast = fast.next.next

        r.. True
