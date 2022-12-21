# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution o..
    ___ oddEvenList  head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = head
        __ head is N..:
            r_ N..
        __ head.next is N..:
            r_ head
        even_head = even = head.next
        w.. odd.next is n.. N.. a.. even.next is n.. N..:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        r_ head

    # def oddEvenList(self, head):
    #     # slicing
    #     if (head != None):
    #         x = []
    #     else:
    #         return []
    #     while (head.next != None):
    #         x.append(head.val)
    #         head = head.next
    #     x.append(head.val)
    #     return x[0::2] + x[1::2]