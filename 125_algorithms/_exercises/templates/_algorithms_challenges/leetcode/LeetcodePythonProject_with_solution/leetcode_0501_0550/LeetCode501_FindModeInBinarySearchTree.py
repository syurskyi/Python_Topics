'''
Created on May 10, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
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
        w.... node:
            stack.a..(node)
            node = node.left
        w.... stack:
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
            w.... node0:
                stack.a..(node0)
                node0 = node0.left
        r.. res
    
    ___ test
        testCases = [
            TreeNode(1),
        ]
        ___ root __ testCases:
            result = findMode(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

