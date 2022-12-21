# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


c_ Solution o..
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     # iteratively
    #     if head is None:
    #         return
    #     stack = []
    #     pos = start = head
    #     while pos is not None:
    #         stack.append(pos)
    #         pos = pos.next
    #     while len(stack) > 0:
    #         if len(stack) >= 2:
    #             stack[0].val, stack[-1].val = stack[-1].val, stack[0].val
    #             stack.pop(0)
    #             stack.pop()
    #         else:
    #             stack.pop()
    #     return head
    #
    # def reverseList(self, head):
    #     # recursively
    #     if head is None:
    #         return head
    #     stack = []
    #     pos = head
    #     while pos is not None:
    #         stack.append(pos)
    #         pos = pos.next
    #     pre_head = ListNode(-1)
    #     self.do_reverse(stack, pre_head)
    #     return pre_head.next
    #
    # def do_reverse(self, stack, curr_head):
    #     if len(stack) == 0:
    #         curr_head.next = None
    #         return
    #     node = stack.pop()
    #     curr_head.next = node
    #     curr_head = node
    #     self.do_reverse(stack, curr_head)

    # def reverseList(self, head):
    #     # simple iteratively without extra space
    #     prev, curr = None, head
    #     while curr is not None:
    #         next_temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next_temp
    #     return prev

    ___ reverseList  head
        # recursion
        # simple recursively without extra space
        __ head is N.. or head.next is N..:
            r_ head
        p = reverseList(head.next)
        head.next.next = head
        head.next = N..
        r_ p
