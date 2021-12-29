'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        r.. self.helper(inorder, 0, l..(inorder)-1, postorder, 0, l..(postorder)-1)
    
    ___ helper(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        __ inStart > inEnd o. postStart > postEnd:
            r.. N..
        val = postorder[postEnd]
        root = TreeNode(val)
        
        k = inorder.index(val)
        
        newInStart = inStart
        newInEnd = k-1
        newPostStart = postStart
        newPostEnd = postStart+k-inStart-1
        
        root.left = self.helper(inorder, newInStart, newInEnd,\
                                postorder, newPostStart, newPostEnd)
        
        newInStart = k+1
        newInEnd = inEnd
        newPostStart = postStart+k-inStart
        newPostEnd = postEnd-1
        
        root.right = self.helper(inorder, newInStart, newInEnd,\
                                 postorder, newPostStart, newPostEnd)
        
        r.. root
