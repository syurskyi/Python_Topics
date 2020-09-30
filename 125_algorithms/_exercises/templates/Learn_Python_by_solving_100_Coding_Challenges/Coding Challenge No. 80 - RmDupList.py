# Remove Duplicates from Sorted List
# Question: Given a sorted linked list, delete all duplicates such that each element appear only once.
# For example:
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
# Solutions:


class ListNode:
    ___ __init__(self, x):
        self.val _ x
        self.next _ N..


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    ___ deleteDuplicates(self, head):
        __ head __ N.. or head.next __ N..:
            r_ head
        p _ head
        while p.next:
            __ p.val __ p.next.val:
                p.next _ p.next.next
            ____
                p _ p.next
        r_ head

    ___ printll(self, node):
        while node:
            print ( node.val )
            node _ node.next


__  -n __ '__main__':
    ll1, ll1.next, ll1.next.next _ ListNode(2), ListNode(2), ListNode(5)
    Solution().printll( Solution().deleteDuplicates(ll1) )