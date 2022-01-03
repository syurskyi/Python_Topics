'''
Created on Feb 9, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ n.. root: r.. []
        stack = [root]
        res    # list
        w.... stack:
            node = stack.pop()
            res.a..(node.val)
            __ node.right:
                stack.a..(node.right)
            __ node.left:
                stack.a..(node.left)
        r.. res
    
    ___ test
        testCases = [
            TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7, N.., TreeNode(9)))
        ]
        ___ root __ testCases:
            result = preorderTraversal(root)
            print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()