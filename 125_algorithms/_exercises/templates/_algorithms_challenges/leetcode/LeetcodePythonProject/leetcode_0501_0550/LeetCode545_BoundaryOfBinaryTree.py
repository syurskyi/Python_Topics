'''
Created on Aug 20, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ boundaryOfBinaryTree(self, root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ not root: r_   # list
        __ not root.left and not root.right: r_ [root.val]
        leftBoundary = self.getLeft(root)
        leaves =   # list
        self.getLeaves(root, leaves)
        rightBoundary = self.getRight(root)
        r_ leftBoundary + leaves + rightBoundary
    
    ___ getLeft(self, root
        result = [root.val]
        root = root.left
        w___ root:
            __ root.left or root.right:
                result.append(root.val)
            __ root.left:
                root = root.left
            ____
                root = root.right
        r_ result
    
    ___ getLeaves(self, root, leaves
        __ not root: r_
        __ not root.left and not root.right:
            leaves.append(root.val)
            r_
        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)
    
    ___ getRight(self, root
        result =   # list
        root = root.right
        w___ root:
            __ root.left or root.right:
                result.append(root.val)
            __ root.right:
                root = root.right
            ____
                root = root.left
        result.reverse()
        r_ result
    
    ___ test(self
        testCases = [
            TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4))),
        ]
        ___ root __ testCases:
            res = self.boundaryOfBinaryTree(root)
            print('result: %s' % res)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
