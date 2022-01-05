'''
Created on Mar 21, 2018

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ findClosestLeaf  root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        backMap    # dict
        kNode = dfs(root, k, backMap)
        queue = [kNode]
        visited = set([kNode])
        w.... queue:
            curr = queue.pop(0)
            __ n.. curr.left a.. n.. curr.right:
                r.. curr.val
            __ curr.left a.. curr.left n.. __ visited:
                queue.a..(curr.left)
                visited.add(curr.left)
            __ curr.right a.. curr.right n.. __ visited:
                queue.a..(curr.right)
                visited.add(curr.right)
            __ curr __ backMap a.. backMap[curr] n.. __ visited:
                queue.a..(backMap[curr])
                visited.add(backMap[curr])
        r.. -1
    
    ___ dfs  root, k, backMap):
        __ root.val __ k:
            r.. root
        __ root.left:
            backMap[root.left] = root
            left = dfs(root.left, k, backMap)
            __ left:
                r.. left
        __ root.right:
            backMap[root.right] = root
            right = dfs(root.right, k, backMap)
            __ right:
                r.. right
        r.. N..
    
    ___ test
        testCases = [
            
        ]
        ___ root, k __ testCases:
            result = findClosestLeaf(root, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
