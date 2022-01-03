'''
Created on Aug 29, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        helper(root, res)
        r.. res[0]
    
    ___ helper(self, root, res):
        __ n.. root: r..
        helper(root.left, res)
        helper(root.right, res)
        leftSum = getSum(root.left)
        rightSum = getSum(root.right)
        res[0] += abs(leftSum-rightSum)
    
    ___ getSum(self, root):
        __ n.. root: r.. 0
        res = root.val
        res += getSum(root.left)
        res += getSum(root.right)
        r.. res
    
    ___ test
        testCases = [
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5))),
        ]
        ___ root __ testCases:
            result = findTilt(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
