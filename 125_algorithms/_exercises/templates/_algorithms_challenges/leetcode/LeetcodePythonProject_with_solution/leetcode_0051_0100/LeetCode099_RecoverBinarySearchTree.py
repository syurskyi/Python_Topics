'''
Created on Jan 31, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        __ not root: return
        self.first = None
        self.second = None
        self.prev = None
        self.inOrder(root)
        __ self.second and self.first:
            val = self.second.val
            self.second.val = self.first.val
            self.first.val = val
    
    ___ inOrder(self, root):
        __ not root:
            return
        self.inOrder(root.left)
        __ self.prev:
            __ root.val < self.prev.val:
                __ not self.first:
                    self.first = self.prev
                self.second = root
        self.prev = root
        self.inOrder(root.right)
    
    ___ test(self):
        pass

__ __name__ == '__main__':
    Solution().test()