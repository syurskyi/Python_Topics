'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , val, nextNode_ N..
        val  val
        next  nextNode

c_ Solution(o..
    ___ removeNthFromEnd  head, n
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast  head
        ___ _ __ r..(n
            fast  fast.next
        dummy  ListNode(-1)
        dummy.next  head
        prev  dummy
        node  head
        w.... fast:
            prev  node
            node  node.next
            fast  fast.next
        prev.next  node.next
        r.. dummy.next
