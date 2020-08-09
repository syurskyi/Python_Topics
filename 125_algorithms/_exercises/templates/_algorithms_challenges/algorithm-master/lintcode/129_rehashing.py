"""
Definition of ListNode
class ListNode(object

    ___ __init__(self, val, next=None
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param hash_table: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    ___ rehashing(self, hash_table
        __ not hash_table:
            r_

        CAPACITY = le.(hash_table) * 2
        heads = [None] * CAPACITY
        tails = [None] * CAPACITY

        curr = _node = i = None
        for node in hash_table:
            curr = node

            w___ curr:
                i = curr.val % CAPACITY
                _node = ListNode(curr.val)

                __ heads[i]:
                    tails[i].next = _node
                ____
                    heads[i] = _node

                tails[i] = _node

                curr = curr.next

        r_ heads
