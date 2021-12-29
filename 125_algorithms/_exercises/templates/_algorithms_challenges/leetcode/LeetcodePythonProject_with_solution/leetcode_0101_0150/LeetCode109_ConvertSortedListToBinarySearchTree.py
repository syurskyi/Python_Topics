'''
Created on May 30, 2018

@author: tongq
'''
# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        __ not head: return None
        node = head
        length = 0
        self.h = head
        while node:
            node = node.next
            length += 1
        return self.helper(0, length-1)
    
    ___ helper(self, l, r):
        __ l > r:
            return None
        mid = (l+r)//2
        left = self.helper(l, mid-1)
        root = TreeNode(self.h.val)
        self.h = self.h.next
        right = self.helper(mid+1, r)
        root.left = left
        root.right = right
        return root
