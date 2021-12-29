'''
Created on Feb 4, 2017

@author: MT
'''

# Definition for binary tree with next pointer.
class TreeLinkNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..
        self.next = N..

class Solution:
    # @param root, a tree link node
    # @return nothing
    ___ connect(self, root):
        lastHead = root
        lastCurrent = N..
        currentHead = N..
        current = N..
        while lastHead:
            lastCurrent = lastHead
            while lastCurrent:
                __ lastCurrent.left:
                    __ n.. currentHead:
                        currentHead = lastCurrent.left
                        current = currentHead
                    ____:
                        current.next = lastCurrent.left
                        current = current.next
                __ lastCurrent.right:
                    __ n.. currentHead:
                        currentHead = lastCurrent.right
                        current = currentHead
                    ____:
                        current.next = lastCurrent.right
                        current = current.next
                lastCurrent = lastCurrent.next
            lastHead = currentHead
            currentHead = N..
