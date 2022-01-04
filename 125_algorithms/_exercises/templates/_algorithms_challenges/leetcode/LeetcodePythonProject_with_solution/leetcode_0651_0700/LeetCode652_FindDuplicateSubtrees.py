'''
Created on Oct 4, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res    # list
        postorder(root, {}, res)
        r.. res
    
    ___ postorder(self, cur, hashmap, res):
        __ n.. cur: r.. '#'
        serial = '%s,%s,%s' % (cur.val,\
                postorder(cur.left, hashmap, res),\
                postorder(cur.right, hashmap, res))
        __ hashmap.get(serial, 0) __ 1:
            res.a..(cur)
        hashmap[serial] = hashmap.get(serial, 0)+1
        r.. serial
    
    ___ test
        testCases = [
            TreeNode(2, TreeNode(1), TreeNode(1)),
            TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4))),
        ]
        ___ root __ testCases:
            res = findDuplicateSubtrees(root)
            print('result: %s' % [node.val ___ node __ res])
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
