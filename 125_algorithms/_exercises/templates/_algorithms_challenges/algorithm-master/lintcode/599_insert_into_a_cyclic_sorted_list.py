"""
Definition of ListNode
class ListNode(object

    ___ __init__(self, val, next=None
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    ___ insert(self, node, x
        __ not node:
            node = ListNode(x)
            node.next = node
            r_ node

        pre, cur = None, node
        w___ True:
            pre = cur
            cur = cur.next

            # in the list
            __ pre.val <= x <= cur.val:
                break

            # at the boundary between minimum and maximum
            __ (pre.val > cur.val) and (x < cur.val or x > pre.val
                break

            # if `cur` have already traversed the list once
            __ cur pa__ node:
                break

        new_node = ListNode(x)
        new_node.next = cur
        pre.next = new_node
        r_ new_node
