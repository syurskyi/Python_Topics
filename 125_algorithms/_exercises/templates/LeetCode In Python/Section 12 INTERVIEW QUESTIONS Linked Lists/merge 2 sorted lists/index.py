# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

c_ Solution:
    ___ mergeTwoLists l1: ListNode, l2: ListNode)  ListNode:
		cur _ ListNode(0)
		ans _ cur
		
		w___(l1 a.. l2
			__(l1.val>l2.val
				cur.n.. _ l2
				l2 _ l2.n..
			____
				cur.n.. _ l1
				l1 _ l1.n..
			cur _ cur.n..
			
		w___(l1
			cur.n.. _ l1
			l1 _ l1.n..
			cur _ cur.n..
		
		w___(l2
			cur.n.. _ l2
			l2 _ l2.n..
			cur _ cur.n..
		r_ ans.n..