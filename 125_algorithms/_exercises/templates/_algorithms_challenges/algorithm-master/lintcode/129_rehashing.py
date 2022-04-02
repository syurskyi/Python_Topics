"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


c_ Solution:
    """
    @param hash_table: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    ___ rehashing  hash_table
        __ n.. hash_table:
            r..

        CAPACITY = l..(hash_table) * 2
        heads = [N..] * CAPACITY
        tails = [N..] * CAPACITY

        curr = _node = i = N..
        ___ node __ hash_table:
            curr = node

            w.... curr:
                i = curr.val % CAPACITY
                _node = ListNode(curr.val)

                __ heads[i]:
                    tails[i].next = _node
                ____:
                    heads[i] = _node

                tails[i] = _node

                curr = curr.next

        r.. heads
