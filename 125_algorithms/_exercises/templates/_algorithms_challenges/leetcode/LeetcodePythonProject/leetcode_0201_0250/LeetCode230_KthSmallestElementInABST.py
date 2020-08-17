'''
Created on Feb 23, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ kthSmallest(self, root, k
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        w___ node:
            stack.append(node)
            node = node.left
        w___ stack:
            node = stack.p..
            k -= 1
            __ k __ 0: r_ node.val
            __ node.right:
                node = node.right
                w___ node:
                    stack.append(node)
                    node = node.left
    
    ___ test(self
        testCases = [
            (
                TreeNode(2, TreeNode(1)),
                1,
            ),
        ]
        ___ root, k in testCases:
            result = self.kthSmallest(root, k)
            print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()
    