# Reverse Nodes in k-Group
# Question: Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is. You may not alter the values in the nodes, only nodes itself may be changed. Only constant memory is allowed.
# For example,
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5.
# Solutions:


c_ ListNode(object):
    ___  -(self, x):
        val _ x
        next _ N..

    ___ to_list
        r_ [val] + next.to_list() __ next ____ [val]


c_ Solution(object):
    ___ reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        __ not head or k <_ 1:
            r_ head
        dummy _ ListNode(-1)
        dummy.next _ head
        temp _ dummy
        while temp:
            temp _ reverseNextK(temp, k)
        r_ dummy.next

    ___ reverseNextK(self, head, k):
        # Check if there are k nodes left
        temp _ head
        ___ i __ ra..(k):
            __ not temp.next:
                r_ N..
            temp _ temp.next

        # The last node when the k nodes reversed
        node _ head.next
        prev _ head
        curr _ head.next
        # Reverse k nodes
        ___ i __ ra..(k):
            nextNode _ curr.next
            curr.next _ prev
            prev _ curr
            curr _ nextNode
        # Connect with head and tail
        node.next _ curr
        head.next _ prev
        r_ node


__  -n __ "__main__":
    n1 _ ListNode(1)
    n2 _ ListNode(2)
    n3 _ ListNode(3)
    n4 _ ListNode(4)
    n5 _ ListNode(5)
    n1.next _ n2
    n2.next _ n3
    n3.next _ n4
    n4.next _ n5
    r _ Solution().reverseKGroup(n1, 3)
    print ( r.to_list() )