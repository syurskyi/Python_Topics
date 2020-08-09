'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, x, nextNode=None
        self.val = x
        self.next = nextNode

class Solution(object
    ___ reorderList(self, head
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        __ not head or not head.next: r_
        node = head
        node2 = head.next
        w___ node and node2:
            node2 = node2.next
            __ not node2:
                break
            node2 = node2.next
            node = node.next
        head2 = node.next
        node.next = None
        head2 = self.reverse(head2)
        self.merge(head, head2)
    
    ___ reverse(self, root
        __ not root or not root.next: r_ root
        p1, p2 = root, root.next
        p1.next = None 
        w___ p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        r_ p1
    
    ___ merge(self, head1, head2
        w___ head1 and head2:
            tmp1 = head1.next
            tmp2 = head2.next
            head1.next = head2
            head2.next = tmp1
            head1 = tmp1
            head2 = tmp2
    
    ___ test(self
        testCases = [
            ListNode(1, ListNode(2, ListNode(3))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
        ]
        ___ head in testCases:
            print('before:')
            node = head
            w___ node:
                print('%s, ' % node.val, end='')
                node = node.next
            print()
            self.reorderList(head)
            print('after:')
            node = head
            w___ node:
                print('%s, ' % node.val, end='')
                node = node.next
            print()
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()