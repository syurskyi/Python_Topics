# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @param root, a tree node
    # @return an integer
    ___ sumNumbers(self, root):
        res = 0  # global variable for sum
        num = 0
        sn(root, num)
        r.. res

    ___ sn(self, root, num):
        __ root __ N..
            r..
        ____ root.left __ N.. a.. root.right __ N..
            num += root.val
            res += num
        ____:
            num += root.val
            sn(root.left, 10 * num)
            sn(root.right, 10 * num)
