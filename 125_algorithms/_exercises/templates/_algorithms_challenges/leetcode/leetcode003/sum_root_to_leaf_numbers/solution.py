# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    ___ sumNumbers(self, root):
        self.res = 0  # global variable for sum
        num = 0
        self.sn(root, num)
        r.. self.res

    ___ sn(self, root, num):
        __ root __ N..
            r..
        ____ root.left __ N.. a.. root.right __ N..
            num += root.val
            self.res += num
        ____:
            num += root.val
            self.sn(root.left, 10 * num)
            self.sn(root.right, 10 * num)
