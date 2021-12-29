'''
Created on Mar 28, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ findLeaves(self, root):
        res = []
        self.helper(root, res)
        return res
    
    ___ helper(self, root, res):
        __ not root: return -1
        left = self.helper(root.left, res)
        right = self.helper(root.right, res)
        level = max(left, right)+1
        __ level < len(res):
            res[level].append(root.val)
        else:
            res.append([root.val])
        return level
    
    ___ findLeavesOwn(self, root):
        __ not root: return []
        result = []
        dummy = TreeNode(-1)
        dummy.left = root
        while dummy.left:
            tmpResult = []
            self.getLeaves(dummy, root, tmpResult)
            result.append(tmpResult)
        return result
    
    ___ getLeaves(self, parent, root, result):
        __ not root: return
        __ not root.left and not root.right:
            __ parent.left == root:
                parent.left = None
            else:
                parent.right = None
            result.append(root.val)
        self.getLeaves(root, root.left, result)
        self.getLeaves(root, root.right, result)
    
    ___ test(self):
        testCases = [
            TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),
        ]
        for root in testCases:
            result = self.findLeaves(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
