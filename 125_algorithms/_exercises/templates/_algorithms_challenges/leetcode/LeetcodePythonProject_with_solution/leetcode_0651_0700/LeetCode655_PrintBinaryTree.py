'''
Created on Oct 5, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ printTree  root
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        __ n.. root: r.. []
        h = getHeight(root)
        n = 2**h-1
        res = [['']*n ___ _ __ r..(h)]
        helper(root, 0, res, 0, n)
        r.. res
    
    ___ helper  root, level, res, start, end
        __ n.. root:
            r..
        mid = (start+end)//2
        res[level][mid] = s..(root.val)
        helper(root.left, level+1, res, start, mid-1)
        helper(root.right, level+1, res, mid+1, end)
    
    ___ getHeight  root
        __ n.. root: r.. 0
        r.. m..(getHeight(root.left),\
                   getHeight(root.right))+1
    
    ___ test
        testCases = [
            TreeNode(1, TreeNode(2)),
            TreeNode(1, TreeNode(2, N.., TreeNode(4)), TreeNode(3)),
            TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5)),
        ]
        ___ root __ testCases:
            result = printTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
