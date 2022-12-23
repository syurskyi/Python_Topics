# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def findSecondMinimumValue(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     # Brute force
    #     values = set()
    #     self.dfs(root, values)
    #     ans, min_value = float('inf'), root.val
    #     for n in values:
    #         if min_value < n and n < ans:
    #             ans = n
    #     return ans if ans < float('inf') else -1

    # def dfs(self, root, values):
    #     if not root:
    #         return
    #     values.add(root.val)
    #     self.dfs(root.left, values)
    #     self.dfs(root.right, values)

    ___ findSecondMinimumValue  root
        __ n.. root:
            r_ -1
        ans = float('inf')
        min_val = root.val
        stack = [root]
        w.. stack:
            curr = stack.pop()
            __ n.. curr:
                c_
            __ min_val < curr.val < ans:
                ans = curr.val
            ____ curr.val __ min_val:
                stack.a.. curr.left)
                stack.a.. curr.right)
        r_ ans __ ans < float('inf') ____ -1
