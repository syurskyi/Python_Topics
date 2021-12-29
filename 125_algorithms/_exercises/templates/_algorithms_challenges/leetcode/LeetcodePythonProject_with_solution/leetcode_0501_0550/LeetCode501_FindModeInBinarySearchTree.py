'''
Created on May 10, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        prev = float('-inf')
        res = []
        count = 0
        maxCount = 0
        node = root
        while node:
            stack.append(node)
            node = node.left
        while stack:
            node = stack.pop()
            __ node.val != prev:
                count = 1
                prev = node.val
            else:
                count += 1
            __ count > maxCount:
                maxCount = count
                res = [node.val]
            elif count == maxCount:
                res.append(node.val)
            node0 = node.right
            while node0:
                stack.append(node0)
                node0 = node0.left
        return res
    
    ___ test(self):
        testCases = [
            TreeNode(1),
        ]
        for root in testCases:
            result = self.findMode(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()

