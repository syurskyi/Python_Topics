'''
Created on Oct 4, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res    # list
        self.postorder(root, {}, res)
        r.. res
    
    ___ postorder(self, cur, hashmap, res):
        __ n.. cur: r.. '#'
        serial = '%s,%s,%s' % (cur.val,\
                self.postorder(cur.left, hashmap, res),\
                self.postorder(cur.right, hashmap, res))
        __ hashmap.get(serial, 0) __ 1:
            res.a..(cur)
        hashmap[serial] = hashmap.get(serial, 0)+1
        r.. serial
    
    ___ test(self):
        testCases = [
            TreeNode(2, TreeNode(1), TreeNode(1)),
            TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4))),
        ]
        ___ root __ testCases:
            res = self.findDuplicateSubtrees(root)
            print('result: %s' % [node.val ___ node __ res])
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
