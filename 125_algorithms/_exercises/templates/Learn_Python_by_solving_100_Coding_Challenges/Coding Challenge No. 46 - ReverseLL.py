# Reverse a Linked List
# Question: Given a Linked List, reverse it..
# Solutions:


c_ ListNode:
    ___  -(self, val, next_None):
        val _ val
        next _ next


c_ Solution:
    # @param {ListNode} head
    # @return {ListNode}

    ___ reverseList(self, head):
        result _ N..
        node _ head
        w___ node !_ N..:
            tmp _ node.next
            node.next _ result
            result _ node
            node _ tmp
        r_ result

    ___ printll(self, node):
        w___ node:
            print ( node.val )
            node _ node.next


l4 _ ListNode(4)
l3 _ ListNode(3,l4)
l2 _ ListNode(2,l3)
l1 _ ListNode(1,l2)
l0 _ ListNode(5,l1)

result0 _ Solution().reverseList(l0)
Solution().printll(result0)