# Remove Nth Node from End of List
# Question: Given a linked list, remove the nth node from the end of list and return its head.
# For example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note: Given n will always be valid. Try to do this in one pass.
# Solutions:


c_ ListNode:
    ___  -(self, x):
        val _ x
        next _ N..


c_ Solution:
    ___ getlength(self,head):
        res _ 0
        w___(head):
            res +_ 1
            head _ head.next
        r_ res

    ___ removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        __ getlength(head)__n:
            r_ head.next

        node _ head
        ___ i __ ra..(getlength(head)-n-1):
            node _ node.next
        node.next _ node.next.next
        r_ head

    ___ printll(self, node):
        w___ node:
            print ( node.val )
            node _ node.next


__  -n __ '__main__':
    ll1, ll1.next, ll1.next.next _ ListNode(0), ListNode(1), ListNode(5)
    Solution().printll( Solution().removeNthFromEnd(ll1,2) )