# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None


c_ Solution:

    ___ mergeTwoLists(, l1, l2
        cur _ ListNode(0)
        ans _ cur

        w___(l1 a.. l2
            __(l1.val > l2.val
                cur.next _ l2
                l2 _ l2.next

            ____
                cur.next _ l1
                l1 _ l1.next
            cur _ cur.next

        w___(l1
            cur.next _ l1
            l1 _ l1.next
            cur _ cur.next
        w___(l2
            cur.next _ l2
            l2 _ l2.next
            cur _ cur.next
        r_ ans.next

    ___ mergeKLists(, lists: L..[ListNode])  ListNode:
        __(le.(lists) __ 0
            r_ N..

        i _ 0
        last _ le.(lists)-1
        j _ last

        w___(last !_ 0
            i _ 0
            j _ last

            w___(j > i
                lists[i] _ .mergeTwoLists(lists[i], lists[j])
                i +_ 1
                j -_ 1
                last _ j

        r_ lists[0]