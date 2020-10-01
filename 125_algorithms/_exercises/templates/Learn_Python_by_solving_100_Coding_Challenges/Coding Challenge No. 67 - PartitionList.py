# Partition List
# Question: Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5
# Solutions:


c_ ListNode:
    ___  -(, x, next_None):
        val _ x
        next _ next


c_ Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    ___ partition(, head, x):
        smaller _ ListNode(-1)
        others _ ListNode(-1)
        smallerLast, othersLast _ smaller, others
        w___ head !_ N..:
            __ head.val < x:
                smallerLast.next _ head
                smallerLast _ smallerLast.next
            ____
                othersLast.next _ head
                othersLast _ othersLast.next
            head _ head.next
        smallerLast.next _ others.next
        othersLast.next _ N..
        r_ smaller.next

    ___ printll(, node):
        w___ node:
            print ( node.val )
            node _ node.next


__  -n __ '__main__':
    node6 _ ListNode(2)
    node5 _ ListNode(5, node6)
    node4 _ ListNode(2, node5)
    node3 _ ListNode(3, node4)
    node2 _ ListNode(4, node3)
    ll1 _ ListNode(1, node2)
    Solution().printll( Solution().partition(ll1,3) )