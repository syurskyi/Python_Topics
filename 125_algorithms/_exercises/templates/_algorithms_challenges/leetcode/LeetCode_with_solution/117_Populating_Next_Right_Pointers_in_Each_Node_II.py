# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

c_ Solution o..
    # def connect(self, root):
    #     """
    #     :type root: TreeLinkNode
    #     :rtype: nothing
    #     """
    # level by level
    #     if root is None:
    #         return
    #     nodes = [root]
    #     while len(nodes) != 0:
    #         next_step = []
    #         last = None
    #         for node in nodes:
    #             if last is not None:
    #                 last.next = node
    #             if node.left is not None:
    #                 next_step.append(node.left)
    #             if node.right is not None:
    #                 next_step.append(node.right)
    #             last = node
    #         nodes = next_step

    ___ connect  root
        # https://discuss.leetcode.com/topic/28580/java-solution-with-constant-space
        dummyHead = TreeLinkNode(-1)
        pre = dummyHead
        w.. root is n.. N..:
            __ root.left is n.. N..:
                pre.next = root.left
                pre = pre.next
            __ root.right is n.. N..:
                pre.next = root.right
                pre = pre.next
            root = root.next
            __ root is N..:
                pre = dummyHead
                root = dummyHead.next
                dummyHead.next = N..


