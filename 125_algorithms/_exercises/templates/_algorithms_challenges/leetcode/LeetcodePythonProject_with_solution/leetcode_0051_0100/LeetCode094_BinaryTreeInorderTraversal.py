'''
Created on Jan 29, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ inorderTraversal  root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result    # list
        __ n.. root:
            r.. result
        stack    # list
        node = root
        w.... node:
            stack.a..(node)
            node = node.left
        w.... stack:
            node = stack.pop()
            result.a..(node.val)
            __ node.right:
                node = node.right
                w.... node:
                    stack.a..(node)
                    node = node.left
        r.. result
    
    ___ test
        root = TreeNode(1, N.., TreeNode(2, TreeNode(3)))
        result = inorderTraversal(root)
        print(result)

___ main
    Solution().test()

__ _____ __ _____
    main()