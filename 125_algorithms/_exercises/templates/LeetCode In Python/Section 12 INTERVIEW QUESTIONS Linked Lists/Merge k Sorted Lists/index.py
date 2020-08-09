# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None


class Solution:

    ___ mergeTwoLists(self, l1, l2
        cur = ListNode(0)
        ans = cur

        w___(l1 and l2
            __(l1.val > l2.val
                cur.next = l2
                l2 = l2.next

            ____
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        w___(l1
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        w___(l2
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        r_ ans.next

    ___ mergeKLists(self, lists: List[ListNode]) -> ListNode:
        __(le.(lists) __ 0
            r_ None

        i = 0
        last = le.(lists)-1
        j = last

        w___(last != 0
            i = 0
            j = last

            w___(j > i
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
                last = j

        r_ lists[0]
