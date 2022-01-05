'''
Created on May 30, 2018

@author: tongq
'''
# Definition for singly-linked list.
c_ ListNode(object):
    ___ - , x):
        val = x
        next = N..

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ sortedListToBST  head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        __ n.. head: r.. N..
        node = head
        length = 0
        h = head
        w.... node:
            node = node.next
            length += 1
        r.. helper(0, length-1)
    
    ___ helper  l, r):
        __ l > r:
            r.. N..
        mid = (l+r)//2
        left = helper(l, mid-1)
        root = TreeNode(h.val)
        h = h.next
        right = helper(mid+1, r)
        root.left = left
        root.right = right
        r.. root
