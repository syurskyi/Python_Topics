# Copy linked list with random pointer
# Question: A linked list is given such that each node contains an additional random pointer which could point to any
# node in the list or null.
# Return a deep copy of the list.
# Solutions:


class RandomListNode:
    ___ __init__(self, x):
        self.val _ x
        self.next _ None
        self.random _ None


class Solution:
    # @param ll, a RandomListNode
    # @return a RandomListNode

    ___ copyRandomList(self, ll):
        # copy and combine copied list with original list
        current _ ll
        while current:
            copied _ RandomListNode(current.val)
            copied.next _ current.next
            current.next _ copied
            current _ copied.next

        # update random node in copied list
        current _ ll
        while current:
            __ current.random:
                current.next.random _ current.random.next
            current _ current.next.next

        # split copied list from combined one
        dummy _ RandomListNode(0)
        copied_current, current _ dummy, ll
        while current:
            copied_current.next _ current.next
            current.next _ current.next.next
            copied_current, current _ copied_current.next, current.next
        r_ dummy.next


__  -n __ "__main__":
    ll, ll.next _ RandomListNode(1), RandomListNode(2),
    ll.random _ ll.next
    result _ Solution().copyRandomList(ll)
    print ( result.val )
    print ( result.next.val )
    print ( result.random.val )