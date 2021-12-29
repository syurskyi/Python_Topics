'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result    # list
        queue    # list
        nextQueue    # list
        elem    # list
        __ n.. root:
            r.. result
        queue.a..(root)
        while queue:
            node = queue.pop(0)
            elem.a..(node.val)
            __ node.left:
                nextQueue.a..(node.left)
            __ node.right:
                nextQueue.a..(node.right)
            __ n.. queue:
                result.insert(0, elem)
                queue = nextQueue
                nextQueue    # list
                elem    # list
        r.. result
    
    ___ test(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        result = self.levelOrderBottom(root)
        print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()

    