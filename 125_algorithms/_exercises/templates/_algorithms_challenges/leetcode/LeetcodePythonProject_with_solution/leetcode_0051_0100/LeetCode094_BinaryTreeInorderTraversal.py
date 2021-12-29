'''
Created on Jan 29, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result    # list
        __ n.. root:
            r.. result
        stack    # list
        node = root
        while node:
            stack.a..(node)
            node = node.left
        while stack:
            node = stack.pop()
            result.a..(node.val)
            __ node.right:
                node = node.right
                while node:
                    stack.a..(node)
                    node = node.left
        r.. result
    
    ___ test(self):
        root = TreeNode(1, N.., TreeNode(2, TreeNode(3)))
        result = self.inorderTraversal(root)
        print(result)

___ main():
    Solution().test()

__ __name__ __ '__main__':
    main()