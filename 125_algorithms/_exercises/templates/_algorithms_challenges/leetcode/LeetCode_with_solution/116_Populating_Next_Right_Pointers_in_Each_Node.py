# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

c_ Solution o..
    ___ connect  root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        __ root is N..:
            r_
        nodes = [root]
        w.. l.. nodes) != 0:
            next_step = []
            last = N..
            ___ node __ nodes:
                __ last is not N..:
                    last.next = node
                __ node.left is not N..:
                    next_step.append(node.left)
                __ node.right is not N..:
                    next_step.append(node.right)
                last = node
            nodes = next_step


