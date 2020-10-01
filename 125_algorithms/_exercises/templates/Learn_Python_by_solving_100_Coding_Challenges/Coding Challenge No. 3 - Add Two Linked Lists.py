# Add Two Numbers
# Question: You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Solutions:

c_ ListNode:
    ___  -(, x):
        val _ x
        next _ N..

c_ Solution:
    ___ addTwoNumbers(l1, l2):
        dummy _ ListNode(0)
        current, carry _ dummy, 0
        w___ l1 o. l2:
            val _ carry
            __ l1:
                val +_ l1.val
                l1 _ l1.next
            __ l2:
                val +_ l2.val
                l2 _ l2.next
                carry, val _ val / 10, val % 10
                current.next _ ListNode(val)
                current _ current.next
            __ carry __ 1:
                current.next _ ListNode(1)
            r_ dummy.next

__  -n __ '__main__':
    a, a.next, a.next.next _ ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next _ ListNode(5), ListNode(6), ListNode(4)
    result _ Solution.addTwoNumbers(a, b)
    print ("{0} -> {1} -> {2}".f..(in.(result.val), in.(result.next.val), in.(result.next.next.val