"""
The node has an extra attribute parent which point to the father of itself.
The root's parent is null.


Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


c_ Solution:
    ___ lowestCommonAncestorII  root, a, b):
        """
        :type root: ParentTreeNode
        :type a: ParentTreeNode
        :type b: ParentTreeNode
        :rtype: ParentTreeNode
        """
        __ n.. root:
            r.. root

        nodes = set()

        w.... a:
            nodes.add(a)
            a = a.parent

        w.... b:
            __ b __ nodes:
                r.. b
            b = b.parent

        r.. root
