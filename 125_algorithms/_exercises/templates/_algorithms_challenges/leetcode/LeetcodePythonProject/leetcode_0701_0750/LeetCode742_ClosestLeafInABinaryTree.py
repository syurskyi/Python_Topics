'''
Created on Mar 21, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ findClosestLeaf(self, root, k
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        backMap = {}
        kNode = self.dfs(root, k, backMap)
        queue = [kNode]
        visited = set([kNode])
        w___ queue:
            curr = queue.pop(0)
            __ not curr.left and not curr.right:
                r_ curr.val
            __ curr.left and curr.left not in visited:
                queue.append(curr.left)
                visited.add(curr.left)
            __ curr.right and curr.right not in visited:
                queue.append(curr.right)
                visited.add(curr.right)
            __ curr in backMap and backMap[curr] not in visited:
                queue.append(backMap[curr])
                visited.add(backMap[curr])
        r_ -1
    
    ___ dfs(self, root, k, backMap
        __ root.val __ k:
            r_ root
        __ root.left:
            backMap[root.left] = root
            left = self.dfs(root.left, k, backMap)
            __ left:
                r_ left
        __ root.right:
            backMap[root.right] = root
            right = self.dfs(root.right, k, backMap)
            __ right:
                r_ right
        r_ None
    
    ___ test(self
        testCases = [
            
        ]
        for root, k in testCases:
            result = self.findClosestLeaf(root, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
