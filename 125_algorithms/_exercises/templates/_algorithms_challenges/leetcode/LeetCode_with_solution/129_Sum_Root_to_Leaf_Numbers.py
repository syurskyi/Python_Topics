# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ sumNumbers  root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ root is N..:
            r_ 0
        res = 0
        # bfs with queue
        queue = [(root, root.val)]
        w.. l.. queue) > 0:
            curr, curr_value = queue.pop(0)
            __ curr.left is N.. and curr.right is N..:
                res += curr_value
                c_
            __ curr.left:
                queue.append((curr.left, curr_value * 10 + curr.left.val))
            __ curr.right:
                queue.append((curr.right, curr_value * 10 + curr.right.val))
        r_ res
