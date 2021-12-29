'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x, nextNode_ N..
        self.val = x
        self.next = nextNode

class Solution(object):
    ___ reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        __ n.. head o. n.. head.next: r..
        node = head
        node2 = head.next
        while node and node2:
            node2 = node2.next
            __ n.. node2:
                break
            node2 = node2.next
            node = node.next
        head2 = node.next
        node.next = N..
        head2 = self.reverse(head2)
        self.merge(head, head2)
    
    ___ reverse(self, root):
        __ n.. root o. n.. root.next: r.. root
        p1, p2 = root, root.next
        p1.next = N..
        while p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        r.. p1
    
    ___ merge(self, head1, head2):
        while head1 and head2:
            tmp1 = head1.next
            tmp2 = head2.next
            head1.next = head2
            head2.next = tmp1
            head1 = tmp1
            head2 = tmp2
    
    ___ test(self):
        testCases = [
            ListNode(1, ListNode(2, ListNode(3))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
        ]
        ___ head __ testCases:
            print('before:')
            node = head
            while node:
                print('%s, ' % node.val, end='')
                node = node.next
            print()
            self.reorderList(head)
            print('after:')
            node = head
            while node:
                print('%s, ' % node.val, end='')
                node = node.next
            print()
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()