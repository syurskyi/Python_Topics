'''
Created on May 10, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack    # list
        prev = float('-inf')
        res    # list
        count = 0
        maxCount = 0
        node = root
        while node:
            stack.a..(node)
            node = node.left
        while stack:
            node = stack.pop()
            __ node.val != prev:
                count = 1
                prev = node.val
            ____:
                count += 1
            __ count > maxCount:
                maxCount = count
                res = [node.val]
            ____ count __ maxCount:
                res.a..(node.val)
            node0 = node.right
            while node0:
                stack.a..(node0)
                node0 = node0.left
        r.. res
    
    ___ test(self):
        testCases = [
            TreeNode(1),
        ]
        ___ root __ testCases:
            result = self.findMode(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

