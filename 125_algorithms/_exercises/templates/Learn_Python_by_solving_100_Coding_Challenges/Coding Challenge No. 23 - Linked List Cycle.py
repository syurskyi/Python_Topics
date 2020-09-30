# Linked List Cycle
# Question: Given a linked list, determine if it has a cycle in it
# Solutions:


class ListNode:
    ___ __init__(self, x):
        self.val _ x
        self.next _ None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    ___ hasCycle(self, head):
        __ head __ None or head.next __ None:
            r_ F..
        slow _ fast _ head
        while fast an. fast.next:
            slow _ slow.next
            fast _ fast.next.next
            __ slow __ fast:
                r_ T..
        r_ F..

__  -n __ '__main__':
    ll, ll.next, ll.next.next _ ListNode(2), ListNode(4), ListNode(3),
    ll.next.next.next _ ll.next
    print( Solution().hasCycle(ll) )