# Linked List Cycle II
# Question: Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# Solutions:



c_ ListNode:
    ___  - , val, next_None:
        val _ val
        next _ next


c_ Solution:
    """
    @param head: The first node of the linked list.
    @return: the node where the cycle begins. If there is no cycle, return null
    """

    ___ detectCycle , head:
        __ head __ N.. o. head.next __ N..:
            r_ N..
        slow _ fast _ head
        w___ fast an. fast.next:
            slow _ slow.next
            fast _ fast.next.next
            __ fast __ slow:
                b..
        __ slow __ fast:
            slow _ head
            w___ slow !_ fast:
                slow _ slow.next
                fast _ fast.next
            r_ slow
        r_ N..


__  -n __ '__main__':
    ll, ll.next, ll.next.next _ ListNode 2, ListNode 4, ListNode 3,
    ll.next.next.next _ ll.next
    print  Solution .detectCycle ll.val