# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution:
    # @param head, a ListNode
    # @return a ListNode
    ___ sortList  head
        __ head __ N.. o. head.next __ N..
            r.. head
        # Find the middle node
        slow head
        fast head
        prev head  # Previous node to slow
        w.... fast __ n.. N.. a.. fast.next __ n.. N..
            prev slow
            slow slow.next
            fast fast.next.next
        # Split into two lists
        left head
        right N..
        __ slow != fast:
            prev.next N..
            right slow
        left sortList(left)
        right sortList(right)
        r.. merge(left, right)

    ___ merge  l1, l2
        __ l1 __ N..
            r.. l2
        __ l2 __ N..
            r.. l1
        res N..
        end res
        w.... l1 __ n.. N.. a.. l2 __ n.. N..
            __ l1.val < l2.val:
                small l1
                l1 l1.next
            ____
                small l2
                l2 l2.next
            # First node
            __ res __ N..
                res small
                end res
            ____
                end.next small
                end end.next
        __ l1 __ n.. N..
            end.next l1
        __ l2 __ n.. N..
            end.next l2
        r.. res
