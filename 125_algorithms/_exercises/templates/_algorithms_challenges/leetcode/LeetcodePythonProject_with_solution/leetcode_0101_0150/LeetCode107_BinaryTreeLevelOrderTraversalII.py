'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ levelOrderBottom  root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result    # list
        queue    # list
        nextQueue    # list
        elem    # list
        __ n.. root:
            r.. result
        queue.a..(root)
        w.... queue:
            node = queue.pop(0)
            elem.a..(node.val)
            __ node.left:
                nextQueue.a..(node.left)
            __ node.right:
                nextQueue.a..(node.right)
            __ n.. queue:
                result.insert(0, elem)
                queue = nextQueue
                nextQueue    # list
                elem    # list
        r.. result
    
    ___ test
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        result = levelOrderBottom(root)
        print('result: %s' % (result))

__ _____ __ _____
    Solution().test()

    