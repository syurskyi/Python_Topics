# Reverse a Linked List
# Question: Given a Linked List, reverse it..
# Solutions:


class ListNode:
    ___ __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    # @param {ListNode} head
    # @return {ListNode}

    ___ reverseList(self, head):
        result = None
        node = head
        while node != None:
            tmp = node.next
            node.next = result
            result = node
            node = tmp
        r_ result

    ___ printll(self, node):
        while node:
            print ( node.val )
            node = node.next


l4 = ListNode(4)
l3 = ListNode(3,l4)
l2 = ListNode(2,l3)
l1 = ListNode(1,l2)
l0 = ListNode(5,l1)

result0 = Solution().reverseList(l0)
Solution().printll(result0)