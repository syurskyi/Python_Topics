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
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    ___ detectCycle(self, head
        """
        example: 1->2->3
                    ^  v
                    5<-4

        * h: head, s: slow, f: fast, i: intersection node

        r1/
            s    f
            1 -> 2 -> 3
                 ^    v
                 5 <- 4

        r2/
                 s
            1 -> 2 -> 3
                 ^    v
                 5 <- 4  f

        r3/
                 f    s
            1 -> 2 -> 3
                 ^    v
                 5 <- 4

        r4/
            h    i
            1 -> 2 -> 3
                 ^    v
                 5 <- 4  s, f

        h->i == 1
        s->i == 2
        """
        __ not head or not head.next:
            r_

        """
        if its a cycle, and then we can ensure
        the 2-pace pointer and the 1-pace pointer
        will eventually meet
        otherwise its a list => at some point there will be no `node.next`
        """
        slow, fast = head, head.next
        w___ slow pa__ not fast:
            __ not fast or not fast.next:
                r_
            slow = slow.next
            fast = fast.next.next

        """
        at this point, slow meet fast
        and at the intersection node
        the steps from the first node is equal to from meet node plus 1
        """
        w___ head pa__ not slow.next:
            head = head.next
            slow = slow.next

        r_ head
