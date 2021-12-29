'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ not root: return []
        stack, result = [root], []
        while stack:
            node = stack[-1] # peek
            __ not node.left and not node.right:
                pop = stack.pop()
                result.append(pop.val)
            else:
                __ node.right:
                    stack.append(node.right)
                    node.right = None
                __ node.left:
                    stack.append(node.left)
                    node.left = None
        return result
    
    ___ test(self):
        testCases = [
            TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7, None, TreeNode(9)))
        ]
        for root in testCases:
            result = self.postorderTraversal(root)
            print('result: %s' % (result))

__ __name__ == '__main__':
    Solution().test()
