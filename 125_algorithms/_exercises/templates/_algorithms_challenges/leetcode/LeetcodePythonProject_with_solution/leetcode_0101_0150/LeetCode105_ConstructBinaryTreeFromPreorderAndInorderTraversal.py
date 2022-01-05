'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(o..):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(o..):
    ___ buildTree  preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        r.. helper(preorder, 0, l..(preorder)-1, inorder, 0, l..(inorder)-1)
    
    ___ helper  preorder, pstart, pend, inorder, istart, iend):
        __ pstart > pend o. istart > iend:
            r.. N..
        val = preorder[pstart]
        root = TreeNode(val)
        k = inorder.index(val)
        
        new_pstart = pstart+1
        new_pend = pstart+k-istart
        new_istart = istart
        new_iend = k-1
        
        root.left = helper(preorder, new_pstart, new_pend,\
                                inorder, new_istart, new_iend)
        
        new_pstart = pstart+k-istart+1
        new_pend = pend
        new_istart = k+1
        new_iend = iend
        
        root.right = helper(preorder, new_pstart, new_pend,\
                                inorder, new_istart, new_iend)
        
        r.. root
