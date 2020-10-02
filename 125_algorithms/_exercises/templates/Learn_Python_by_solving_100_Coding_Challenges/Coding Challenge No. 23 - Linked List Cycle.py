# Linked List Cycle
# Question: Given a linked list, determine if it has a cycle in it
# Solutions:


c_ ListNode:
    ___  - , x:
        val _ x
        next _ N..


c_ Solution:
    # @param head, a ListNode
    # @return a boolean
    ___ hasCycle , head:
        __ head __ N.. o. head.next __ N..:
            r_ F..
        slow _ fast _ head
        w___ fast an. fast.next:
            slow _ slow.next
            fast _ fast.next.next
            __ slow __ fast:
                r_ T..
        r_ F..

__  -n __ ______
    ll, ll.next, ll.next.next _ ListNode 2, ListNode 4, ListNode 3,
    ll.next.next.next _ ll.next
    print  Solution .hasCycle ll 