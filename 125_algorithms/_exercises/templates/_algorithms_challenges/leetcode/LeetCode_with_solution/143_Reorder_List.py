# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    # def reorderList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: void Do not return anything, modify head in-place instead.
    #     """
    #     # List as index to rebuild relation
    #     if not head:
    #         return
    #     dmap = []
    #     current = head
    #     while current is not None:
    #         dmap.append(current)
    #         current = current.next
    #     ls = len(dmap)
    #     for i in range(ls / 2):
    #         t = -1 * (i + 1)
    #         dmap[t].next = dmap[i].next
    #         dmap[i].next = dmap[t]
    #     dmap[ls / 2].next = None

    ___ reorderList  head
        # Two points
        __ head is N.. or head.next is N..:
            r_
        p1, p2 = head, head.next
        w.. p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        head2 = p1.next
        p1.next = N..
        p2 = head2.next
        head2.next = N..
        # reverse mid->end to end->mid
        w.. p2:
            temp = p2.next
            p2.next = head2
            head2 = p2
            p2 = temp
        p1, p2 = head, head2
        # merge
        w.. p1:
            temp = p1.next
            p1.next = p2
            p1 = p1.next
            p2 = temp

