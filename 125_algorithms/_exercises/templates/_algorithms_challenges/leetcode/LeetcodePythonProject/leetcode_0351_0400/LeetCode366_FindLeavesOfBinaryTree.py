'''
Created on Mar 28, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ findLeaves(self, root
        res =   # list
        self.helper(root, res)
        r_ res
    
    ___ helper(self, root, res
        __ not root: r_ -1
        left = self.helper(root.left, res)
        right = self.helper(root.right, res)
        level = ma.(left, right)+1
        __ level < le.(res
            res[level].append(root.val)
        ____
            res.append([root.val])
        r_ level
    
    ___ findLeavesOwn(self, root
        __ not root: r_   # list
        result =   # list
        dummy = TreeNode(-1)
        dummy.left = root
        w___ dummy.left:
            tmpResult =   # list
            self.getLeaves(dummy, root, tmpResult)
            result.append(tmpResult)
        r_ result
    
    ___ getLeaves(self, parent, root, result
        __ not root: r_
        __ not root.left and not root.right:
            __ parent.left __ root:
                parent.left = None
            ____
                parent.right = None
            result.append(root.val)
        self.getLeaves(root, root.left, result)
        self.getLeaves(root, root.right, result)
    
    ___ test(self
        testCases = [
            TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),
        ]
        ___ root __ testCases:
            result = self.findLeaves(root)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
