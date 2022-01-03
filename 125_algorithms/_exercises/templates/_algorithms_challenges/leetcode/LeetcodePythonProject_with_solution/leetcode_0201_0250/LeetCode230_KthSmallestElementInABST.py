'''
Created on Feb 23, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
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
    
    ___ test
        testCases = [
            (
                TreeNode(2, TreeNode(1)),
                1,
            ),
        ]
        ___ root, k __ testCases:
            result = kthSmallest(root, k)
            print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()
    