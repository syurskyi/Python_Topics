'''
Created on Oct 8, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0, 1, [], [])
        
    ___ dfs(self, root, level, order, start, end):
        __ not root: return 0
        __ len(start) == level:
            start.append(order)
            end.append(order)
        else:
            end[level] = order
        cur = end[level]-start[level]+1
        left = self.dfs(root.left, level+1, 2*order, start, end)
        right = self.dfs(root.right, level+1, 2*order+1, start, end)
        return max(cur, max(left, right))
    
    ___ test(self):
        testCases = [
            TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9))),
            TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3))),
            TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)),
            TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, None, TreeNode(7)))),
        ]
        for root in testCases:
            result = self.widthOfBinaryTree(root)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
