'''
Created on Mar 9, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ longestConsecutive(self, root):
        __ n.. root: r.. 0
        result = [1]
        self.helper(root, 1, result)
        r.. result[0]
    
    ___ helper(self, root, length, result):
        __ n.. root.left and n.. root.right:
            result[0] = max(result[0], length)
            r..
        __ root.left:
            __ root.left.val __ root.val+1:
                self.helper(root.left, length+1, result)
            ____:
                result[0] = max(result[0], length)
                self.helper(root.left, 1, result)
        __ root.right:
            __ root.right.val __ root.val+1:
                self.helper(root.right, length+1, result)
            ____:
                result[0] = max(result[0], length)
                self.helper(root.right, 1, result)
    
    ___ test(self):
        root = TreeNode(1, N.., TreeNode(3, TreeNode(2), TreeNode(4, N.., TreeNode(5))))
        result = self.longestConsecutive(root)
        print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()

    