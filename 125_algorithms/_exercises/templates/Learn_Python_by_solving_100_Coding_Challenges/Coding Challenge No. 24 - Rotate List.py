# Rotate List
# Question: Given a list, rotate the list to the right by k places, where k is non-negative.
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL
# Solutions:

class ListNode(object):
    ___ __init__(self, x):
        self.val _ x
        self.next _ None

    ___ to_list(self):
        r_ [self.val] + self.next.to_list() __ self.next ____ [self.val]

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    ___ rotateRight(self, head, k):
        __ head __ None:
            r_ None
        temp _ head
        ___ i __ ra..(0,k):
            __ temp.next __ None:
                temp _ head
            ____
                temp _ temp.next
        newLast _ head
        while temp.next !_ None:
            temp _ temp.next
            newLast _ newLast.next
        temp.next _ head
        newHead _ newLast.next
        newLast.next _ None
        r_ newHead


__  -n __ "__main__":
    n1 _ ListNode(1)
    n2 _ ListNode(2)
    n3 _ ListNode(3)
    n4 _ ListNode(4)
    n5 _ ListNode(5)
    n1.next _ n2
    n2.next _ n3
    n3.next _ n4
    n4.next _ n5
    r _ Solution().rotateRight(n1, 2)
    print ( r.to_list() )