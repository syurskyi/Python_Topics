"""
The node has an extra attribute parent which point to the father of itself.
The root's parent is null.


Definition of ParentTreeNode:
class ParentTreeNode:
    ___ __init__(self, val
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    ___ lowestCommonAncestorII(self, root, a, b
        """
        :type root: ParentTreeNode
        :type a: ParentTreeNode
        :type b: ParentTreeNode
        :rtype: ParentTreeNode
        """
        __ not root:
            r_ root

        nodes = set()

        w___ a:
            nodes.add(a)
            a = a.parent

        w___ b:
            __ b in nodes:
                r_ b
            b = b.parent

        r_ root
