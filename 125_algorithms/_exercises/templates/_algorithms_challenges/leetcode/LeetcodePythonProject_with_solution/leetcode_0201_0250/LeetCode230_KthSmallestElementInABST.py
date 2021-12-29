'''
Created on Feb 23, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
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
        stack    # list
        node = root
        w.... node:
            stack.a..(node)
            node = node.left
        w.... stack:
            node = stack.pop()
            k -= 1
            __ k __ 0: r.. node.val
            __ node.right:
                node = node.right
                w.... node:
                    stack.a..(node)
                    node = node.left
    
    ___ test(self):
        testCases = [
            (
                TreeNode(2, TreeNode(1)),
                1,
            ),
        ]
        ___ root, k __ testCases:
            result = self.kthSmallest(root, k)
            print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()
    