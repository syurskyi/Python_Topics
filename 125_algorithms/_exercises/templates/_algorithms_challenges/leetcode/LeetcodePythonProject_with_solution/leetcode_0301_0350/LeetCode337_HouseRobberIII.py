# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(object):
    ___ rob(self, root):
        __ n.. root: r.. 0
        result = helper(root)
        r.. max(result[0], result[1])
    
    # return include, exclude
    ___ helper(self, root):
        __ n.. root: r.. [0, 0]
        left = helper(root.left)
        right = helper(root.right)
        include = max(left[0]+right[0], root.val+left[1]+right[1])
        exclude = max(left[0]+right[0], left[1]+right[1])
        r.. [include, exclude]
    
    ___ test
        testCases = [
            TreeNode(3, TreeNode(2, N.., TreeNode(3)), TreeNode(3, N.., TreeNode(1))),
            TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, N.., TreeNode(1))),
        ]
        ___ root __ testCases:
            result = rob(root)
            print('result: %s' % (result))

__ __name__ __ '__main__':
    Solution().test()

