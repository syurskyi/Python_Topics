# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    # def mergeKLists(self, lists):
    #     # Priority queue
    #     from Queue import PriorityQueue
    #     queue = PriorityQueue()
    #     for l in lists:
    #         while l is not None:
    #             queue.put((l.val, l))
    #             l = l.next
    #     p = dummyHead = ListNode(-1)
    #     while queue.qsize() > 0:
    #         p.next = queue.get()[1]
    #         p = p.next
    #     p.next = None
    #     return dummyHead.next


    # def mergeKLists(self, lists):
    #     """
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     # sort
    #     v_map = {}
    #     # hash
    #     for l in lists:
    #         while l is not None:
    #             try:
    #                 v_map[l.val].append(l)
    #             except KeyError:
    #                 v_map[l.val] = [l]
    #             l = l.next
    #     head = last = ListNode(-1)
    #     # sort and connect
    #     for k in sorted(v_map.keys()):
    #         for t in v_map[k]:
    #             last.next = t
    #             last = t
    #     last.next = None
    #     return head.next




    ___ mergeKLists  lists):
        # recursive
        __ lists is N..:
            r_ N..
        ____ l.. lists) __ 0:
            r_ N..
        r_ mergeK(lists, 0, l.. lists) - 1)

    ___ mergeK  lists, low, high):
        __ low __ high:
            r_ lists[low]
        ____ low + 1 __ high:
            r_ mergeTwolists(lists[low], lists[high])
        mid = (low + high) / 2
        r_ mergeTwolists(mergeK(lists, low, mid), mergeK(lists, mid + 1, high))

    ___ mergeTwolists  l1, l2):
        __ l1 is N..:
            r_ l2
        __ l2 is N..:
            r_ l1
        head = curr = ListNode(-1)
        w.. l1 is not N.. and l2 is not N..:
            __ l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            ____
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        __ l1 is not N..:
            curr.next = l1
        __ l2 is not N..:
            curr.next = l2
        r_ head.next




