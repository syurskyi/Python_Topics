# # Definition for singly-linked list.
# # # class ListNode:
# # #     ___ __init__(self, x
# # #         self.val = x
# # #         self.next = None
# #
# # c_ Solution
# #     ___ mergeTwoLists l1 LN.. l2 LN..  LN..
# # 		cur _ LN.. 0
# # 		ans _ ?
# #
# # 		w___ ? a.. ?
# # 			__ ?.v.. > ?.v..
# # 				c__.n.. _ ?
# # 				? _ ?.n..
# # 			____
# # 				c__.n.. _ ?
# # 				? _ ?.n..
# # 			cur _ c__.n..
# #
# # 		w___ ?
# # 			c__.n.. _ ?
# # 			? _ ?.n..
# # 			c__ _ c__.n..
# #
# # 		w___ ?
# # 			c__.n.. _ ?
# # 			? _ ?.n..
# # 			c__ _ c__.n..
# # 		r_ a__.n..