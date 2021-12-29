'''
Created on Oct 5, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        __ n.. root: r.. []
        h = self.getHeight(root)
        n = 2**h-1
        res = [['']*n ___ _ __ r..(h)]
        self.helper(root, 0, res, 0, n)
        r.. res
    
    ___ helper(self, root, level, res, start, end):
        __ n.. root:
            r..
        mid = (start+end)//2
        res[level][mid] = s..(root.val)
        self.helper(root.left, level+1, res, start, mid-1)
        self.helper(root.right, level+1, res, mid+1, end)
    
    ___ getHeight(self, root):
        __ n.. root: r.. 0
        r.. max(self.getHeight(root.left),\
                   self.getHeight(root.right))+1
    
    ___ test(self):
        testCases = [
            TreeNode(1, TreeNode(2)),
            TreeNode(1, TreeNode(2, N.., TreeNode(4)), TreeNode(3)),
            TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5)),
        ]
        ___ root __ testCases:
            result = self.printTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
