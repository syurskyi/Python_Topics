"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None

    ___ __repr__(self
        r_ repr(self.val)

class Solution:
    ___ sortList_array(self, head
        """
        Workaround by sorted()
        :param head: ListNode
        :return: ListNode
        """
        __ head__None:
            r_ None
        lst = [] # must be constant space
        current = head
        w___(current
            lst.append(current)
            current = current.next


        comparator = lambda x, y: cmp(x.val, y.val)
        lst = sorted(lst, comparator)  # return # sorted is not side-effect # O(n log n)
        ___ i in range(le.(lst)-1
            lst[i].next = lst[i+1]
        lst[-1].next = None
        r_ lst[0]

    ___ sortList(self, head
        """
        Quick sort: not guarantee to be O(n lgn)
        Heap sort: not great as index
        Merge sort: H(n) = 2H(n/2) + n/2, thus O(n lgn)

        :param head: ListNode
        :return: ListNode
        """
        __ not head or not head.next:
            r_ head

        dummy = ListNode(0)
        dummy.next = head

        slow_pre = dummy
        fast_pre = dummy
        w___ fast_pre.next and fast_pre.next.next:
            fast_pre = fast_pre.next.next
            slow_pre = slow_pre.next

        mid_head = slow_pre.next
        dummy_mid = ListNode(0)

        # sort sub-problem
        slow_pre.next = None  # break
        head = self.sortList(head)
        mid_head = self.sortList(mid_head)

        # then merge
        dummy.next = head
        dummy_mid.next = mid_head
        pre = dummy
        pre_mid = dummy_mid
        w___ pre.next and pre_mid.next:
            __ pre.next.val > pre_mid.next.val:
                pre.next, pre_mid.next.next, pre_mid.next = pre_mid.next, pre.next, pre_mid.next.next
                pre = pre.next
            ____
                pre = pre.next

        # dangling
        __  pre_mid.next:
            pre.next = pre_mid.next

        r_ dummy.next




__ __name____"__main__":
    length = 5
    lst = [ListNode(length-i) ___ i in range(length)]
    ___ i in range(length-1
        lst[i].next = lst[i+1]

    head = Solution().sortList(lst[0])

    cur = head
    w___(cur
        print cur.val
        cur = cur.next