'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = []
        nextQueue = []
        elem = []
        __ not root:
            return result
        queue.append(root)
        while queue:
            node = queue.pop(0)
            elem.append(node.val)
            __ node.left:
                nextQueue.append(node.left)
            __ node.right:
                nextQueue.append(node.right)
            __ not queue:
                result.insert(0, elem)
                queue = nextQueue
                nextQueue = []
                elem = []
        return result
    
    ___ test(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        result = self.levelOrderBottom(root)
        print('result: %s' % (result))

__ __name__ == '__main__':
    Solution().test()

    