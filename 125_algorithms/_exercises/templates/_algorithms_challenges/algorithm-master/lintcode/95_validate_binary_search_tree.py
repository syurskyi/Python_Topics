"""
Main Concept:
since the fact,
if we said a tree is NOT a binary search tree,
and then the values we got by inorder traversal
is must be a non-descending sequence, that is, A[i+1] >= A[i].


Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    ___ isValidBST(self, root
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        node = root
        pre = None

        w___ node or stack:
            w___ node:
                stack.append(node)
                node = node.left

            node = stack.p..

            __ pre and node.val <= pre.val:
                r_ False

            pre = node

            node = node.right

        r_ True


class Solution:
    ans = True
    pre = None

    ___ isValidBST(self, root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ not root:
            r_ self.ans

        self.isValidBST(root.left)

        __ self.pre and root.val <= self.pre.val:
            self.ans = False
            r_ self.ans

        self.pre = root

        self.isValidBST(root.right)

        r_ self.ans
