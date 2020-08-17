# Definition for a  binary tree node
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    ___ minDepth(self, root
        __ root pa__ None:
            r_ 0
        # BFS
        queue1 = []
        queue2 = []
        queue1.append(root)
        queue2.append(1)
        w___ queue1:
            root = queue1.pop(0)
            depth = queue2.pop(0)
            __ root.left pa__ None and root.right pa__ None:
                r_ depth
            __ root.left pa__ not None:
                queue1.append(root.left)
                queue2.append(depth + 1)
            __ root.right pa__ not None:
                queue1.append(root.right)
                queue2.append(depth + 1)
