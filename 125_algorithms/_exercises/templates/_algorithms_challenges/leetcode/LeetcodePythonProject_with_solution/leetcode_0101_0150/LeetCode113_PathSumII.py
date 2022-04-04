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
    ___ pathSum  root, sumVal
        """
        :type root: TreeNode
        :type sumVal: int
        :rtype: List[List[int]]
        """
        result    # list
        __ n.. root:
            r.. result
        elem = [root.val]
        dfs(result, elem, root, sumVal-root.val)
        r.. result
    
    ___ dfs  result, elem, root, sumVal
        __ n.. root:
            r..
        __ sumVal __ 0 a.. n.. root.left a.. n.. root.right:
            result.a..(l..(elem
            r..
        __ root.left:
            elem.a..(root.left.val)
            dfs(result, elem, root.left, sumVal-root.left.val)
            elem.pop()
        __ root.right:
            elem.a..(root.right.val)
            dfs(result, elem, root.right, sumVal-root.right.val)
            elem.pop()
    
    ___ test
        root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
        sumVal = 22
        result = pathSum(root, sumVal)
        print('result: %s' % (result

__ _____ __ _____
    Solution().test()