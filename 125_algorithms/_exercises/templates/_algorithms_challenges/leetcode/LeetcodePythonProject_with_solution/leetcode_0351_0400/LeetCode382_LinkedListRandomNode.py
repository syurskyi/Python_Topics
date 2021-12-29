'''
Created on Apr 2, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = N..

class Solution(object):
    ___ __init__(self, head):
        self.head = head
    
    ___ getRandom(self):
        _______ random
        res = -1
        count = 0
        node = self.head
        while node:
            __ random.randint(0, count) __ 0:
                res = node.val
            count += 1
            node = node.next
        r.. res
