'''
Created on Feb 23, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ kthSmallest  root, k
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
            node = stack.p.. )
            k -_ 1
            __ k __ 0: r.. node.val
            __ node.right:
                node = node.right
                w.... node:
                    stack.a..(node)
                    node = node.left
    
    ___ test
        testCases = [
            (
                TreeNode(2, TreeNode(1,
                1,
            ),
        ]
        ___ root, k __ testCases:
            result = kthSmallest(root, k)
            print('result: %s' % (result

__ _____ __ _____
    Solution().test()
    