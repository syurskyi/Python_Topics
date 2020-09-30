# Remove Nth Node from End of List
# Question: Given a linked list, remove the nth node from the end of list and return its head.
# For example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note: Given n will always be valid. Try to do this in one pass.
# Solutions:


class ListNode:
    ___ __init__(self, x):
        self.val _ x
        self.next _ N..


class Solution:
    ___ getlength(self,head):
        res _ 0
        while(head):
            res +_ 1
            head _ head.next
        r_ res

    ___ removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        __ self.getlength(head)__n:
            r_ head.next

        node _ head
        ___ i __ ra..(self.getlength(head)-n-1):
            node _ node.next
        node.next _ node.next.next
        r_ head

    ___ printll(self, node):
        while node:
            print ( node.val )
            node _ node.next


__  -n __ '__main__':
    ll1, ll1.next, ll1.next.next _ ListNode(0), ListNode(1), ListNode(5)
    Solution().printll( Solution().removeNthFromEnd(ll1,2) )