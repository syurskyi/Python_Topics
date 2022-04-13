'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , x, nextNode_ N..
        val x
        next nextNode

c_ Solution(o..
    ___ reorderList  head
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        __ n.. head o. n.. head.next: r..
        node head
        node2 head.next
        w.... node a.. node2:
            node2 node2.next
            __ n.. node2:
                _____
            node2 node2.next
            node node.next
        head2 node.next
        node.next N..
        head2 reverse(head2)
        merge(head, head2)
    
    ___ reverse  root
        __ n.. root o. n.. root.next: r.. root
        p1, p2 root, root.next
        p1.next N..
        w.... p2:
            tmp  p2.next
            p2.next p1
            p1 p2
            p2 tmp
        r.. p1
    
    ___ merge  head1, head2
        w.... head1 a.. head2:
            tmp1 head1.next
            tmp2 head2.next
            head1.next head2
            head2.next tmp1
            head1 tmp1
            head2 tmp2
    
    ___ test
        testCases [
            ListNode(1, ListNode(2, ListNode(3))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
        ]
        ___ head __ testCases:
            print('before:')
            node head
            w.... node:
                print('%s, ' % node.val, e.._'')
                node node.next
            print()
            reorderList(head)
            print('after:')
            node head
            w.... node:
                print('%s, ' % node.val, e.._'')
                node node.next
            print()
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()