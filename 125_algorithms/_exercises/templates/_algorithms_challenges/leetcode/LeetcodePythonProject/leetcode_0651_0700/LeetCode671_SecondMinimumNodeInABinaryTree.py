'''
Created on Oct 12, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ findSecondMinimumValue(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root: r_ -1
        first = float('inf')
        second = float('inf')
        queue = [root]
        w___ queue:
            node = queue.pop(0)
            __ node.val < first:
                second = first
                first = node.val
            ____ first < node.val < second:
                second = node.val
            __ node.left:
                queue.append(node.left)
            __ node.right:
                queue.append(node.right)
        r_ second __ second != float('inf') else -1
    
    ___ test(self
        testCases = [
            TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7))),
        ]
        for root in testCases:
            result = self.findSecondMinimumValue(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
