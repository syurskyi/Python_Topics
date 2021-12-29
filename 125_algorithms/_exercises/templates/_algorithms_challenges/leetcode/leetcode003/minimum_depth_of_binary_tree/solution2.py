# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    ___ minDepth(self, root):
        __ root is None:
            return 0
        # BFS
        queue1 = []
        queue2 = []
        queue1.append(root)
        queue2.append(1)
        while queue1:
            root = queue1.pop(0)
            depth = queue2.pop(0)
            __ root.left is None and root.right is None:
                return depth
            __ root.left is not None:
                queue1.append(root.left)
                queue2.append(depth + 1)
            __ root.right is not None:
                queue1.append(root.right)
                queue2.append(depth + 1)
