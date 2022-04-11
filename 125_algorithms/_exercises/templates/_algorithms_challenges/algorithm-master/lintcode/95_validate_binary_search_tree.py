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


c_ Solution:
    ___ isValidBST  root
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack    # list
        node root
        pre N..

        w.... node o. stack:
            w.... node:
                stack.a..(node)
                node node.left

            node stack.p.. )

            __ pre a.. node.val <_ pre.val:
                r.. F..

            pre node

            node node.right

        r.. T..


c_ Solution:
    ans T..
    pre N..

    ___ isValidBST  root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root:
            r.. ans

        isValidBST(root.left)

        __ pre a.. root.val <_ pre.val:
            ans F..
            r.. ans

        pre root

        isValidBST(root.right)

        r.. ans
