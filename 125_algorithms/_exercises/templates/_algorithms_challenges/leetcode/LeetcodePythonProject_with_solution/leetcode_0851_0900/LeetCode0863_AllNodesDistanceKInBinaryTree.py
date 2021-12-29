'''
Created on Sep 18, 2019

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        hashmap = {}
        self.find(root, target, hashmap)
        res    # list
        self.dfs(root, target, K, hashmap[root], res, hashmap)
        r.. res
    
    ___ find(self, root, target, hashmap):
        __ n.. root: r.. -1
        __ root __ target:
            hashmap[root] = 0
            r.. 0
        left = self.find(root.left, target, hashmap)
        __ left >= 0:
            hashmap[root] = left+1
            r.. left+1
        right = self.find(root.right, target, hashmap)
        __ right >= 0:
            hashmap[root] = right+1
            r.. right+1
        r.. -1
    
    ___ dfs(self, root, target, k, length, res, hashmap):
        __ n.. root: r..
        __ root __ hashmap:
            length = hashmap[root]
        __ length __ k:
            res.a..(root.val)
        self.dfs(root.left, target, k, length+1, res, hashmap)
        self.dfs(root.right, target, k, length+1, res, hashmap)

__ __name__ __ '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    
    res = Solution().distanceK(root, root.left.right, 1)
    print('res: %s' % res)
