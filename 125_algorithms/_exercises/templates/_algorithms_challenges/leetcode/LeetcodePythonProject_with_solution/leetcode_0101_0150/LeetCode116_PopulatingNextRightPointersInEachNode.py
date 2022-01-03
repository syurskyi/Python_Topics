'''
Created on Feb 4, 2017

@author: MT
'''

# Definition for binary tree with next pointer.
c_ TreeLinkNode:
    ___ - , x):
        val = x
        left = N..
        right = N..
        next = N..

c_ Solution:
    # @param root, a tree link node
    # @return nothing
    ___ connect(self, root):
        lastHead = root
        lastCurrent = N..
        currentHead = N..
        w.... lastHead:
            lastCurrent = lastHead
            w.... lastCurrent:
                __ n.. currentHead:
                    currentHead = lastCurrent.left
                    current =  lastCurrent.left
                ____:
                    current.next = lastCurrent.left
                    current = current.next
                __ currentHead:
                    current.next = lastCurrent.right
                    current = current.next
                lastCurrent = lastCurrent.next
            lastHead = currentHead
            currentHead = N..
    
    ___ test
        pass