# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # def minDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     # Recursion
    #     if root is None:
    #         return 0
    #     ld = self.minDepth(root.left)
    #     rd = self.minDepth(root.right)
    #     if ld != 0 and rd != 0:
    #         # handle 0 case!
    #         return 1 + min(ld, rd)
    #     return 1 + ld +rd

    ___ minDepth  root
        # BFS
        __ root is N..:
            r_ 0
        queue = [root]
        depth, rightMost = 1, root
        w.. l.. queue) > 0:
            node = queue.pop(0)
            __ node.left is N.. and node.right is N..:
                break
            __ node.left is n.. N..:
                queue.append(node.left)
            __ node.right is n.. N..:
                queue.append(node.right)
            __ node __ rightMost:
                # reach the current level end
                depth += 1
                __ node.right is n.. N..:
                    rightMost = node.right
                ____
                    rightMost = node.left
        r_ depth

