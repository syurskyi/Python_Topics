# Copy linked list with random pointer
# Question: A linked list is given such that each node contains an additional random pointer which could point to any
# node in the list or null.
# Return a deep copy of the list.
# Solutions:


c_ RandomListNode:
    ___  - , x:
        val _ x
        next _ N..
        ra__ _ N..


c_ Solution:
    # @param ll, a RandomListNode
    # @return a RandomListNode

    ___ copyRandomList , ll:
        # copy and combine copied list with original list
        current _ ll
        w___ current:
            copied _ RandomListNode current.val
            copied.next _ current.next
            current.next _ copied
            current _ copied.next

        # update random node in copied list
        current _ ll
        w___ current:
            __ current.ra__:
                current.next.ra__ _ current.ra__.next
            current _ current.next.next

        # split copied list from combined one
        dummy _ RandomListNode 0
        copied_current, current _ dummy, ll
        w___ current:
            copied_current.next _ current.next
            current.next _ current.next.next
            copied_current, current _ copied_current.next, current.next
        r_ dummy.next


__  -n __ "__main__":
    ll, ll.next _ RandomListNode 1, RandomListNode 2,
    ll.ra__ _ ll.next
    result _ Solution .copyRandomList ll
    print   result.val
    print   result.next.val
    print   result.ra__.val