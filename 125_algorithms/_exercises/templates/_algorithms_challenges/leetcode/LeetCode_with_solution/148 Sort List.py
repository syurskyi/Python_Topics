"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x):
        self.val = x
        self.next = N..

    ___ __repr__(self):
        r.. repr(self.val)

class Solution:
    ___ sortList_array(self, head):
        """
        Workaround by sorted()
        :param head: ListNode
        :return: ListNode
        """
        __ head__N..
            r.. N..
        lst    # list # must be constant space
        current = head
        w....(current):
            lst.a..(current)
            current = current.next


        comparator = l.... x, y: cmp(x.val, y.val)
        lst = s..(lst, comparator)  # return # sorted is not side-effect # O(n log n)
        ___ i __ r..(l..(lst)-1):
            lst[i].next = lst[i+1]
        lst[-1].next = N..
        r.. lst[0]

    ___ sortList(self, head):
        """
        Quick sort: not guarantee to be O(n lgn)
        Heap sort: not great as index
        Merge sort: H(n) = 2H(n/2) + n/2, thus O(n lgn)

        :param head: ListNode
        :return: ListNode
        """
        __ n.. head o. n.. head.next:
            r.. head

        dummy = ListNode(0)
        dummy.next = head

        slow_pre = dummy
        fast_pre = dummy
        w.... fast_pre.next a.. fast_pre.next.next:
            fast_pre = fast_pre.next.next
            slow_pre = slow_pre.next

        mid_head = slow_pre.next
        dummy_mid = ListNode(0)

        # sort sub-problem
        slow_pre.next = N..  # break
        head = self.sortList(head)
        mid_head = self.sortList(mid_head)

        # then merge
        dummy.next = head
        dummy_mid.next = mid_head
        pre = dummy
        pre_mid = dummy_mid
        w.... pre.next a.. pre_mid.next:
            __ pre.next.val > pre_mid.next.val:
                pre.next, pre_mid.next.next, pre_mid.next = pre_mid.next, pre.next, pre_mid.next.next
                pre = pre.next
            ____:
                pre = pre.next

        # dangling
        __  pre_mid.next:
            pre.next = pre_mid.next

        r.. dummy.next




__ __name____"__main__":
    length = 5
    lst = [ListNode(length-i) ___ i __ r..(length)]
    ___ i __ r..(length-1):
        lst[i].next = lst[i+1]

    head = Solution().sortList(lst[0])

    cur = head
    w....(cur):
        print cur.val
        cur = cur.next