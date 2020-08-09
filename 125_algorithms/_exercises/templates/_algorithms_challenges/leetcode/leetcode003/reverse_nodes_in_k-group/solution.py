# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    ___ reverseKGroup(self, head, k
        __ head is None:
            r_ head
        h = head
        n = 0
        w___ h is not None:
            n += 1
            h = h.next
        num_groups = n / k
        # if k is larger than n, return head
        __ num_groups __ 0:
            r_ head
        # `last_group` is the 1-base index of the last group node
        last_group = num_groups * k
        res = None
        res_end = None
        temp = None
        temp_end = None
        i = 1
        w___ head is not None:
            next_node = head.next
            __ i <= last_group:
                # Appended current node to `temp` list
                __ temp is None:
                    temp_end = head
                head.next = temp
                temp = head
                # Appended `temp` list to `res`
                __ i % k __ 0:
                    __ res is None:
                        res = temp
                        res_end = temp_end
                    ____
                        res_end.next = temp
                        res_end = temp_end
                    # Reset `temp`
                    temp = None
            ____
                res_end.next = head
                break
            i += 1
            head = next_node
        r_ res
