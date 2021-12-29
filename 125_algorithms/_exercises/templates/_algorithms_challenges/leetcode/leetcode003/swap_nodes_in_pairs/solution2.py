# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    ___ swapPairs(self, head):
        __ head __ N..
            r.. head
        res = N..
        res_end = N..
        temp = N..
        temp_end = N..
        i = 1
        while head __ n.. N..
            next_node = head.next
            # Append current node to temp list
            __ temp __ N..
                temp_end = head
            head.next = temp
            temp = head
            __ i % 2 __ 0:
                # Append temp to res
                __ res __ N..
                    res = temp
                    res_end = temp_end
                ____:
                    res_end.next = temp
                    res_end = temp_end
                temp = N..
            i += 1
            head = next_node
        __ temp __ n.. N..
            __ res __ N..
                res = temp
                res_end = temp_end
            ____:
                res_end.next = temp
                res_end = temp_end
        r.. res
