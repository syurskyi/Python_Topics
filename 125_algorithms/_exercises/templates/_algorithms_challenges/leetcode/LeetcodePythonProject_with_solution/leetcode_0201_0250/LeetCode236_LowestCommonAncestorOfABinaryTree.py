'''
Created on Feb 26, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        __ not root:
            return None
        elif root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        __ l and r:
            return root
        elif not l and not r:
            return None
        else:
            return r __ not l else l
    
    ___ test(self):
        node1 = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
        node2 = TreeNode(1, TreeNode(0), TreeNode(8))
        root = TreeNode(3)
        root.left = node1
        root.right = node2
        result = self.lowestCommonAncestor(root, node2, node1)
        print(result)
        __ result:
            print(result.val)

__ __name__ == '__main__':
    Solution().test()
