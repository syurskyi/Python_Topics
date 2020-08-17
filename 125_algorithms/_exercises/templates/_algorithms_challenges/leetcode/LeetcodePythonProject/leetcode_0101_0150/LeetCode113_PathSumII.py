'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ pathSum(self, root, sumVal
        """
        :type root: TreeNode
        :type sumVal: int
        :rtype: List[List[int]]
        """
        result = []
        __ not root:
            r_ result
        elem = [root.val]
        self.dfs(result, elem, root, sumVal-root.val)
        r_ result
    
    ___ dfs(self, result, elem, root, sumVal
        __ not root:
            r_
        __ sumVal __ 0 and not root.left and not root.right:
            result.append(list(elem))
            r_
        __ root.left:
            elem.append(root.left.val)
            self.dfs(result, elem, root.left, sumVal-root.left.val)
            elem.p..
        __ root.right:
            elem.append(root.right.val)
            self.dfs(result, elem, root.right, sumVal-root.right.val)
            elem.p..
    
    ___ test(self
        root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
        sumVal = 22
        result = self.pathSum(root, sumVal)
        print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()