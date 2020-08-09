# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ rob(self, root
        __ not root: r_ 0
        result = self.helper(root)
        r_ max(result[0], result[1])
    
    # return include, exclude
    ___ helper(self, root
        __ not root: r_ [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        include = max(left[0]+right[0], root.val+left[1]+right[1])
        exclude = max(left[0]+right[0], left[1]+right[1])
        r_ [include, exclude]
    
    ___ test(self
        testCases = [
            TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1))),
            TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1))),
        ]
        for root in testCases:
            result = self.rob(root)
            print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()

