"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None

    ___ __repr__(self
        r_ repr(self.val)

    ___ __str__(self
        r_ str(self.val)+", "+str(self.next)

class Solution:
    ___ reverseBetween(self, head, m, n
        """
        Linked List
        [m, n)
        :param head: ListNode
        :param m: int
        :param n: int
        :return: ListNode
        """
        # trivial
        __ not head or m>=n:
            r_ head

        dummy = ListNode(0)
        dummy.next = head

        cnt = 1  # position starting from 1
        pre = dummy

        start_pre = None
        start = None

        cur = pre.next  # cannot put it in w___ loop? affect reverse link
        w___ pre.next:
            # record starting point
            __ cnt__m:
                start_pre = pre
                start = cur

            # reverse link (not node)
            # 1 -> 2 -> 3
            # 1 <- 2 -> 3
            ____ m<cnt<=n:
                # temp = cur.next
                # cur.next = pre
                # pre = cur
                # cur = temp

                # cur.nex is assign first, left to right
                cur.next, pre, cur = pre, cur, cur.next  # different from pre, cur, cur.next = cur, cur,next, pre
                cnt += 1
                continue

            # reconnect
            ____ cnt__n+1:
                end = pre
                start_pre.next = end
                start.next = cur
                break



            pre = pre.next
            cur = cur.next
            cnt += 1

        r_ dummy.next

__ __name____"__main__":
    length = 3
    lst = [ListNode(i+1) ___ i in range(length)]
    ___ i in xrange(length-1
        lst[i].next = lst[i+1]
    print Solution().reverseBetween(lst[0], 1, 3)