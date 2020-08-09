'''
Created on Oct 4, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ findDuplicateSubtrees(self, root
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        self.postorder(root, {}, res)
        r_ res
    
    ___ postorder(self, cur, hashmap, res
        __ not cur: r_ '#'
        serial = '%s,%s,%s' % (cur.val,\
                self.postorder(cur.left, hashmap, res),\
                self.postorder(cur.right, hashmap, res))
        __ hashmap.get(serial, 0) __ 1:
            res.append(cur)
        hashmap[serial] = hashmap.get(serial, 0)+1
        r_ serial
    
    ___ test(self
        testCases = [
            TreeNode(2, TreeNode(1), TreeNode(1)),
            TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4))),
        ]
        ___ root in testCases:
            res = self.findDuplicateSubtrees(root)
            print('result: %s' % [node.val ___ node in res])
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
