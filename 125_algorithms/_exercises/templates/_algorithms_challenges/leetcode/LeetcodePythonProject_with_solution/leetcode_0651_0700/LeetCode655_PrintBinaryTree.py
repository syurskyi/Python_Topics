'''
Created on Oct 5, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        __ not root: return []
        h = self.getHeight(root)
        n = 2**h-1
        res = [['']*n for _ in range(h)]
        self.helper(root, 0, res, 0, n)
        return res
    
    ___ helper(self, root, level, res, start, end):
        __ not root:
            return
        mid = (start+end)//2
        res[level][mid] = str(root.val)
        self.helper(root.left, level+1, res, start, mid-1)
        self.helper(root.right, level+1, res, mid+1, end)
    
    ___ getHeight(self, root):
        __ not root: return 0
        return max(self.getHeight(root.left),\
                   self.getHeight(root.right))+1
    
    ___ test(self):
        testCases = [
            TreeNode(1, TreeNode(2)),
            TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)),
            TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5)),
        ]
        for root in testCases:
            result = self.printTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
