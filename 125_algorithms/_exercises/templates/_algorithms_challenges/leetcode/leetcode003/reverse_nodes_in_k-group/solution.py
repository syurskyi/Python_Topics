# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    ___ reverseKGroup  head, k):
        __ head __ N..
            r.. head
        h = head
        n = 0
        w.... h __ n.. N..
            n += 1
            h = h.next
        num_groups = n / k
        # if k is larger than n, return head
        __ num_groups __ 0:
            r.. head
        # `last_group` is the 1-base index of the last group node
        last_group = num_groups * k
        res = N..
        res_end = N..
        temp = N..
        temp_end = N..
        i = 1
        w.... head __ n.. N..
            next_node = head.next
            __ i <= last_group:
                # Appended current node to `temp` list
                __ temp __ N..
                    temp_end = head
                head.next = temp
                temp = head
                # Appended `temp` list to `res`
                __ i % k __ 0:
                    __ res __ N..
                        res = temp
                        res_end = temp_end
                    ____:
                        res_end.next = temp
                        res_end = temp_end
                    # Reset `temp`
                    temp = N..
            ____:
                res_end.next = head
                break
            i += 1
            head = next_node
        r.. res
