'''
Created on Mar 21, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        backMap = {}
        kNode = self.dfs(root, k, backMap)
        queue = [kNode]
        visited = set([kNode])
        while queue:
            curr = queue.pop(0)
            __ n.. curr.left and n.. curr.right:
                r.. curr.val
            __ curr.left and curr.left n.. __ visited:
                queue.a..(curr.left)
                visited.add(curr.left)
            __ curr.right and curr.right n.. __ visited:
                queue.a..(curr.right)
                visited.add(curr.right)
            __ curr __ backMap and backMap[curr] n.. __ visited:
                queue.a..(backMap[curr])
                visited.add(backMap[curr])
        r.. -1
    
    ___ dfs(self, root, k, backMap):
        __ root.val __ k:
            r.. root
        __ root.left:
            backMap[root.left] = root
            left = self.dfs(root.left, k, backMap)
            __ left:
                r.. left
        __ root.right:
            backMap[root.right] = root
            right = self.dfs(root.right, k, backMap)
            __ right:
                r.. right
        r.. N..
    
    ___ test(self):
        testCases = [
            
        ]
        ___ root, k __ testCases:
            result = self.findClosestLeaf(root, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
