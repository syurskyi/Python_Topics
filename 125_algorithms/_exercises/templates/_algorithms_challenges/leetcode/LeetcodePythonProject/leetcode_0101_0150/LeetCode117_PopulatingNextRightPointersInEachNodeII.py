'''
Created on Feb 4, 2017

@author: MT
'''

# Definition for binary tree with next pointer.
class TreeLinkNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    ___ connect(self, root
        lastHead = root
        lastCurrent = None
        currentHead = None
        current = None
        w___ lastHead:
            lastCurrent = lastHead
            w___ lastCurrent:
                __ lastCurrent.left:
                    __ not currentHead:
                        currentHead = lastCurrent.left
                        current = currentHead
                    ____
                        current.next = lastCurrent.left
                        current = current.next
                __ lastCurrent.right:
                    __ not currentHead:
                        currentHead = lastCurrent.right
                        current = currentHead
                    ____
                        current.next = lastCurrent.right
                        current = current.next
                lastCurrent = lastCurrent.next
            lastHead = currentHead
            currentHead = None
