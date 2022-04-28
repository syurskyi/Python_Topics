# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    ___ reverseBetween  head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        __ m __ n:
            r_ head
        split_node, prev, curr = N.., N.., head
        count = 1
        w.. count <= m and curr is not N..:
            __ count __ m:
                split_node = prev
            prev = curr
            curr = curr.next
            count += 1
        tail, next_node = prev, N..
        w.. curr is not N.. and count <= n:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            count += 1
        __ split_node is not N..:
            split_node.next = prev
        __ tail is not N..:
            tail.next = curr
        __ m __ 1:
            r_ prev
        r_ head

        