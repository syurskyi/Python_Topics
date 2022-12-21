c_ Solution o..
    # https://leetcode.com/problems/convert-bst-to-greater-tree/solution/
    # def __init__(self):
    #     self.total = 0

    # def convertBST(self, root):
    #     if root is not None:
    #         self.convertBST(root.right)
    #         self.total += root.val
    #         root.val = self.total
    #         self.convertBST(root.left)
    #     return root

    ___ convertBST  root
        total = 0
        
        node = root
        stack =    # list
        w.. stack or node is n.. N..:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            w.. node is n.. N..:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        r_ root
