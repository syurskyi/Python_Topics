# Rotate List
# Question: Given a list, rotate the list to the right by k places, where k is non-negative.
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL
# Solutions:

c_ ListNode(object):
    ___  -(, x):
        val _ x
        next _ N..

    ___ to_list
        r_ [val] + next.to_list() __ next ____ [val]

c_ Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    ___ rotateRight(, head, k):
        __ head __ N..:
            r_ N..
        temp _ head
        ___ i __ ra..(0,k):
            __ temp.next __ N..:
                temp _ head
            ____
                temp _ temp.next
        newLast _ head
        w___ temp.next !_ N..:
            temp _ temp.next
            newLast _ newLast.next
        temp.next _ head
        newHead _ newLast.next
        newLast.next _ N..
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