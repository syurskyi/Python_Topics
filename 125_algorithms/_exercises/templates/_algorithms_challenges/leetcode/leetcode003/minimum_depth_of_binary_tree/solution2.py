# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @param root, a tree node
    # @return an integer
    ___ minDepth(self, root):
        __ root __ N..
            r.. 0
        # BFS
        queue1    # list
        queue2    # list
        queue1.a..(root)
        queue2.a..(1)
        w.... queue1:
            root = queue1.pop(0)
            depth = queue2.pop(0)
            __ root.left __ N.. a.. root.right __ N..
                r.. depth
            __ root.left __ n.. N..
                queue1.a..(root.left)
                queue2.a..(depth + 1)
            __ root.right __ n.. N..
                queue1.a..(root.right)
                queue2.a..(depth + 1)
