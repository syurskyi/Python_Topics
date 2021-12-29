'''
Created on Mar 5, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        stack1, stack2    # list, []
        res    # list
        self.inOrderReg(root, target, stack1)
        self.inOrderRev(root, target, stack2)
        print('stack1: %s' % stack1)
        print('stack2: %s' % stack2)
        ___ _ __ r..(k):
            __ n.. stack1:
                res.a..(stack2.pop())
            ____ n.. stack2:
                res.a..(stack1.pop())
            ____ abs(stack1[-1]-target) <= abs(stack2[-1]-target):
                res.a..(stack1.pop())
            ____:
                res.a..(stack2.pop())
        r.. res
    
    ___ inOrderReg(self, root, target, stack):
        __ n.. root: r..
        self.inOrderReg(root.left, target, stack)
        __ root.val > target: r..
        stack.a..(root.val)
        self.inOrderReg(root.right, target, stack)
    
    ___ inOrderRev(self, root, target, stack):
        __ n.. root: r..
        self.inOrderRev(root.right, target, stack)
        __ root.val <= target: r..
        stack.a..(root.val)
        self.inOrderRev(root.left, target, stack)
    
    ___ test(self):
        root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(7)), TreeNode(15, TreeNode(13), TreeNode(20)))
        target = 13.5
        k = 5
        result = self.closestKValues(root, target, k)
        print('result: %s' % (result))
        print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
