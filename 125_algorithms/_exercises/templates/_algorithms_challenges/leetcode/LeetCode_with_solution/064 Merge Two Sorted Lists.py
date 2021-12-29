"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of
the first two lists.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x):
        self.val = x
        self.next = N..

    ___ __repr__(self):
        r.. repr(self.val)

    ___ __str__(self):
        r.. "%d, %s"%(self.val, self.next)

class Solution:
    ___ mergeTwoLists(self, l1, l2):
        """
        Linked List
        assuming ascending order
        :param l1: ListNode
        :param l2: ListNode
        :return:
        """
        dummy = ListNode(0)
        dummy.next = l1

        pre = dummy
        the_other = l2
        while pre and pre.next:
            cur = pre.next
            __ the_other and cur.val>the_other.val:
                # insert
                temp = the_other.next
                pre.next, the_other.next = the_other, cur

                the_other = temp  # advance the_other
            pre = pre.next


        # dangling list
        __ the_other:
            pre.next = the_other  # appending

        r.. dummy.next

__ __name____"__main__":
    length = 10
    list1 = [ListNode(2*i) ___ i __ xrange(length)]
    list2 = [ListNode(2*i+1) ___ i __ xrange(length)]
    ___ i __ xrange(length-1):
        list1[i].next = list1[i+1]
        list2[i].next = list2[i+1]

    lst = Solution().mergeTwoLists(list1[0], list2[0])
    print lst
