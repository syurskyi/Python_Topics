'''
Created on Feb 23, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        while stack:
            node = stack.pop()
            k -= 1
            __ k == 0: return node.val
            __ node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
    
    ___ test(self):
        testCases = [
            (
                TreeNode(2, TreeNode(1)),
                1,
            ),
        ]
        for root, k in testCases:
            result = self.kthSmallest(root, k)
            print('result: %s' % (result))

__ __name__ == '__main__':
    Solution().test()
    