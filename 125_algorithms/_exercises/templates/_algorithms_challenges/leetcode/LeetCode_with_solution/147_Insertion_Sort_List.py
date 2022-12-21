# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    ___ insertionSortList  head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # https://discuss.leetcode.com/topic/8570/an-easy-and-clear-way-to-sort-o-1-space
        __ head is N..:
            r_ N..
        helper = ListNode(-1000)
        pre, curr = helper, head
        w.. curr is n.. N..:
            next_step = curr.next
            w.. pre.next a.. pre.next.val < curr.val:
                pre = pre.next
            curr.next = pre.next
            pre.next = curr
            pre = helper
            curr = next_step
        r_ helper.next
