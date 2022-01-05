"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


c_ Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    ___ insert  node, x):
        __ n.. node:
            node = ListNode(x)
            node.next = node
            r.. node

        pre, cur = N.., node
        w... T...
            pre = cur
            cur = cur.next

            # in the list
            __ pre.val <= x <= cur.val:
                break

            # at the boundary between minimum and maximum
            __ (pre.val > cur.val) a.. (x < cur.val o. x > pre.val):
                break

            # if `cur` have already traversed the list once
            __ cur __ node:
                break

        new_node = ListNode(x)
        new_node.next = cur
        pre.next = new_node
        r.. new_node
