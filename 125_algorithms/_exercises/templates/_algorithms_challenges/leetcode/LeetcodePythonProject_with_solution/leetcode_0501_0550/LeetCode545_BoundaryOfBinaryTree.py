'''
Created on Aug 20, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ boundaryOfBinaryTree  root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ n.. root: r.. []
        __ n.. root.left a.. n.. root.right: r.. [root.val]
        leftBoundary = getLeft(root)
        leaves    # list
        getLeaves(root, leaves)
        rightBoundary = getRight(root)
        r.. leftBoundary + leaves + rightBoundary
    
    ___ getLeft  root
        result = [root.val]
        root = root.left
        w.... root:
            __ root.left o. root.right:
                result.a..(root.val)
            __ root.left:
                root = root.left
            ____:
                root = root.right
        r.. result
    
    ___ getLeaves  root, leaves
        __ n.. root: r..
        __ n.. root.left a.. n.. root.right:
            leaves.a..(root.val)
            r..
        getLeaves(root.left, leaves)
        getLeaves(root.right, leaves)
    
    ___ getRight  root
        result    # list
        root = root.right
        w.... root:
            __ root.left o. root.right:
                result.a..(root.val)
            __ root.right:
                root = root.right
            ____:
                root = root.left
        result.r..
        r.. result
    
    ___ test
        testCases = [
            TreeNode(1, N.., TreeNode(2, TreeNode(3), TreeNode(4))),
        ]
        ___ root __ testCases:
            res = boundaryOfBinaryTree(root)
            print('result: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
