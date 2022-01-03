"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each
of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

__author__ = 'Danyang'


c_ ListNode:
    ___ - , x):
        val = x
        next = N..

    ___ __repr__
        # for debugging
        r.. repr(val)


c_ Solution:
    ___ addTwoNumbers(self, l1, l2):
        """
        Algorithm: Two pointers & math
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
        w.... cur1 o. cur2:
            cur.val = cur.val+addNode(cur1, cur2)
            __ cur.val < 10:
                __ cur1 a.. cur1.next o. cur2 a.. cur2.next:  # next node
                    cur.next = ListNode(0)
            ____:
                cur.val -= 10
                cur.next = ListNode(1)

            __ cur1:
                cur1 = cur1.next
            __ cur2:
                cur2 = cur2.next
            cur = cur.next

        r.. result_head

    ___ addNode(self, node1, node2):
        """
        Handles None situation

        :param node1: ListNode
        :param node2: ListNode
        :return: integer, summation
        """
        __ n.. node1 a.. n.. node2:
            raise Exception("two nodes are None")
        __ n.. node1:
            r.. node2.val
        __ n.. node2:
            r.. node1.val
        r.. node1.val+node2.val


__ __name__ __ "__main__":
    l1s = [ListNode(1)]
    l2s = [ListNode(9), ListNode(9)]
    ___ i __ r..(l..(l1s)-1):
        l1s[i].next = l1s[i+1]
    ___ i __ r..(l..(l2s)-1):
        l2s[i].next = l2s[i+1]
    Solution().addTwoNumbers(l1s[0], l2s[0])
