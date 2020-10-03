# # Merge k Sorted Lists
# # Question: Merge k sorted linked lists and return it as one sorted list. Analyse and describe its complexity.
# # Solutions:
#
#
# c_ ListNode
#     ___  -  x
#         val _ x
#         next _ N..
#
#
# c_ Solution
#     # @param a list of ListNode
#     # @return a ListNode
#     ___ mergeKLists lists
#         __ le. ? __ 0
#             r_ N..
#         w___ le. ? > 1
#             nextLists _   # list
#             ___ i __ ra.. 0 le. ?-1,2
#                 ?.ap.. ? ?? ? ? + 1
#             __ le. ?%2__1
#                 ?.ap.. ? le. ? - 1
#             ? _ ?
#         r_ ? 0
#
#     ___ mergeLists  list1 list2
#         dummy _ ? 0
#         li.. _ ?
#         w___ ? !_ N.. an. ? !_ N..
#             __ ?.v.. < ?.v..
#                 li...n.. _ ?
#                 ? _ ?.n..
#             ____
#                 li...n.. _ ?
#                 ? _ ?.n..
#             li.. _ li...n..
#         __ ? __ N..
#             li...n.. _ ?
#         ____
#             li...n.. _ ?
#         r_ d__.n..
#
#     ___ printll  node
#         w___ ?
#             print ?.v..
#             n.. _ ?.n..
# __  -n __ ______
#     ll1 ?.n.. ?.n...n.. _ ? 2, ? 3, ? 5
#     ll2 ?.n.. ?.n...n.. _ ? 4, ? 7, ? 15
#     ll3 ?.n.. ?.n...n.. _ ? 6, ? 9, ? 10
#     ? .p..  ? .? ? ?,?]