'''
Created on May 30, 2018

@author: tongq
'''
# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = N..

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        __ n.. head: r.. N..
        node = head
        length = 0
        self.h = head
        w.... node:
            node = node.next
            length += 1
        r.. self.helper(0, length-1)
    
    ___ helper(self, l, r):
        __ l > r:
            r.. N..
        mid = (l+r)//2
        left = self.helper(l, mid-1)
        root = TreeNode(self.h.val)
        self.h = self.h.next
        right = self.helper(mid+1, r)
        root.left = left
        root.right = right
        r.. root
