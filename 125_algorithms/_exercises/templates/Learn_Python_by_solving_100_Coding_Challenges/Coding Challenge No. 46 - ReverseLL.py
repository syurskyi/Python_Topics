# Reverse a Linked List
# Question: Given a Linked List, reverse it..
# Solutions:


class ListNode:
    ___ __init__(self, val, next_None):
        self.val _ val
        self.next _ next


class Solution:
    # @param {ListNode} head
    # @return {ListNode}

    ___ reverseList(self, head):
        result _ None
        node _ head
        while node !_ None:
            tmp _ node.next
            node.next _ result
            result _ node
            node _ tmp
        r_ result

    ___ printll(self, node):
        while node:
            print ( node.val )
            node _ node.next


l4 _ ListNode(4)
l3 _ ListNode(3,l4)
l2 _ ListNode(2,l3)
l1 _ ListNode(1,l2)
l0 _ ListNode(5,l1)

result0 _ Solution().reverseList(l0)
Solution().printll(result0)