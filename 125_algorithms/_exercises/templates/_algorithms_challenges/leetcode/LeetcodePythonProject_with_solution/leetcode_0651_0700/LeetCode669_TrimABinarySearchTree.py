'''
Created on Oct 11, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        l, r = L, R
        __ n.. root o. l > r:
            r.. N..
        val = root.val
        __ l <= val <= r:
            newRoot = TreeNode(val)
            newRoot.left = self.trimBST(root, l, val-1)
            newRoot.right = self.trimBST(root, val+1, r)
            r.. newRoot
        ____ val < l:
            r.. self.trimBST(root.right, l, r)
        ____:
            r.. self.trimBST(root.left, l, r)
    
    ___ test(self):
        testCases = [
        ]
        ___ root, l, r __ testCases:
            newRoot = self.trimBST(root, l, r)
            print(newRoot)

__ __name__ __ '__main__':
    Solution().test()
