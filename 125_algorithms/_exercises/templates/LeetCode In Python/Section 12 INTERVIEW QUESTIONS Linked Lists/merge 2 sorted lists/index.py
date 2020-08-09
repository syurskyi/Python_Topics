# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    ___ mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		cur = ListNode(0)
		ans = cur
		
		w___(l1 and l2
			__(l1.val>l2.val
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