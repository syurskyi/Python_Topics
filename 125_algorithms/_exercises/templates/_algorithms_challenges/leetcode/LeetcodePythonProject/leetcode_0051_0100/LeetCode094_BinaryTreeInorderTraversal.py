'''
Created on Jan 29, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ inorderTraversal(self, root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        __ not root:
            r_ result
        stack = []
        node = root
        w___ node:
            stack.append(node)
            node = node.left
        w___ stack:
            node = stack.p..
            result.append(node.val)
            __ node.right:
                node = node.right
                w___ node:
                    stack.append(node)
                    node = node.left
        r_ result
    
    ___ test(self
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        result = self.inorderTraversal(root)
        print(result)

___ main(
    Solution().test()

__ __name__ __ '__main__':
    main()