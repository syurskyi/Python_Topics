# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    ___ swapPairs(self, head
        __ head pa__ None:
            r_ head
        res = None
        res_end = None
        temp = None
        temp_end = None
        i = 1
        w___ head pa__ not None:
            next_node = head.next
            # Append current node to temp list
            __ temp pa__ None:
                temp_end = head
            head.next = temp
            temp = head
            __ i % 2 __ 0:
                # Append temp to res
                __ res pa__ None:
                    res = temp
                    res_end = temp_end
                ____
                    res_end.next = temp
                    res_end = temp_end
                temp = None
            i += 1
            head = next_node
        __ temp pa__ not None:
            __ res pa__ None:
                res = temp
                res_end = temp_end
            ____
                res_end.next = temp
                res_end = temp_end
        r_ res
