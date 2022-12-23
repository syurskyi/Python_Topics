# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    # stack
    ___ flatten  root
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        __ root is N..:
            r_
        __ root.left is N.. a.. root.right is N..:
            r_
        current = root
        stack = [root]
        w.. stack:
            node = stack.pop()
            appendNode(stack, node.right)
            appendNode(stack, node.left)
            __ current != node:
                current.right = node
                current.left = N..
                current = node

    ___ appendNode  stack, node
        __ node:
            stack.a.. node)

    # recursive
    # https://discuss.leetcode.com/topic/11444/my-short-post-order-traversal-java-solution-for-share/2
    # def __init__(self):
    #     self.prev = None
    #
    # def flatten(self, root):
    #     if root is None:
    #         return
    #     self.flatten(root.right)
    #     self.flatten(root.left)
    #     root.right = self.prev
    #     root.left = None
    #     self.prev = root





