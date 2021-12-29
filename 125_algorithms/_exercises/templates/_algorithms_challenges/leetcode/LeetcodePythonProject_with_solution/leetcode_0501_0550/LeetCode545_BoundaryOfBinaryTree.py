'''
Created on Aug 20, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ n.. root: r.. []
        __ n.. root.left and n.. root.right: r.. [root.val]
        leftBoundary = self.getLeft(root)
        leaves    # list
        self.getLeaves(root, leaves)
        rightBoundary = self.getRight(root)
        r.. leftBoundary + leaves + rightBoundary
    
    ___ getLeft(self, root):
        result = [root.val]
        root = root.left
        while root:
            __ root.left o. root.right:
                result.a..(root.val)
            __ root.left:
                root = root.left
            ____:
                root = root.right
        r.. result
    
    ___ getLeaves(self, root, leaves):
        __ n.. root: r..
        __ n.. root.left and n.. root.right:
            leaves.a..(root.val)
            r..
        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)
    
    ___ getRight(self, root):
        result    # list
        root = root.right
        while root:
            __ root.left o. root.right:
                result.a..(root.val)
            __ root.right:
                root = root.right
            ____:
                root = root.left
        result.reverse()
        r.. result
    
    ___ test(self):
        testCases = [
            TreeNode(1, N.., TreeNode(2, TreeNode(3), TreeNode(4))),
        ]
        ___ root __ testCases:
            res = self.boundaryOfBinaryTree(root)
            print('result: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
