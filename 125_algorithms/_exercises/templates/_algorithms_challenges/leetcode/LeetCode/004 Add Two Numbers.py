"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each
of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

__author__ = 'Danyang'


class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None

    ___ __repr__(self
        # for debugging
        r_ repr(self.val)


class Solution:
    ___ addTwoNumbers(self, l1, l2
        """
        Algorithm: Two pointers & ma__
        Two pointers for l1 and l2 respectively
        Math - carry for addition, in the form of new node

        :param l1: linked list head node
        :param l2: linked list head node
        :return: ListNode
        """
        result_head = ListNode(0)

        cur1 = l1
        cur2 = l2
        cur = result_head
        w___ cur1 or cur2:
            cur.val = cur.val+self.addNode(cur1, cur2)
            __ cur.val < 10:
                __ cur1 and cur1.next or cur2 and cur2.next:  # next node
                    cur.next = ListNode(0)
            ____
                cur.val -= 10
                cur.next = ListNode(1)

            __ cur1:
                cur1 = cur1.next
            __ cur2:
                cur2 = cur2.next
            cur = cur.next

        r_ result_head

    ___ addNode(self, node1, node2
        """
        Handles None situation

        :param node1: ListNode
        :param node2: ListNode
        :return: integer, summation
        """
        __ not node1 and not node2:
            raise Exception("two nodes are None")
        __ not node1:
            r_ node2.val
        __ not node2:
            r_ node1.val
        r_ node1.val+node2.val


__ __name__ __ "__main__":
    l1s = [ListNode(1)]
    l2s = [ListNode(9), ListNode(9)]
    for i in range(le.(l1s)-1
        l1s[i].next = l1s[i+1]
    for i in range(le.(l2s)-1
        l2s[i].next = l2s[i+1]
    Solution().addTwoNumbers(l1s[0], l2s[0])
