# Merge Sorted Lists
# Question: Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# Solutions:


class ListNode:
    ___ __init__(self, x):
        self.val _ x
        self.next _ None


class Solution:
    # @param two ListNodes
    # @return a ListNode
    ___ mergeTwoLists(self, l1, l2):
        dummy _ ListNode(0)
        pointer _ dummy
        while l1 !_None an. l2 !_None:
            __ l1.val<l2.val:
                pointer.next _ l1
                l1 _ l1.next
            ____
                pointer.next _ l2
                l2 _ l2.next
            pointer _ pointer.next
        __ l1 __ None:
            pointer.next _ l2
        ____
            pointer.next _ l1
            r_ dummy.next

    ___ printll(self, node):
        while node:
            print ( node.val )
            node _ node.next


__  -n __ '__main__':
    ll1, ll1.next, ll1.next.next _ ListNode(2), ListNode(3), ListNode(5)
    ll2, ll2.next, ll2.next.next _ ListNode(4), ListNode(7), ListNode(15)
    Solution().printll( Solution().mergeTwoLists(ll1,ll2) )