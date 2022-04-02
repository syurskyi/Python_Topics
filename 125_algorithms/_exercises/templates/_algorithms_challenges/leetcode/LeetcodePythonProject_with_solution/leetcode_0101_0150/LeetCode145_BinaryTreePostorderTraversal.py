'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ postorderTraversal  root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ n.. root: r.. []
        stack, result = [root], []
        w.... stack:
            node = stack[-1] # peek
            __ n.. node.left a.. n.. node.right:
                pop = stack.pop()
                result.a..(pop.val)
            ____:
                __ node.right:
                    stack.a..(node.right)
                    node.right = N..
                __ node.left:
                    stack.a..(node.left)
                    node.left = N..
        r.. result
    
    ___ test
        testCases = [
            TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7, N.., TreeNode(9)))
        ]
        ___ root __ testCases:
            result = postorderTraversal(root)
            print('result: %s' % (result))

__ _____ __ _____
    Solution().test()
