'''
Created on Feb 8, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ sumNumbers(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root: r_ 0
        res = []
        self.helper(root, str(root.val), res)
        resNum = su.([int(val) ___ val in res])
        r_ resNum
        
    ___ helper(self, root, curr, res
        __ not root.left and not root.right:
            res.append(curr)
        __ root.left:
            self.helper(root.left, curr+str(root.left.val), res)
        __ root.right:
            self.helper(root.right, curr+str(root.right.val), res)
    
    ___ test(self
#         root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        result = self.sumNumbers(root)
        print(result)

__ __name__ __ '__main__':
    Solution().test()