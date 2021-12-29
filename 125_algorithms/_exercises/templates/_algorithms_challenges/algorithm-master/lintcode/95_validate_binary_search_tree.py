"""
Main Concept:
since the fact,
if we said a tree is NOT a binary search tree,
and then the values we got by inorder traversal
is must be a non-descending sequence, that is, A[i+1] >= A[i].


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    ___ isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack    # list
        node = root
        pre = N..

        w.... node o. stack:
            w.... node:
                stack.a..(node)
                node = node.left

            node = stack.pop()

            __ pre a.. node.val <= pre.val:
                r.. False

            pre = node

            node = node.right

        r.. True


class Solution:
    ans = True
    pre = N..

    ___ isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root:
            r.. self.ans

        self.isValidBST(root.left)

        __ self.pre a.. root.val <= self.pre.val:
            self.ans = False
            r.. self.ans

        self.pre = root

        self.isValidBST(root.right)

        r.. self.ans
